
# Aleph
--

Extract codebase information as structured data.

## Usage

```bash
aleph <codebase>
```

## File-Structure

```
bs/                 build-system files
go/                 go code-extraction rules
js/                 js & adjacent language code-extraction rules
py/                 python code-extraction rules
matches/            holds extracted codebase information, and operations to store it

config.py           class for loading configuration
config.json         my codebase configuration
file.py             operations for interacting with files and listing projects
main.py             runs code-extraction

rule_set.py         a class representing groups of code-extraction rules
rule.py             classes representing code-extraction rules and match information
comby_matcher.py    code for interacting with the code-search tool `comby`
```

## Description

Aleph extracts codebase information into a sqlite database. This information includes:

- Dependency imports
- Function & class definitions
- Function & method calls
- Comments
- Todos & comment-annotations
- Type definitions

## Supported Languages

- Python
- Go
- Js/Ts/Jsx/Tsx

## Build

Aleph uses bs (a thin shell wrapper) as a build-system

```bash
bs test
```

## License

The MIT License

Copyright (c) 2022 Róisín Grannell

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

