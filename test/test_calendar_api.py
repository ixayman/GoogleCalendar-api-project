import unittest

from infra.utils import generate_random_string
from infra.logger import Logger
from logic.calendars_api import CalendarsAPI
from test.object_generator import example_calendar_object


class TestColorsAPI(unittest.TestCase):
    new_calendar = example_calendar_object()

    def setUp(self):
        # Initialize logger and CalendarsAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("-" * 26)
        self.logger.info("Setting up the test case environment")
        try:
            self.calendarsAPI = CalendarsAPI()
            self.config = self.calendarsAPI.config
            self.service = self.calendarsAPI
            self.created_calendar = self.service.insert_calendar(self.new_calendar)
            self.logger.info(f"Inserted new calendar with ID: {self.created_calendar['id']}")
        except Exception as e:
            self.logger.error(f"Error during setup: {e}")
            self.fail(f"Setup failed with exception: {e}")

    def tearDown(self):
        # Delete the created calendar and reset the CalendarsAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("Tearing down the test case environment")
        try:
            self.service.delete_calendar(self.created_calendar["id"])
            self.logger.info(f"Deleted calendar with ID: {self.created_calendar['id']}")
        except Exception as e:
            self.logger.info(f"exception incase of calendar deletion test, no second deletion needed")
            pass
        self.calendarsAPI = None
        self.logger.info("-" * 26)

    def test_insert_new_calendar(self):
        # Verify the created calendar's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        # assert
        try:
            self.assertEqual(self.created_calendar['kind'], self.config["object_kind"]["calendar"])
            self.assertEqual(self.created_calendar['summary'], self.new_calendar['summary'])
            self.assertEqual(self.created_calendar['location'], self.new_calendar['location'])
            self.assertEqual(self.created_calendar['timeZone'], self.new_calendar['timeZone'])
            self.assertEqual(self.created_calendar['description'], self.new_calendar['description'])
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Insert new calendar test failed with exception: {e}")

    def test_get_calendar_by_id(self):
        # Verify the retrieved calendar's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # act
            c_list = self.service.get_calendar(self.created_calendar["id"])
            # assert
            self.assertEqual(c_list['kind'], self.config["object_kind"]["calendar"])
            self.assertEqual(c_list['id'], self.created_calendar["id"])
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Get calendar by ID test failed with exception: {e}")

    def test_patch_calendar(self):
        # Verify the patched calendar's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # arrange
            new_summary = generate_random_string(8)
            calendar_object = self.service.create_calendar_object(summary=new_summary)
            # act
            updated_calendar = self.service.patch_calendar(self.created_calendar["id"], calendar_object)
            # assert
            self.assertEqual(updated_calendar['kind'], self.config["object_kind"]["calendar"])
            self.assertEqual(updated_calendar['summary'], new_summary)
            self.assertEqual(self.new_calendar['description'], updated_calendar['description'])
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Patch calendar test failed with exception: {e}")

    def test_update_calendar(self):
        # Verify the updated calendar's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # arrange
            new_summary = generate_random_string(8)
            calendar_object = self.service.create_calendar_object(summary=new_summary)
            # act
            updated_calendar = self.service.update_calendar(self.created_calendar["id"], calendar_object)
            # assert
            self.assertEqual(updated_calendar['kind'], self.config["object_kind"]["calendar"])
            self.assertEqual(updated_calendar['summary'], new_summary)
            self.assertNotIn("description", updated_calendar)
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Update calendar test failed with exception: {e}")

    def test_delete_calendar_by_id(self):
        # Verify the calendar deletion operation
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # act
            response = self.service.delete_calendar(self.created_calendar["id"])
            # assert
            self.assertEqual(response, None)  # successful response returns None
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Delete calendar by ID test failed with exception: {e}")
