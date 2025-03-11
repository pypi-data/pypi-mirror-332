import unittest
from unittest.mock import patch
from flood_monitoring.monitor import FloodMonitor

class TestFloodMonitor(unittest.TestCase):
    """
    A class for testing the FloodMonitor class. 
    Given the scope of this project, I've included only one test case to illustrate how testing could work for larger projects.
    """

    @patch('requests.get')
    def test_perform_monitoring_api_error(self, mock_get):
        """
        This function tests whether the perform_monitoring function raises the correct ValueError when the API returns a specific error.
        """
        # simulate an API error with 500 status code (server error)
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = {
            'error': 'Internal Server Error'
        }

        # create an instance of the FloodMonitor class
        monitor = FloodMonitor(parameterName='Water Level', town='Manchester')

        # run the monitor function and check if it raises a ValueError
        with self.assertRaises(ValueError) as context:
            monitor.perform_monitoring(monitor.station_parameters)

        # see if the error message is correct, expect assertion error if not
        self.assertEqual(str(context.exception), 'Error: 500')


if __name__ == '__main__':
    unittest.main()