# pylogger

## Description

A simple logger for Python.

## Usage

```python
import pylogger
```

### macOS

You can install `python` on macOS using homebrew with `brew install python`.

To install `direnv` on `macOS` use `brew install direnv`.  If using bash, then add `eval \"$(direnv hook bash)\"` to the `~/.bash_profile` file .  If using zsh, then add `eval \"$(direnv hook zsh)\"` to the `~/.zshrc` file.

## Development

You can setup a local development environment using the following commands.

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In order to run Python linting checks with `make flake8`, install flake8 with the following command.

```shell
pip install flake8
```

## Testing

**Python**

To run Go tests use `make test_python`, which runs unit tests.

## Contributing

We'd love to have your contributions!  Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

## Security

Please see [SECURITY.md](SECURITY.md) for more info.

## License

This project constitutes a work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105.  However, because the project utilizes code licensed from contributors and other third parties, it therefore is licensed under the MIT License.  See LICENSE file for more information.
