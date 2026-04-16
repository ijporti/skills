"""Skill loader utilities for fetching and loading skills from the Hub or locally."""

import os
import importlib.util
import sys
from pathlib import Path
from typing import Callable, Optional, Union


def load_skill_local(skill_path: Union[str, Path]) -> Callable:
    """Load a skill from a local file path.

    Args:
        skill_path: Path to the Python file containing the skill function.

    Returns:
        The skill callable loaded from the file.

    Raises:
        FileNotFoundError: If the skill file does not exist.
        AttributeError: If the file does not define a `skill` function.

    Example:
        >>> skill = load_skill_local("my_skills/summarize.py")
        >>> result = skill("Some long text to summarize...")
    """
    skill_path = Path(skill_path)
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill file not found: {skill_path}")

    module_name = skill_path.stem
    spec = importlib.util.spec_from_file_location(module_name, skill_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for skill at {skill_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    if not hasattr(module, "skill"):
        raise AttributeError(
            f"Skill file '{skill_path}' must define a top-level `skill` function."
        )

    return module.skill


def load_skill(
    repo_id: str,
    filename: str = "skill.py",
    token: Optional[str] = None,
    cache_dir: Optional[Union[str, Path]] = None,
    repo_type: str = "model",
) -> Callable:
    """Load a skill from the Hugging Face Hub.

    Args:
        repo_id: The repository ID on the Hub (e.g. ``"username/my-skill"``).
        filename: The filename within the repo containing the skill. Defaults to ``"skill.py"``.
        token: Optional Hugging Face API token for private repos.
        cache_dir: Optional directory to cache downloaded skill files.
        repo_type: The type of Hub repository. Defaults to ``"model"`` (upstream used
            ``"space"`` but most skill repos are plain model repos).

    Returns:
        The skill callable loaded from the Hub.

    Raises:
        ImportError: If ``huggingface_hub`` is not installed.
        FileNotFoundError: If the skill file cannot be found in the repo.

    Example:
        >>> skill = load_skill("huggingface/summarize-skill")
        >>> result = skill("Some long text to summarize...")
    """
    try:
        from huggingface_hub import hf_hub_download
    except ImportError as e:
        raise ImportError(
            "The `huggingface_hub` package is required to load skills from the Hub. "
            "Install it with: pip install huggingface_hub"
        ) from e

    local_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        token=token or os.environ.get("HF_TOKEN"),
        cache_dir=cache_dir,
        repo_type=repo_type,
    )

    return load_skill_local(local_path)
