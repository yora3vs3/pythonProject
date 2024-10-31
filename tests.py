import unittest
import warnings
import logging

# Sample function to demonstrate exceptions, warnings, and logging
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def deprecated_function():
    warnings.warn("This function is deprecated", DeprecationWarning)

def log_message(logger):
    logger.error("An error has occurred")

class TestAssertions(unittest.TestCase):

    def test_assertRaises(self):
        """Test that divide raises ValueError when dividing by zero."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_assertRaisesRegex(self):
        """Test that divide raises ValueError with correct message when dividing by zero."""
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_assertWarns(self):
        """Test that deprecated_function raises a DeprecationWarning."""
        with self.assertWarns(DeprecationWarning):
            deprecated_function()

    def test_assertWarnsRegex(self):
        """Test that deprecated_function raises DeprecationWarning with correct message."""
        with self.assertWarnsRegex(DeprecationWarning, "deprecated"):
            deprecated_function()

    def test_assertLogs(self):
        """Test that log_message logs an error message with minimum level ERROR."""
        logger = logging.getLogger("test_logger")
        with self.assertLogs(logger, level='ERROR') as log:
            log_message(logger)
        self.assertIn("An error has occurred", log.output[0])

    def test_assertNoLogs(self):
        """Test that no logs are produced with minimum level WARNING."""
        logger = logging.getLogger("test_logger")
        with self.assertLogs(logger, level='WARNING') as log:
            pass  # Nothing is logged, so this should capture no entries
        self.assertEqual(len(log.output), 0, "Expected no logs but found some")


if __name__ == '__main__':
    unittest.main(verbosity=2)
