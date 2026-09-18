import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("handler", Path(__file__).parents[1] / "function" / "lambda_function.py")
handler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handler)

class HandlerTests(unittest.TestCase):
    def test_supported_input(self):
        self.assertEqual(handler.lambda_handler({"input": "Hello"}, None), "World")

    def test_invalid_events(self):
        for event in (None, [], {}, {"input": ""}, {"input": "Goodbye"}, {"input": 4}):
            with self.subTest(event=event), self.assertRaisesRegex(ValueError, "event.input"):
                handler.lambda_handler(event, None)

if __name__ == "__main__":
    unittest.main()
