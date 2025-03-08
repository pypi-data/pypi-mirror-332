# baikal api client

# baikal controller client

import logging
import re
import time
import urllib.parse
from typing import Any, Dict, List, Tuple
from uuid import uuid4

import arrow
import httpx
from bs4 import BeautifulSoup
from pydantic import validate_call

from . import settings
from .models import (
    VALID_TOKEN_CHARS,
    Account,
    AddBookRequest,
    AddUserRequest,
    Book,
    DeleteBookRequest,
    DeleteUserRequest,
    User,
)
from .passwd import Accounts
from .version import __version__

LOG_SOUP = False
POST_DELETE_TIMEOUT = 5


class BrowserException(Exception):
    pass


class BrowserInterfaceFailure(BrowserException):
    pass


class InitFailed(BrowserException):
    pass


class AddFailed(BrowserException):
    pass


class DeleteFailed(BrowserException):
    pass


class UnexpectedServerResponse(BrowserException):
    pass


class NoSuchElementException(BrowserException):
    pass


logger = logging.getLogger(__name__)
CLIENT_TIMEOUT = 300
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"


class APIError(Exception):
    def __init__(self, response):
        if getattr(response, "is_error", False):
            error = response.json()
            message = error.get("error", repr(response))
            detail = error.get("detail", [])
        else:
            message = repr(response)
            detail = []
        super().__init__(message)
        self.detail = detail


class APIClient:

    def __init__(self, url=None):
        if url is None:
            url = settings.CALDAV_URL
        self.url = url.strip("/")
        self.cert = (settings.CLIENT_CERT, settings.CLIENT_KEY)
        self.client = httpx.Client(cert=(settings.CLIENT_CERT, settings.CLIENT_KEY), follow_redirects=True)
        self.headers = {"X-Api-Key": str(settings.API_KEY), "User-Agent": USER_AGENT}
        self.timeout = CLIENT_TIMEOUT
        self.logged_in = False
        self.logger = logger
        self.load_time = time.time()

    def quit(self):
        if self.logged_in:
            self.logout()
        self.client.close()
        self.client = None

    def _request(self, func, path, **kwargs):
        raise_on_error = kwargs.pop("raise_on_error", True)
        log_errors = kwargs.pop("log_errors", True)
        kwargs.setdefault("timeout", self.timeout)
        boundary = kwargs.pop("multipart_form", None)
        if boundary is not None:
            self.client.headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        try:
            self.response = func(self.url + path, **kwargs)
        except httpx.HTTPError as e:
            breakpoint()
            if raise_on_error:
                raise
            return APIError(e)
        finally:
            self.client.headers.pop("Content-Type", None)
        self.request = self.response.request
        if self.response.is_error:
            breakpoint()
            ret = APIError(self.response)
            if log_errors:
                self.print_error(ret, logger.error)
            if raise_on_error:
                raise ret
            return ret

        self.logger.debug(f"request: {self.request.method} {self.request.url}")
        self.logger.debug(f"request_content: {self.response.request.content.decode()}")
        self._log_headers("request", self.response.request.headers)
        self._log_headers("response", self.response.headers)
        self.dom = BeautifulSoup(self.response.text, features="html.parser")
        self.loaded_time = time.time()
        return self.dom

    def _log_headers(self, label, headers):
        self.logger.debug(f"{label}_headers:")
        for k, v in dict(headers).items():
            self.logger.debug(f"{k} {v}")

    def get(self, url, **kwargs):
        self.logger.debug(f"GET {url}")
        return self._request(self.client.get, url, **kwargs)

    def post(self, url, **kwargs):
        self.logger.debug(f"POST {url}")
        return self._request(self.client.post, url, **kwargs)

    def patch(self, url, **kwargs):
        self.logger.debug(f"PATCH {url}")
        return self._request(self.client.patch, url, **kwargs)

    def delete(self, url, **kwargs):
        self.logger.debug(f"DELETE {url}")
        return self._request(self.client.delete, url, **kwargs)

    @validate_call
    def post_form(self, path: str, data: Dict[str, Any]):
        boundary = f"----boundary{uuid4().hex}"
        boundary = "----geckoformboundaryccff3ff29bfd70de26178f03ce5668d8"
        body = ""
        for key, value in data.items():
            body += f"--{boundary}\r\n"
            body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'
            body += f"{value}\r\n"
        body += f"--{boundary}--\r\n"

        ret = self.post(path, content=body.encode("utf-8"), multipart_form=boundary)
        return ret

    @validate_call
    def meta_refresh(self):
        # process meta refresh if present
        if self.dom.find("meta"):
            attrs = self.dom.find("meta").attrs
            if attrs.get("http-equiv", None) == "refresh":
                content = attrs.get("content", ";")
                fields = [c.strip() for c in content.split(";")]
                refresh_time = None
                path = str(self.request.url)
                for i, field in enumerate(fields):
                    if i == 0:
                        refresh_time = self.loaded_time + int(field)
                    elif field.startswith("url="):
                        path = field[4:]
                if refresh_time is None:
                    raise BrowserInterfaceFailure(f"meta refresh delay time missing: {content=}")
                if time.time() < refresh_time:
                    self.logger.warning(f"meta_refresh: waiting; delay={refresh_time - time.time()}")
                    while time.time() < refresh_time:
                        time.sleep(1)
                if self.request.method != "GET":
                    raise BrowserInterfaceFailure(f"unexpected meta refresh method: {self.request.method}")
                self.get(path)

    def response_path(self):
        return str(self.response.url)[len(self.url) :]


class Session:

    def __init__(self):
        self.logger = logging.getLogger(settings.LOGGER_NAME)
        self.logger.setLevel(settings.LOG_LEVEL)
        self.logger.info("Browser session startup")
        self.driver = None
        self.startup()

    @validate_call
    def reset(self) -> Dict[str, str]:
        self.logger.debug("request: reset")
        if self.driver:
            self.shutdown()
        self.startup()
        self.reset_time = arrow.now()
        self.logger.debug("request: reset complete")
        return dict(message="session reset")

    @validate_call
    def startup(self) -> Dict[str, str]:
        self.logger.debug("request: startup")
        if self.driver:
            message = "ignoring startup; already started"
            self.logger.warning(message)
        else:
            try:
                self.driver = APIClient()
            except Exception as e:
                raise InitFailed(e)
            self.logged_in = False
            self.startup_time = arrow.now()
            self.reset_time = None
            message = "session started"
        self.logger.debug("request: startup complete")
        return dict(message=message)

    def shutdown(self):
        self.logger.debug("request: shutdown")
        if self.driver:
            self.driver.quit()
            self.driver = None
        else:
            self.logger.warning("already shutdown")
        self.logger.debug("shutdown: complete")

    def _normalize_text(self, text, ignore_case):
        if text is not None:
            text = " ".join(text.strip().split())
            if ignore_case:
                text = text.lower()
        return text

    @validate_call
    def _find_element(
        self,
        name: str,
        selector: str,
        *,
        parent: Any | None = None,
        with_text: str | None = None,
        with_classes: List[str] | None = [],
        allow_none: bool | None = False,
        ignore_case: bool | None = False,
        click: bool | None = False,
    ) -> Any:
        if parent is None:
            parent = self.driver.dom
        elements = parent.select(selector)
        if with_text:
            with_text = self._normalize_text(with_text, ignore_case)
            elements = [e for e in elements if self._normalize_text(e.text, ignore_case) == with_text]
        if with_classes:
            with_classes = [self._normalize_text(c, ignore_case) for c in with_classes]
            class_matches = []
            for element in elements:
                element_classes = [self._normalize_text(c, ignore_case) for c in element.attrs.get("class", [])]
                matches = {cls: (cls in element_classes) for cls in with_classes}
                if all(matches.values()):
                    class_matches.append(element)
            elements = class_matches
        if len(elements) == 1:
            return self._click(elements[0], click)
        elif len(elements) > 1:
            raise BrowserInterfaceFailure(
                f"{name} unexpected multiple matches: {selector=} {with_text=} {with_classes=}"
            )
        elif allow_none:
            return None
        raise BrowserInterfaceFailure(f"{name} not found: {selector=} {with_text=} {with_classes=}")

    def _click(self, element, enabled=True):
        if enabled:
            self.driver.get(element.attrs["href"])
        return element

    @validate_call
    def _find_elements(
        self,
        name: str,
        selector: str,
        *,
        parent: Any | None = None,
        with_text: str | None = None,
        allow_none: bool | None = False,
        ignore_case: bool | None = False,
        click: bool | None = False,
    ) -> List[Any]:
        if parent is None:
            parent = self.driver.dom
        elements = parent.select(selector)
        if elements and with_text:
            with_text = self._normalize_text(with_text, ignore_case)
            elements = [element for element in elements if self._normalize_text(element.text, ignore_case) == with_text]
        if elements:
            self._click(elements[0], click)
        elif not allow_none:
            raise BrowserInterfaceFailure(f"{name} no matching elements found: {selector=} {with_text=}")
        return elements

    @validate_call
    def _click_button(self, name: str, selector: str, *, parent: Any | None = None, with_text: str | None = None):
        return self._find_element(name, selector, parent=parent, with_text=with_text, click=True)

    @validate_call
    def _check_popups(self, require_none: bool | None = False, ignore_case: bool | None = False) -> List[str]:
        messages = self.driver.dom.select("body #message")
        ret = [self._normalize_text(m.text, ignore_case) for m in messages]
        if ret and require_none:
            raise UnexpectedServerResponse(repr(ret))
        return ret

    @validate_call
    def _set_text(self, name: str, selector: str, text: str | None):
        breakpoint()
        element = self._find_element(name, selector)
        element.clear()
        if text:
            element.send_keys(text)

    @validate_call
    def login(self, admin: Account):
        self.logger.debug("request: login")
        if self.logged_in == admin.username:
            self.logger.debug(f"login: already logged in as {admin.username}")
            return

        dom = self.driver.get("/admin/")

        if dom.title == "Baïkal Maintainance":
            raise BrowserInterfaceFailure("server not initialized")

        self.logger.debug(f"connected: {self.driver.dom.title}")

        post_dom = self.driver.post_form("/admin/", dict(auth=1, login=admin.username, password=admin.password))
        self.logger.debug(post_dom.title)
        self._check_popups(require_none=True)
        self.logged_in = admin.username
        self.logger.debug(f"login: authenticated as {admin.username}")

    @validate_call
    def initialize(self, admin: Account) -> Dict[str, str]:
        self.logger.debug("request: initialize")
        self.driver.get("/admin/install/")
        strings = list(self.driver.dom.strings)
        if len(strings) == 1 and strings[0].startswith("Installation was already completed."):
            raise InitFailed("initialize: already initialized")

        breakpoint()
        if self.driver.title != "Baïkal Maintainance":
            raise BrowserInterfaceFailure(f"unexpected page title: {self.driver.title}")

        self.logger.info(f"Initialize: {self.driver.title}")

        # TODO: support parameters for configuration options

        while True:
            if self._find_elements(
                "start button",
                "body .btn-success",
                with_text="Start using Baïkal",
                allow_none=True,
                click=True,
            ):
                if self.driver.current_url.endswith("/baikal/admin/"):
                    self.logger.info("initialize: successfully configured")
                    return dict(message="initialized")
                else:
                    raise InitFailed("unexpected url after start button: {self.driver.current_url}")
            jumbotron = self._find_element("initialization title", "body .jumbotron")
            title_text = jumbotron.text.lower()
            if "database setup" in title_text:
                self.logger.info("initialize: confirming default database config")
                self._click_button("database init save changes button", "body form .btn", with_text="Save changes")
            elif "initialization wizard" in title_text:
                raise RuntimeError("unimplemented")
            # self.logger.info("initialize: setting timezone")
            # timezone = self._find_element("init timezone selector", 'body form select[name="data[timezone]"]')
            # select = Select(timezone)
            # select.select_by_visible_text("UTC")
            # self.logger.info("initialize: clearing invite address")
            # self._set_text("init invite address", 'body form input[name="data[invite_from]"]', None)
            # self.logger.info("initialize: setting admin password")
            # self._set_text(
            #   "init admin password",
            #   'body form input[name="data[admin_passwordhash]"]',
            #   admin.password,
            # )
            # self._set_text(
            #   "init admin password confirmation",
            #   'body form input[name="data[admin_passwordhash_confirm]"]',
            #   admin.password,
            # )
            # self._click_button("general init save changes button", "body form .btn", with_text="Save changes")
            else:
                raise InitFailed(f"unexpected init title: {jumbotron.text}")

        raise BrowserInterfaceFailure("initialization failed")

    def logout(self):
        self.logger.debug("request: logout")
        if self.logged_in:
            self.driver.get("/admin/")
            self._click_navbar_link("logout", "Logout")
            self.logged_in = False
            links = self._navbar_links().keys()
            if list(links) != ["Web Admin"]:
                raise BrowserInterfaceFailure(f"logout: unexpected navbar content after logout: {links}")
            self.logger.debug("logout: logged out")
        else:
            self.logger.debug("logout: not logged in")

    @validate_call
    def _navbar_links(self):
        navbars = self.driver.dom.select("div.navbar")
        if len(navbars) != 1:
            breakpoint()
            raise BrowserInterfaceFailure("multiple navbars located")
        elements = navbars[0].find_all("a")
        links = {e.text.strip(): e.attrs.get("href", None) for e in elements if e.text.strip()}
        return links

    @validate_call
    def _click_navbar_link(self, name: str, label: str):
        links = self._navbar_links()
        url = links.get(label, None)
        if url:
            self.driver.get(url)
        else:
            raise BrowserInterfaceFailure(f"{name}: navbar link {label} not found in: {list(links.keys())}")

    @validate_call
    def _table_rows(self, name: str, allow_none: bool | None = True):
        table = self._find_element(f"{name} table", "body table", with_classes=[name])
        tbody = self._find_element(f"{name} table body", "tbody", parent=table, allow_none=True)
        if tbody is not None:
            table = tbody
        rows = table.find_all("tr")
        if not rows:
            message = f"no {name} table body rows found"
            if allow_none:
                self.logger.warning(message)
            else:
                raise BrowserInterfaceFailure(message)
        return rows

    @validate_call
    def _parse_user_row(self, row: Any) -> Dict[str, str]:
        col_username = self._find_element("user table row displayname column", "td.col-username", parent=row)
        fields = col_username.find_all(True)
        username = fields[1].text
        mailto = urllib.parse.unquote(fields[3].attrs["href"])
        match = re.match("^mailto:(.*) <(.*)>$", mailto)
        groups = None
        if match:
            groups = match.groups()
        if not groups:
            raise BrowserInterfaceFailure(f"failed decoding user mailto: {mailto}")
        displayname, email = groups
        ret = self._parse_row_info("user", row)
        ret.update(dict(username=username, displayname=displayname, email=email))
        return ret

    @validate_call
    def _parse_book_row(self, row: Any) -> Dict[str, str]:
        ret = {}
        col_displayname = self._find_element("book table row displayname column", "td.col-displayname", parent=row)
        ret["bookname"] = col_displayname.text.strip()
        col_contacts = self._find_element("book table row contacts column", "td.col-contacts", parent=row)
        ret["contacts"] = int(col_contacts.text.strip())
        col_description = self._find_element("book table row description column", "td.col-description", parent=row)
        ret["description"] = col_description.text.strip()
        data = self._parse_row_info("addressbooks", row)
        ret.update(data)
        ret["token"] = ret["uri"].split("/")[-2]
        return ret

    @validate_call
    def _parse_row_info(self, name: str, row: Any) -> Dict[str, str]:
        popover = self._find_element(f"{name} table row actions popover data", "span.popover-hover", parent=row)
        data_content = popover.attrs["data-content"]
        soup = BeautifulSoup(data_content, "html.parser")
        ret = {}
        last_line = None
        for line in soup.strings:
            if last_line == "URI":
                ret["uri"] = line
            elif last_line == "User name":
                ret["username"] = line
            last_line = line
        if "uri" not in ret:
            raise BrowserInterfaceFailure(f"{name} table row info parse failed")
        return ret

    @validate_call
    def _row_action_buttons(self, name: str, row: Any) -> Dict[str, Any]:
        actions = self._find_element(f"{name} table row actions column", "td.col-actions", parent=row)
        action_buttons = self._find_elements(f"{name} table row actions buttons", "a.btn", parent=actions)
        buttons = {e.text.strip(): e for e in action_buttons if e.text}
        return buttons

    @validate_call
    def users(self, admin: Account) -> List[User]:
        self.logger.debug("request: users")
        self.login(admin)
        self._click_navbar_link("users", "Users and resources")
        rows = self._table_rows("users")
        user_list = [User(**self._parse_user_row(row)) for row in rows]
        self.logger.debug(f"users: returning {len(user_list)}")
        return user_list

    @validate_call
    def _submit_form(self, name: str, args: Dict[str, Any]):
        form = self._find_element(f"{name} form", "form")
        fields = self._find_elements(f"{name} fields", "input", parent=form)
        values = {}
        for field in fields:
            if field.attrs["type"] == "hidden":
                values[field.attrs["name"]] = field.attrs["value"]
            else:
                values[field.attrs["name"]] = None
        form_fields = [k for k in values if values[k] is None]
        for field_name, value in args.items():
            if field_name not in form_fields:
                raise AddFailed(f"field {field_name=} not present in {form_fields=}")
            values[field_name] = value
        for field_name, value in values.items():
            if value is None:
                raise AddFailed(f"no value provided for {field_name=}")
        path = self.driver.response_path()
        self.driver.post_form(path, values)

    @validate_call
    def add_user(self, admin: Account, request: AddUserRequest) -> User:
        self.logger.debug(f"request: add_user {request.username} {request.displayname} ************")
        user = User(**request.model_dump())
        Accounts().set(user.username, request.password)
        self.login(admin)
        self._click_navbar_link("add_user", "Users and resources")
        self._click_button("add user button", "body .btn", with_text="+ Add user")
        self._submit_form(
            "add user",
            {
                "data[username]": user.username,
                "data[displayname]": user.displayname,
                "data[email]": user.username,
                "data[password]": request.password,
                "data[passwordconfirm]": request.password,
            },
        )
        self._check_add_popups("user", f"User {user.username} has been created.")
        _, parsed = self._find_user_row(user.username, allow_none=False)
        added = User(**parsed)
        if added.username == request.username and added.displayname == request.displayname:
            self.logger.debug("add_user: added")
            return added
        raise AddFailed(
            f"added user mismatches request: added={repr(added.model_dump())} request={repr(request.model_dump())}"
        )

    @validate_call
    def _check_add_popups(self, name: str, expected: str):
        popups = self._check_popups()
        self._click_button(f"add {name} close button", "body form .btn", with_text="Close")
        if expected in popups:
            return
        message = f"unexpected add response: {repr(popups)}"
        self.logger.error(message)
        raise AddFailed(message)

    @validate_call
    def delete_user(self, admin: Account, request: DeleteUserRequest) -> Dict[str, str]:
        username = request.username
        self.logger.debug(f"request: delete_user {username}")
        self.login(admin)
        actions = self._find_user_actions(username)
        if not actions:
            raise DeleteFailed(f"user not found: {username=}")
        button = actions.get("Delete", None)
        if not button:
            raise BrowserInterfaceFailure("failed to locate Delete button")
        self.driver.get(button.attrs["href"])
        self._find_elements(
            "user delete confirmation button", "div.alert .btn-danger", with_text="Delete " + username, click=True
        )
        self.driver.meta_refresh()
        self.logger.debug("delete_user: deleted")
        Accounts().remove(username)
        return dict(message=f"deleted: {username}")

    @validate_call
    def _find_user_row(self, username: str, allow_none: bool | None = True) -> Tuple[Any | None, Any | None]:
        self._click_navbar_link("find_user_row", "Users and resources")
        rows = self._table_rows("users", allow_none=allow_none)
        for row in rows:
            user = self._parse_user_row(row)
            if user["username"] == username:
                return row, user
        self.logger.warning(f"user {username} not found")
        if allow_none:
            return None, None
        raise BrowserInterfaceFailure(f"failed to locate user row: {username=}")

    @validate_call
    def _find_user_actions(self, username: str, allow_none: bool | None = True) -> Dict[str, Any]:
        row, _ = self._find_user_row(username, allow_none=allow_none)
        if row:
            return self._row_action_buttons("user", row)
        return {}

    @validate_call
    def _select_user_address_books(self, username: str, allow_none: bool | None = True):
        buttons = self._find_user_actions(username, allow_none=allow_none)
        button = buttons.get("Address Books", None)
        if button:
            url = button.attrs.get("href", None)
            self.driver.get(url)
            return True
        return None

    @validate_call
    def _find_book_row(
        self, username: str, token: str, allow_none: bool | None = True
    ) -> Tuple[Any | None, Dict[str, Any] | None]:
        if not self._select_user_address_books(username, allow_none=allow_none):
            return None, None
        rows = self._table_rows("addressbooks")
        for row in rows:
            parsed = self._parse_book_row(row)
            if parsed["token"] == token:
                return row, parsed
        return None, None

    @validate_call
    def books(self, admin: Account, username: str) -> List[Book]:
        self.logger.debug(f"request: books {username}")
        self.login(admin)
        if not self._select_user_address_books(username):
            self.logger.debug("books: returning 0")
            return []
        rows = self._table_rows("addressbooks")
        ret = [Book(**self._parse_book_row(row)) for row in rows]
        self.logger.debug(f"books: returning {len(ret)}")
        return ret

    @validate_call
    def add_book(self, admin: Account, request: AddBookRequest) -> Book:
        self.logger.debug(f"request: add_book {request.username} {request.bookname} {request.description}")
        self.login(admin)
        user_row, _ = self._find_user_row(request.username)
        if user_row is None:
            raise AddFailed(f"user not found: username={request.username}")
        token = request.username + "-" + request.bookname
        token = "".join([c if c in VALID_TOKEN_CHARS else "-" for c in token])
        book = Book(token=token, **request.model_dump())

        row, _ = self._find_book_row(book.username, book.token)
        if row is not None:
            raise AddFailed(f"address book exists: username={book.username} token={book.token}")

        self._click_button("add address book button", "body .btn", with_text="+ Add address book")
        self._submit_form(
            "add book",
            {
                "data[uri]": book.token,
                "data[displayname]": book.bookname,
                "data[description]": book.description,
            },
        )
        self._check_add_popups("addressbook", f"Address Book {book.bookname} has been created.")

        # self._set_text("add book token field", 'body form input[name="data[uri]"]', book.token)
        # self._set_text("add book name field", 'body form input[name="data[displayname]"]', book.bookname)
        # self._set_text("add book description field", 'body form input[name="data[description]"]', book.description)
        # self._click_button("add book save changes button", "body form .btn", with_text="Save changes")

        _, parsed = self._find_book_row(request.username, token, allow_none=False)
        added = Book(**parsed)
        if (
            added.username == request.username
            and added.bookname == request.bookname
            and added.description == request.description
            and added.token == token
        ):
            self.logger.debug("add_book: added")
            return added
        raise AddFailed(
            f"added book mismatches request: added={repr(added.model_dump())} request={repr(request.model_dump())}"
        )

    @validate_call
    def delete_book(self, admin: Account, request: DeleteBookRequest) -> Dict[str, str]:
        self.logger.debug(f"request: delete_book {request.username} {request.token}")
        self.login(admin)
        user_row, _ = self._find_user_row(request.username)
        if user_row is None:
            raise DeleteFailed(f"user not found: username={request.username}")
        row, book = self._find_book_row(request.username, request.token)
        if not row:
            raise DeleteFailed(f"book not found: username={request.username} token={request.token}")
        actions = self._row_action_buttons("addressbook", row)
        button = actions.get("Delete", None)
        if not button:
            raise BrowserInterfaceFailure("failed to locate address book Delete button")
        self.driver.get(button.attrs["href"])
        self._find_elements(
            "book delete confirmation button",
            "div.alert .btn-danger",
            with_text="Delete " + book["bookname"],
            click=True,
        )
        self.driver.meta_refresh()
        self.logger.debug("delete_book: deleted")
        return dict(message=f"deleted: {request.token}")

    @validate_call
    def status(self, admin: Account) -> Dict[str, str]:
        self.logger.debug("request: status")

        try:
            self.login(admin)
            login = "success"
        except Exception as e:
            login = f"failed: {repr(e)}"

        state = dict(
            name="bcc",
            version=__version__,
            driver=repr(self.driver),
            url=settings.CALDAV_URL,
            uptime=self.startup_time.humanize() if self.driver else "down",
            reset=self.reset_time.humanize() if self.reset_time else "never",
            certificates=repr(self.driver.cert),
            certificate_loaded=settings.CLIENT_CERT,
            login=login,
        )
        self.logger.debug("status: returning state")
        return state
