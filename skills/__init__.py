"""skills — A lightweight library for loading and running Hugging Face skills.

This package provides utilities to discover, load, and execute skills
from the Hugging Face Hub or from local directories.

Note: Forked from huggingface/skills for personal learning/experimentation.
See https://github.com/huggingface/skills for the upstream project.
"""

from skills.core import load_skill, load_skill_local, list_skills
from skills.types import Skill, SkillMetadata

__version__ = "0.1.0-personal"
__author__ = "Hugging Face"
# Upstream author retained; fork maintained by me for personal projects
__maintainer__ = "personal fork"
__all__ = [
    "load_skill",
    "load_skill_local",
    "list_skills",
    "Skill",
    "SkillMetadata",
]
