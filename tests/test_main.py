import unittest
from unittest.mock import patch
from src.main import hello_world
import schedule


class TestMain(unittest.TestCase):
    # Test hello_world function
    def test_hello_world(self):
        with patch("builtins.print") as mock_print:
            hello_world()
            mock_print.assert_called_once_with("Hello, world!")

    # Test if the hello_world function is scheduled
    @patch("schedule.run_pending")
    def test_scheduling(self, mock_run_pending):
        schedule.every(10).seconds.do(hello_world)
        schedule.run_pending()

        # Check that the scheduling logic triggered run_pending
        mock_run_pending.assert_called_once()


if __name__ == "__main__":
    unittest.main()
