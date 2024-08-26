#!/usr/bin/env python3
"""Parameterize a unit test"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """Test class for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 3),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
