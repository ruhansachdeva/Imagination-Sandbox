from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from imagination_sandbox.app import get_message


def main() -> None:
    print(get_message())


if __name__ == "__main__":
    main()
