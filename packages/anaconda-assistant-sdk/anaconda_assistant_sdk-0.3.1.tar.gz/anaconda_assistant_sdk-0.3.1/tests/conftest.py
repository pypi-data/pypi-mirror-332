from pathlib import Path
from typing import Any

import pytest
from pytest import MonkeyPatch


@pytest.fixture()
def tmp_cwd(monkeypatch: MonkeyPatch, tmp_path: Path) -> Path:
    """Create & return a temporary directory after setting current working directory to it."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture(scope="session")
def is_not_none() -> Any:
    """
    An object that can be used to test whether another is None.

    This is particularly useful when testing contents of collections, e.g.:

    ```python
    def test_data(data, is_not_none):
        assert data == {"some_key": is_not_none, "some_other_key": 5}
    ```

    """

    class _NotNone:
        def __eq__(self, other: Any) -> bool:
            return other is not None

    return _NotNone()


@pytest.fixture(autouse=True)
def fake_config_toml(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    toml_path = tmp_path / "config.toml"
    monkeypatch.setenv("ANACONDA_CONFIG_TOML", str(toml_path))

    monkeypatch.delenv("ANACONDA_ASSISTANT_ACCEPTED_TERMS", raising=False)
    monkeypatch.delenv("ANACONDA_ASSISTANT_DATA_COLLECTION", raising=False)
