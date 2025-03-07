# terminal-help-app

Provides command-line tool `help` to write terminal commands for you using natural language powered by ChatGPT.

You must provide an OpenAI API token via the environment variables `TERMINAL_HELP_OPENAI_API_KEY` or `OPENAI_API_KEY`.  You can create an OpenAI key here: https://platform.openai.com/api-keys

## Example

Here's an example interaction:

```shell
[~] help
[question] list files modified the past day (not recursive)
[chatgpt] use "find" with the right flags.
[code] find . -maxdepth 1 -type f -mtime -1
./.DS_Store
./.localrc
./.zsh_history
./.zcompdump
./Brewfile
./.viminfo
```

## Installation using `uv`

You can install **terminal-help-app** using `uv` by adding an alias in your shell configuration (`~/.bashrc`, `~/.zshrc`, etc.):

```shell
alias help="uvx --from=terminal-help-app help"
# You can alias `help` to whatever you would like
```

### Install `uv`

If you don't have `uv` installed, here's a quick setup:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

You can read more about installing `uv` here:<br />
https://docs.astral.sh/uv/getting-started/installation/

### Alternative install with `pipx`

Alternatively you can install using `pipx` by doing:

```shell
pipx install terminal-help-app
```

This will add command-line utility `help`.

You can learn more about install `pipx` here:<br />
https://pipx.pypa.io/stable/installation/

## Environment Variables

### `TERMINAL_HELP_OPENAI_API_KEY` or `OPENAI_API_KEY`

Set your OpenAI key in your shell configuration (`~/.bashrc`, `~/.zshrc`, etc.):

```shell
export OPENAI_API_KEY="your-key-here"

# Optionally specifically the OpenAI Key for this tool only
export TERMINAL_HELP_OPENAI_API_KEY="your-key-here"
```

You can create an OpenAI key here: https://platform.openai.com/api-keys

### `TERMINAL_HELP_MODEL`

Specify the model you would like to use; the default is [`gpt-4o-mini`](https://platform.openai.com/docs/models/gpt-4o-mini).

## `TERMINAL_HELP_CONFIG_PATH`

You can override the config directory using the environment variable:

```bash
export TERMINAL_HELP_CONFIG_PATH="/path/to/your/config"
# Default is ~/.config/terminal_help
```

### History & Prompt Cache Paths

Configuration and history files are stored by default in:

- **Config Directory:** `~/.config/terminal_help`
- **Prompt Cache:** `~/.config/terminal_help/db.sqlite3`
- **Question History:** `~/.config/terminal_help/question_history`
- **Shell History:** `~/.config/terminal_help/code_history`

## License

[MIT](https://opensource.org/license/mit)