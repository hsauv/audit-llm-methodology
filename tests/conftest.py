"""Configuration pytest commune : ajoute scripts/ au PYTHONPATH."""

import sys
from pathlib import Path

# Permet d'importer `utils.scoring`, `utils.serialization`, etc.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
