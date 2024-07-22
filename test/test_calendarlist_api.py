import unittest

from infra.logger import Logger
from logic.calendarlist_api import CalendarListAPI
from test.object_generator import get_actual_calendar_summaries


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        # Initialize logger and CalendarListAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("Setting up the test case environment")
        try:
            self.api = CalendarListAPI()
            self.service = self.api.service
        except Exception as e:
            self.logger.error(f"Error during setup: {e}")
            self.fail(f"Setup failed with exception: {e}")

    def tearDown(self):
        # Reset the CalendarListAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("Tearing down the test case environment")
        self.api = None

    def test_get_calendar_list_api(self):
        # Verify the calendar list attributes and summaries
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            c_list = self.api.get_calendar_list()
            self.assertEqual(c_list['kind'], self.api.config["object_kind"]["calendarList"])
            actual_summaries = get_actual_calendar_summaries()
            calendar_summaries = {item['summary'] for item in c_list['items']}
            for summary in actual_summaries:
                self.assertIn(summary, calendar_summaries)
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Get calendar list API test failed with exception: {e}")

    def test_calendar_in_calendar_list(self):
        # Verify the presence of the test calendar ID
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            calendar_id = self.api.config["test_calendar_id"]
            self.assertTrue(self.api.check_if_calendar_in_calendar_list(calendar_id))
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Calendar in calendar list test failed with exception: {e}")
