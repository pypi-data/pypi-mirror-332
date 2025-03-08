import json
from pathlib import Path

from . import settings


class Accounts:
    def __init__(self, filename=None):
        if not filename:
            filename = settings.PASSWD_FILE
        self.path = Path(filename)
        if not self.path.is_file():
            self.write(dict())
            mode = int(settings.PASSWD_MODE, 8)
            self.path.chmod(mode)

    def read(self):
        return json.loads(self.path.read_text())

    def write(self, values):
        with self.path.open("w+") as fp:
            fp.write(json.dumps(values, indent=2) + "\n")
        return self.read()

    def get(self, username):
        values = self.read()
        return values[username]

    def set(self, username, password):
        values = self.read()
        values[username] = password
        self.write(values)

    def remove(self, username):
        values = self.read()
        if username in values:
            del values[username]
        self.write(values)
