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

The session below is transcribed from a real interactive run, with `Hello World Foo` typed
at the first prompt:

```
$ python3 acronymMaker.py
Enter what you want to make into an acronym: Hello World Foo
Your new acronym is HWF
Press 'Enter' to exit the program.
```

## License

This project is licensed under the Stephenson Software Non-Commercial License
(Stephenson-NC). See [LICENSE](LICENSE) for the full text.
