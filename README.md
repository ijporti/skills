# Skills

A fork of [huggingface/skills](https://huggingface.co/skills) — a collection of AI-powered skills and agents for various tasks.

## Overview

This repository contains a curated set of skills that can be used with AI assistants and agents. Skills are modular, reusable components that extend the capabilities of language models.

> **Personal fork note:** I'm using this primarily to experiment with custom tool-use skills for local LLM setups. PRs here are for my own learning — please contribute upstream to [huggingface/skills](https://github.com/huggingface/skills) instead.

## Structure

```
├── .claude-plugin/          # Claude AI plugin configuration
│   ├── marketplace.json     # Marketplace listing metadata
│   └── plugin.json          # Plugin configuration
├── .cursor-plugin/          # Cursor IDE plugin configuration
│   ├── marketplace.json     # Marketplace listing metadata
│   └── plugin.json          # Plugin configuration
└── .github/
    └── workflows/
        ├── generate-agents.yml          # CI: Generate agent definitions
        ├── push-evals-leaderboard.yml   # CI: Push evaluation results
        └── push-hackers-leaderboard.yml # CI: Push hacker leaderboard
```

## Getting Started

### Prerequisites

- Python 3.9+
- [Hugging Face account](https://huggingface.co/join)
- `huggingface_hub` CLI

### Installation

```bash
pip install huggingface_hub
huggingface-cli login
```

### Using Skills

Skills can be loaded directly from the Hugging Face Hub:

```python
from huggingface_hub import hf_hub_download

# Download a specific skill
skill_path = hf_hub_download(
    repo_id="huggingface/skills",
    filename="skill_name.py",
    repo_type="dataset"
)
```

### Using Skills Locally (Personal Setup)

For local LLM experimentation, I find it useful to clone the dataset repo directly:

```bash
# Clone the skills dataset locally for offline use
git clone https://huggingface.co/datasets/huggingface/skills skills-local
```

You can also load a skill directly from a local path without hitting the Hub:

```python
import importlib.util

def load_skill_local(skill_path: str):
    """Load a skill module from a local file path (useful for offline/dev work)."""
    spec = importlib.util.spec_from_file_location("skill", skill_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
```

## Contributing

1. Fork this repository
2. Create a new branch: `git checkout -b feat/my-new-skill`
3. Add your skill following the [skill template](./SKILL_TEMPLATE.md)
4. Submit a pull request

### Skill Requirements

- Each skill must have a clear, single responsibility
- Include docstrings and type hints
- Add evaluation metrics where applicable
- Follow the existing naming conventions

## Leaderboards

- **Evals Leaderboard**: Tracks skill performance across standardized benchmarks
- **Hackers Leaderboard**: Tracks community contributions and skill submissions

Leaderboards are automatically updated via GitHub Actions on each push to `main`.

## Security

> **Note:** The security policy path in the original repo appears to be incorrect — `SECURITY.md` is typically at the repo root or `.github/SECURITY.md`, not inside `workflows/`. Keeping the link as-is for now until confirmed.

Please review our [Security Policy](.github/SECURITY.md) before reporting vulnerabilities.

## License

This project is licensed u