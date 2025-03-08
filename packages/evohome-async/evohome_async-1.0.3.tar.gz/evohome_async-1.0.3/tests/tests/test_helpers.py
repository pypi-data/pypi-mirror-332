"""Tests for evohome-async - validate the schedule schemas."""

from __future__ import annotations

from evohome.helpers import obscure_secrets


def test_helper_obscure_secrets() -> None:
    """Test the obscure_secrets helper."""

    assert obscure_secrets(None) is None

    for _ in ((), [], {}):
        assert obscure_secrets(_) == _

    for _ in (False, True, 0, 1, "", "a"):
        assert obscure_secrets(_) == _

    for _ in (
        {"a": 1, "b": 2},
        [{"a:": 1}, {"b": 2}],
    ):
        assert obscure_secrets(_) == _

    for _ in (
        {"name": 1, "b": 2},
        [{"name:": 1}, {"b": 2}],
    ):
        pass
