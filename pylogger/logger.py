# =================================================================
#
# Work of the U.S. Department of Defense, Defense Digital Service.
# Released as open source under the MIT License.  See LICENSE file.
#
# =================================================================

from datetime import datetime
import json
import sys

import pytz

from pyserializer.encoder import Encoder


class Logger:

    def info(self, msg, fields=None):
        if self.level == "error":
            return
        now = datetime.now(self.timezone)
        if fields is None:
            fields = {}
        if self.encoding == "json":
            data = dict(
                list(fields.items()) +
                list({"ts": now.isoformat(), "msg": msg, "level": "info"}.items())
            )
            print(json.dumps(data, cls=Encoder), file=self.file)
        else:
            if len(fields) > 0:
                print(now.strftime("[ info ] [ %H:%M:%S ]")+" "+msg.ljust(self.width)+"    "+json.dumps(fields, cls=Encoder), file=self.file) # noqa
            else:
                print(now.strftime("[ info ] [ %H:%M:%S ]")+" "+msg.ljust(self.width), file=self.file)

    def error(self, msg, fields=None):
        now = datetime.now(self.timezone)
        if fields is None:
            fields = {}
        if self.encoding == "json":
            data = dict(
                list(fields.items()) +
                list({"ts": now.isoformat(), "msg": msg, "level": "error"}.items())
            )
            print(json.dumps(data, cls=Encoder), file=self.file)
        else:
            if len(fields) > 0:
                print(now.strftime("[ error ] [ %H:%M:%S ]")+" "+msg.ljust(self.width)+"    "+json.dumps(fields, cls=Encoder), file=self.file) # noqa
            else:
                print(now.strftime("[ error ] [ %H:%M:%S ]")+" "+msg.ljust(self.width), file=self.file)

    def __init__(self, encoding=None, file=None, level=None, timezone=None, width=None):
        self.encoding = encoding or "console"
        self.file = file or sys.stdout
        self.level = level or "info"
        self.timezone = pytz.timezone(timezone or "UTC")
        self.width = width or 60
