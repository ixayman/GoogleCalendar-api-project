import unittest

from infra.logger import Logger
from infra.utils import generate_random_string
from logic.events_api import EventsAPI
from test.object_generator import example_event_object, example_event_object_to_update


class TestEventsOperationsAPI(unittest.TestCase):
    def setUp(self):
        # Initialize logger and EventsAPI instance, and insert a new event
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("-" * 26)
        self.logger.info("Setting up the test case environment")
        try:
            self.api = EventsAPI()
            self.config = self.api.config
            event = example_event_object()
            self.new_event = self.api.insert_event(self.config['test_calendar_id'], event)
        except Exception as e:
            self.logger.error(f"Error during setup: {e}")
            self.fail(f"Setup failed with exception: {e}")

    def tearDown(self):
        # Delete the created event and reset the EventsAPI instance
        self.logger.info("Tearing down the test case environment")
        try:
            self.api.delete_event(self.config['test_calendar_id'], self.new_event['id'])
        except Exception as e:
            self.logger.info(f"exception incase of event deletion test, no second deletion needed")
            pass
        self.api = None
        self.logger.info("-" * 26)

    def test_get_event_by_id(self):
        # Verify the retrieved event's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # act
            event = self.api.get_event_by_id(self.config['test_calendar_id'], self.new_event['id'])
            # assert
            self.assertEqual(event['kind'], self.config['object_kind']['event'])
            self.assertEqual(event['id'], self.new_event['id'])

        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Get event by ID test failed with exception: {e}")

    def test_get_calendar_events(self):
        # Verify the retrieved events list's kind attribute
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # act
            c_list = self.api.get_calendar_events(self.config['test_calendar_id'])
            # assert
            self.assertEqual(c_list['kind'], 'calendar#events')

        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Get calendar events test failed with exception: {e}")

    def test_patch_event(self):
        # Verify the patched event's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # arrange
            new_summary = generate_random_string(8)
            # act
            event_object = self.api.create_event_object(summary=new_summary)
            updated_event = self.api.patch_event(self.config['test_calendar_id'], self.new_event['id'], event_object)
            # assert
            self.assertEqual(updated_event['kind'], self.config['object_kind']['event'])
            self.assertEqual(updated_event['summary'], new_summary)
            self.assertEqual(self.new_event['description'], updated_event['description'])

        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Patch event test failed with exception: {e}")

    def test_update_event(self):
        # Verify the updated event's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # arrange
            event_object = example_event_object_to_update()
            # act
            updated_event = self.api.update_event(self.config['test_calendar_id'], self.new_event['id'], event_object)
            # assert
            self.assertEqual(updated_event['kind'], self.config['object_kind']['event'])
            self.assertEqual(updated_event['summary'], event_object['summary'])
            self.assertNotIn("description", updated_event)

        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Update event test failed with exception: {e}")

    def test_delete_event(self):
        # Verify the deletion operation
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # act
            response = self.api.delete_event(self.config['test_calendar_id'], self.new_event['id'])
            # assert
            self.assertEqual(response, None)  # successful response returns None
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Delete event test failed with exception: {e}")


