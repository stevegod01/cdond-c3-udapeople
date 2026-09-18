import io
import unittest
from unittest.mock import Mock

from scripts.smoke_test import check


class Response(io.BytesIO):
    def __init__(self, body, status=200):
        super().__init__(body.encode())
        self.status = status


class SmokeTests(unittest.TestCase):
    def test_backend_requires_explicit_ok(self):
        check("http://unused", "backend", opener=Mock(return_value=Response('{"status":"ok"}')))
        with self.assertRaises(RuntimeError):
            check("http://unused", "backend", attempts=1,
                  opener=Mock(return_value=Response('{"status":"error"}')))

    def test_frontend_checks_actual_root_not_unrelated_welcome_text(self):
        check("http://unused", "frontend",
              opener=Mock(return_value=Response('<html><div id="root"></div></html>')))
        with self.assertRaises(RuntimeError):
            check("http://unused", "frontend", attempts=1,
                  opener=Mock(return_value=Response("Welcome to an unrelated website")))

    def test_failure_http_status_is_not_success(self):
        with self.assertRaises(RuntimeError):
            check("http://unused", "backend", attempts=1,
                  opener=Mock(return_value=Response('{"status":"ok"}', 503)))

    def test_transient_failure_retries_then_succeeds(self):
        sleep = Mock()
        opener = Mock(side_effect=[OSError("starting"), Response('{"status":"ok"}')])
        check("http://unused", "backend", attempts=2, opener=opener, sleep=sleep)
        self.assertEqual(opener.call_count, 2)
        sleep.assert_called_once_with(5)

    def test_retry_budget_is_bounded(self):
        sleep = Mock()
        opener = Mock(side_effect=OSError("down"))
        with self.assertRaises(RuntimeError):
            check("http://unused", "backend", attempts=3, opener=opener, sleep=sleep)
        self.assertEqual(opener.call_count, 3)
        self.assertEqual(sleep.call_count, 2)
