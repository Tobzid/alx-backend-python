#!/usr/bin/env python3
"""
Unit tests for utils.memoize
"""
import unittest
from unittest.mock import patch
from utils import memoize
from unittest.mock import patch, Mock


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class
    """

    def test_memoize(self):
        """
        Test the memoize decorator
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method') as mock_a_method:
            # Set the return value of the mock
            mock_a_method.return_value = Mock(return_value=42)

            result_1 = test_instance.a_property()
            result_2 = test_instance.a_property()

        mock_a_method.assert_called_once()
        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)
