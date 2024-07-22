import unittest
from infra.logger import Logger
from logic.events_api import EventsAPI
from test.object_generator import example_event_object


class TestEventsAddAPI(unittest.TestCase):
    def setUp(self):
        # Initialize logger and EventsAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("-" * 26)
        self.logger.info("Setting up the test case environment")
        try:
            self.api = EventsAPI()
            self.config = self.api.config
        except Exception as e:
            self.logger.error(f"Error during setup: {e}")
            self.fail(f"Setup failed with exception: {e}")

    def tearDown(self):
        # Reset the EventsAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("Tearing down the test case environment")
        self.api = None
        self.logger.info("-" * 26)

    def test_add_event(self):
        # Verify the added event's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            event = example_event_object()
            new_event = self.api.insert_event(self.config['test_calendar_id'], event)
            self.assertEqual(new_event['kind'], self.config['object_kind']['event'])
            self.assertEqual(event['summary'], new_event['summary'])
            self.assertEqual(event['description'], new_event['description'])
            self.assertEqual(event['location'], new_event['location'])
            self.assertEqual(event['start']['dateTime'], new_event['start']['dateTime'])
            self.assertEqual(event['end']['dateTime'], new_event['end']['dateTime'])
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Add event API test failed with exception: {e}")

    def test_quick_add_event(self):
        # Verify the added event's attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            calendar_id = self.config['test_calendar_id']
            quick_add_text = self.config['quick_add_text']
            new_event = self.api.quick_add_event(calendar_id, quick_add_text)
            self.assertEqual(new_event['kind'], self.config['object_kind']['event'])
            self.assertIn(new_event['summary'], quick_add_text)
            self.assertIn(new_event['location'], quick_add_text)
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Quick add event API test failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
