# ASCII character print

It's sometimes useful to have a command-line ASCII table or character.

This Python script provides just that.  It can be used to display ranges of characters or single characters.

Valid arguments are decimal and hexadecimal ASCII and UNICODE values.

## Examples:

Display characters from 32 to 255 (default):
```bash
./asc.py
```

Display a range of characters:
```bash
./asc.py 224 255
```

Display a single ASCII character:
```bash
./asc.py 65
```

Display a UNICODE character:
```bash
./asc.py 0x2623
```

You can mix-and-match decimal and hexadecimal:
```bash
./asc.py 9728 0x262f
```
