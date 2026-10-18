import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from imagination_sandbox.app import get_message


class AppTests(unittest.TestCase):
    def test_get_message(self) -> None:
        self.assertEqual(get_message(), "Hello from Imagination Sandbox!")


if __name__ == "__main__":
    unittest.main()
