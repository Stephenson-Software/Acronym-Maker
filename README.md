# Acronym Maker

Transforms your input into an acronym. The first character of each space-separated word is
taken, in order, and the result is printed.

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
before exiting.

## Example

The session below is the output of a real run with the input piped in:

```
$ printf 'Hello World Foo\n\n' | python3 acronymMaker.py
Enter what you want to make into an acronym: Your new acronym is HWF
Press 'Enter' to exit the program.
```

When the program is run interactively instead, the typed phrase is echoed by the terminal
after the prompt, and the acronym is printed on the following line.

## License

This project is licensed under the Stephenson Software Non-Commercial License
(Stephenson-NC). See [LICENSE](LICENSE) for the full text.
