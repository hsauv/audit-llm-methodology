"""Smoke tests pour scripts/utils/serialization.py."""

from pathlib import Path

import numpy as np
import yaml

from utils.serialization import safe_yaml_dump


def test_safe_yaml_dump_handles_numpy_scalars(tmp_path: Path):
    data = {
        "int64": np.int64(42),
        "float64": np.float64(3.14),
        "bool": np.bool_(True),
    }
    out = tmp_path / "scalars.yaml"
    safe_yaml_dump(data, out)
    loaded = yaml.safe_load(out.read_text())
    assert loaded == {"int64": 42, "float64": 3.14, "bool": True}
    assert isinstance(loaded["int64"], int)
    assert isinstance(loaded["float64"], float)
    assert isinstance(loaded["bool"], bool)


def test_safe_yaml_dump_handles_numpy_arrays(tmp_path: Path):
    data = {"arr": np.array([1, 2, 3]), "mat": np.array([[1.0, 2.0]])}
    out = tmp_path / "arrays.yaml"
    safe_yaml_dump(data, out)
    loaded = yaml.safe_load(out.read_text())
    assert loaded["arr"] == [1, 2, 3]
    assert loaded["mat"] == [[1.0, 2.0]]


def test_safe_yaml_dump_handles_nested_structures(tmp_path: Path):
    data = {
        "results": {
            "grade": "A",
            "scores": [np.float64(85.5), np.float64(72.1)],
            "details": {"n": np.int64(100)},
        }
    }
    out = tmp_path / "nested.yaml"
    safe_yaml_dump(data, out)
    loaded = yaml.safe_load(out.read_text())
    assert loaded["results"]["grade"] == "A"
    assert loaded["results"]["scores"] == [85.5, 72.1]
    assert loaded["results"]["details"]["n"] == 100


def test_safe_yaml_dump_preserves_unicode(tmp_path: Path):
    data = {"prenom": "Aïcha", "ville": "Montréal"}
    out = tmp_path / "unicode.yaml"
    safe_yaml_dump(data, out)
    # Ne doit pas être encodé en \uXXXX
    content = out.read_text(encoding="utf-8")
    assert "Aïcha" in content
    assert "Montréal" in content
