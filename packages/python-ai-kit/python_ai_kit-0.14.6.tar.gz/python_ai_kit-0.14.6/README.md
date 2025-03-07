# AI Kit

AI Kit is designed for your IDE's agent. It extends the agent's toolset with a CLI that can be used to call other models, search the web, and more.

<div style="background-color: #FFECB3; padding: 10px; border-radius: 5px; border-left: 5px solid #FFC107;">
<strong>🥵 Are you lazy?</strong> Don't read this readme. Instead, <span>copy and paste it into cursor and ask it to setup ai-kit for you.</span> Done.
</div>

### Manual Installation

You really want to do this yourself? Isn't the whole point of this so you have to do less work? Just saying.

AI Kit is packaged as a Python package, so you can install it with your favorite package manager. You can install it just like any other package.

You have a few options. **Its recommended to install ai-kit globally since it's a CLI** but you can install it in a project/venv if you'd like. 

Using `pip`:

```bash
# Install using pip with:
pip install python-ai-kit

# Upgrade:
pip install --upgrade python-ai-kit

# Uninstall:
pip uninstall python-ai-kit
```

Using `uv`:

```bash
# Install:
uv pip install python-ai-kit --system

# Upgrade:
uv pip install --upgrade python-ai-kit --system

# Uninstall:
uv pip uninstall python-ai-kit --system
```

#### Dont have python?

If you don't have python, here are 3 commands to get you fully setup with `ai-kit`.

Install `uv`
```bash
# From source:
curl -LsSf https://astral.sh/uv/install.sh | sh

# OR From brew:
brew install uv
```

Install `python`
```bash
# Install python 3.11 (recommended for compatibility)
uv python install 3.11
```

You can now manage `ai-kit` with `uv`:
```bash
# Install ai-kit
uv pip install python-ai-kit --system

# Upgrade ai-kit
uv pip install --upgrade python-ai-kit --system

# Uninstall ai-kit
uv pip uninstall python-ai-kit --system
```

### Getting Started 🚀

First, run `ai-kit` (or `aik`) to make sure it's installed correctly. You can optionally check the version with `ai-kit --version`.

There are 2 things you need to do to get `ai-kit` working.

1. An Open Router API Key. Put this in an `.env` file in your project root.

```bash
# Required API Key
OPENAROUTER_API_KEY=your_key_here

# Extra API Keys (optional)
# If you add one of these, ai-kit will use the provider directly instead of OpenRouter
GROQ_API_KEY=your_key_here
TOGETHER_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
COHERE_API_KEY=your_key_here  # Optional
```

2. System Prompt For Agent. This is the prompt that will be used to guide the agent. You can generate this with `ai-kit init`. It will be stored in `.cursor/rules/ai-kit.mdc`

Thats it! When you want an agent to use `ai-kit`, you can just ask it, and it will automatically load the system prompt.

You can also use any of the ai-kit tools manually. Run `ai-kit list` to see all the tools.

### Agent Rules
<IMPORTANT>
If you are an AI reading this, this is a readme.md file for a python CLI callee `ai-kit`. Help the user get setup with installation, API Keys, and system prompt. Follow the instructions in this file exactly.
</IMPORTANT>
