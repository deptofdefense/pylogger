# =================================================================
#
# Work of the U.S. Department of Defense, Defense Digital Service.
# Released as open source under the MIT License.  See LICENSE file.
#
# =================================================================

import io
import json
import unittest

from pylogger.logger import Logger


class TestLogger(unittest.TestCase):

    def test_info_default(self):
        buf = io.StringIO()
        logger = Logger(file=buf)
        logger.info("hello world")
        line = buf.getvalue().strip()
        self.assertTrue(
            line.startswith("[ info ]"),
            'error logging message as default encoding'
        )

    def test_info_console(self):
        buf = io.StringIO()
        logger = Logger(file=buf)
        logger.info("hello world")
        line = buf.getvalue().strip()
        self.assertTrue(
            line.startswith("[ info ]"),
            'error logging message as default encoding'
        )

    def test_info_json(self):
        buf = io.StringIO()
        logger = Logger(encoding="json", file=buf)
        logger.info("hello world")
        line = buf.getvalue().strip()
        data = json.loads(line)
        self.assertSetEqual(
            set(data.keys()),
            set(["ts", "msg", "level"]),
            'error logging message as json encoding'
        )
        self.assertDictEqual(
            {k: v for k, v in data.items() if k != "ts"},
            {"msg": "hello world", "level": "info"},
            'error logging message as json encoding'
        )

    def test_info_json_fields(self):
        buf = io.StringIO()
        logger = Logger(encoding="json", file=buf)
        logger.info("hello world", {"foo": "bar"})
        line = buf.getvalue().strip()
        data = json.loads(line)
        self.assertSetEqual(
            set(data.keys()),
            set(["ts", "msg", "foo", "level"]),
            'error logging message as json encoding'
        )
        self.assertDictEqual(
            {k: v for k, v in data.items() if k != "ts"},
            {"msg": "hello world", "level": "info", "foo": "bar"},
            'error logging message as json encoding'
        )

    def test_info_json_exception(self):
        buf = io.StringIO()
        logger = Logger(encoding="json", file=buf)
        logger.error(Exception("hello world"), {"foo": "bar"})
        line = buf.getvalue().strip()
        data = json.loads(line)
        self.assertSetEqual(
            set(data.keys()),
            set(["ts", "msg", "foo", "level"]),
            'error logging message as json encoding'
        )
        self.assertDictEqual(
            {k: v for k, v in data.items() if k != "ts"},
            {"msg": "hello world", "level": "error", "foo": "bar"},
            'error logging message as json encoding'
        )
