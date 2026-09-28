"""Обёртка для запуска mkdocs serve с плагином roadmap_save из scripts/."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from mkdocs.__main__ import cli
if __name__ == '__main__':
    cli()
