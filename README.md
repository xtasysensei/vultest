<h1 align="center"> 🕷Vultest 🕷</h1>

 <h2 align="center"> Automatic Web Vulnerability Scanner</h2>

Vultest is a terminal-based web vulnerability scanner written in **Python**.
It is a script that crawls and tests a given URL against well-known vulnerabilities.
## Screenshots

![vultest-prompt](screenshots/vul.jpeg)

## Main Features

- Reflected XSS scanning
- Blind XSS find
- SQL injection scanning
- Crawling all links on a website
- POST and GET forms are supported

## OS support

- Linux
- Windows
- MacOS

## Tools

- Python
- [Python Poetry](https://realpython.com/dependency-management-python-poetry/)
- Shell environment
- Git

## Getting started

You must have python installed in the OS of choice.
Then run:
```bash
$ git clone https://github.com/xtasysensei/vultest.git
$ cd vultest

# installing project dependencies found in pyproject.toml
$ poetry install
```
### Python environment

[Python Poetry](https://realpython.com/dependency-management-python-poetry/) will handle the activation and creation of the virtual environment.

## Usage
Run:
```bash
# activating virtual environment
$ poetry shell

# running the application
$ poetry run python vultest.py
```

Follow the prompt that comes up.
