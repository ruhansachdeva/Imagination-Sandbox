import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from imagination_sandbox.__main__ import main
from imagination_sandbox.app import get_message


class GetMessageTests(unittest.TestCase):
    def test_default_recipient(self) -> None:
        self.assertEqual(get_message(), "Hello from Imagination Sandbox!")

    def test_custom_recipient(self) -> None:
        self.assertEqual(get_message("Ruhan"), "Hello from Ruhan!")


class CliTests(unittest.TestCase):
    def run_cli(self, argv: list[str]) -> str:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(argv)
        self.assertEqual(exit_code, 0)
        return buffer.getvalue().strip()

    def test_cli_default(self) -> None:
        self.assertEqual(self.run_cli([]), "Hello from Imagination Sandbox!")

    def test_cli_name_option(self) -> None:
        self.assertEqual(self.run_cli(["--name", "Iknoor"]), "Hello from Iknoor!")


if __name__ == "__main__":
    unittest.main()
