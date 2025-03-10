from __future__ import annotations

from test_uv_tooling import __version__


def test_main() -> None:
    assert isinstance(__version__, str)
