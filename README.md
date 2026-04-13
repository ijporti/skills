# Skills

A fork of [huggingface/skills](https://huggingface.co/skills) — a collection of AI-powered skills and agents for various tasks.

## Overview

This repository contains a curated set of skills that can be used with AI assistants and agents. Skills are modular, reusable components that extend the capabilities of language models.

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

Please review our [Security Policy](.github/workflows/SECURITY.md) before reporting vulnerabilities.

## License

This project is licensed under the Apache 2.0 License — see the [LICENSE](LICENSE) file for details.
