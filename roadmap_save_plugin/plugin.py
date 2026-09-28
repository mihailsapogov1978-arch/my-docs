"""Плагин mkdocs «roadmap_save» (см. scripts/roadmap_plugin.py)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
from roadmap_plugin import RoadmapSavePlugin  # noqa: F401
