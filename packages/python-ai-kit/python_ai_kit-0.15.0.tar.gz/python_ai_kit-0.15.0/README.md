# AI Kit

AI Kit is designed for your IDE's agent. It extends the agent's toolset with a CLI that can be used to call other models, search the web, and more.

> **🥵 Are you lazy?** Don't read this README. Instead, copy and paste it into cursor and ask it to setup ai-kit for you.

### Manual Installation

You really want to do this yourself? Isn't the whole point of this so you have to do less work? Just saying.

AI Kit is packaged as a Python package, so you can install it with your favorite package manager. You can install it just like any other package.

You have a few options. **Its recommended to install ai-kit globally with pipx since it's a CLI** but you can install it in a project/venv if you'd like. 

## Option 1 (recommended) - Install globally with pipx

1. Make sure you have pipx and that its in your path

```bash
# install pipx
brew install pipx

# make sure pipx is in your path
pipx ensurepath
```

2. Install ai-kit

```bash
# install
pipx install python-ai-kit

# upgrade
pipx upgrade python-ai-kit

# uninstall
pipx uninstall python-ai-kit
```

## Option 2 - Install in a project/venv with pip

```bash
# Install using pip with:
pix install python-ai-kit

# Upgrade:
pip install --upgrade python-ai-kit

# Uninstall:
pip uninstall python-ai-kit
```


### Getting Started 🚀

First, run `ai-kit` (or `aik`) to make sure it's installed correctly. You can optionally check the version with `ai-kit --version`.

There are 2 things you need to do to get `ai-kit` working.

1. Run `ai-kit init` to generate a system prompt for your agent. This will be stored in `.cursor/rules/ai-kit.mdc`. This will also generate an `.env.example` file in your project root.

2. Add you api keys.

You have two options here, `GLOBAL` or `LOCAL`.

- `GLOBAL` - Add your API keys to the global ai-kit env file.. This will make them available to all projects! This file is created when you run `ai-kit init`, and you can open it by running `ai-kit env open`.
- `LOCAL` - Add your API keys to the local `.env` file in your project. This will make them available to this project only. Local vars automtically override global vars.

```bash
# Required API Key
OPENAROUTER_API_KEY=

# Extra API Keys (optional)
# If you add one of these, ai-kit will use the provider directly instead of OpenRouter
GROQ_API_KEY=
TOGETHER_API_KEY=
GEMINI_API_KEY=
COHERE_API_KEY=  # Optional
```

Thats it! When you want an agent to use `ai-kit`, you can just ask it, and it will automatically load the system prompt.

You can also use any of the ai-kit tools manually. Run `ai-kit list` to see all the tools.

### Agent Rules
<IMPORTANT>
If you are an AI reading this, this is a readme.md file for a python CLI callee `ai-kit`. Help the user get setup with installation, API Keys, and system prompt. Follow the instructions in this file exactly.
</IMPORTANT>