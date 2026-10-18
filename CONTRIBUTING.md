# Contributing

Thanks for taking an interest in Imagination Sandbox. This project collects
small, self-contained games and programs, so most contributions are additive
and do not need to touch existing code.

## Getting set up

Requires Python 3.11 or newer. No third-party runtime dependencies.

```bash
git clone https://github.com/ruhansachdeva/Imagination-Sandbox.git
cd Imagination-Sandbox
python main.py
```

## Running the tests

```bash
python -m unittest discover -s tests
```

Please make sure the suite passes before opening a pull request. CI runs the
same command on Python 3.11, 3.12 and 3.13.

## Layout

```
main.py                        convenience entry point
src/imagination_sandbox/       the package itself
tests/                         unittest suite
```

## Pull requests

- Branch off `main` and keep each pull request focused on one change.
- Add or update tests for behaviour you change.
- Write commit messages that explain *why*, not just *what*.
- If you worked with someone else, credit them with a `Co-Authored-By:`
  trailer so GitHub attributes the commit to both of you.
