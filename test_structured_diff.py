"""Test script to verify structured diff path display in real assertions."""

import pytest


def test_simple_dict_diff():
    """Test diff path for simple dict comparison in real assertion."""
    expected = {"name": "Alice", "age": 30, "city": "Beijing"}
    actual = {"name": "Alice", "age": 25, "city": "Beijing"}
    assert expected == actual


def test_nested_dict_diff():
    """Test diff path for nested dict comparison in real assertion."""
    expected = {
        "user": {
            "name": "Alice",
            "profile": {
                "age": 30,
                "email": "alice@example.com"
            }
        }
    }
    actual = {
        "user": {
            "name": "Alice",
            "profile": {
                "age": 25,
                "email": "alice@example.com"
            }
        }
    }
    assert expected == actual


def test_mixed_list_dict_diff():
    """Test diff path for mixed list and dict comparison in real assertion."""
    expected = {
        "users": [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    }
    actual = {
        "users": [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 28}
        ]
    }
    assert expected == actual


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
