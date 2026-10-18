# Acronym Maker

Transforms your input into an acronym. The first character of each word is taken, in order, and
the result is printed. Words are separated by any run of whitespace (spaces or tabs); leading
and trailing whitespace is ignored.

![A real Acronym Maker session turning "Portable Network Graphics" into "PNG"](docs/images/acronym-maker.gif)

*A real session: `Portable Network Graphics` becomes `PNG`.*

Case is preserved: each initial keeps whatever case it had in the input, so `hello World foo`
becomes `hWf`, not `HWF`.

## Requirements

Python 3. No third-party packages are used — only the standard library.

## Usage

Run the script from the repository root:

```
python3 acronymMaker.py
```

The program prompts for a phrase, prints the acronym, then waits for one more `Enter`
before exiting. If standard input ends first (for example, when the phrase is piped in), the
program exits normally without waiting. If standard input ends before any phrase is entered, the
program exits normally without printing an acronym.

## Example

The session below is transcribed from a real interactive run, with `Hello World Foo` typed
at the first prompt:

```
$ python3 acronymMaker.py
Enter what you want to make into an acronym: Hello World Foo
Your new acronym is HWF
Press 'Enter' to exit the program.
```

## Tests

The test suite uses the standard library's `unittest`. Run it from the repository root:

```
python3 -m unittest discover -s tests -t . -v
```

## How the screenshot was captured

`docs/images/acronym-maker.gif` was recorded on 2026-10-18 from a real run of `python3 acronymMaker.py` (Python 3.12) with `Portable Network Graphics` typed at the prompt. The program was started in a pseudo-terminal, the input shown was typed into it by a script, and the recorded terminal output was rendered to an image with [pyte](https://github.com/selectel/pyte) and [Pillow](https://python-pillow.org/). Nothing in the output was edited; only the window frame was added.

## License

This project is licensed under the Stephenson Software Non-Commercial License
(Stephenson-NC). See [LICENSE](LICENSE) for the full text.
