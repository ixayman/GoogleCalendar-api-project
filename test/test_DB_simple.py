import unittest

from infra.logger import Logger
from logic.events_api import EventsAPI
from test.object_generator import example_event_object

from database.logic.event_data_db import EventDataDB
from database.logic.event_start_time_db import EventStartTimeDB
from database.logic.event_end_time_db import EventEndTimeDB
from database.utils.join_tables import JoinTables


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

    def test_add_event_to_DB(self):

        self.logger.info("Test Case: " + self._testMethodName)
        try:
            # arrange
            event_data = EventDataDB()
            event_start_time = EventStartTimeDB()
            event_end_time = EventEndTimeDB()

            event_data.add_event_to_table_DB(self.new_event)
            event_start_time.add_start_object_to_table_DB(self.new_event)
            event_end_time.add_end_object_to_table_DB(self.new_event)
            print("Tables content after adding an event:\n")
            print("event_data table:")
            event_data.print_event_table_from_DB()
            print("\nevent_start_time table:")
            event_start_time.print_start_table_from_DB()
            print("\nevent_end_time table:")
            event_end_time.print_end_table_from_DB()
            print("------------\n")
            print("Join tables:")
            JoinTables()
            print("------------\n"
                  "")
            event_data.delete_event_from_table_DB(self.new_event)
            event_start_time.delete_start_object_from_table_DB(self.new_event)
            event_end_time.delete_end_object_from_table_DB(self.new_event)

            print("Tables content after deleting an event:\n")
            print("event_data table:")
            event_data.print_event_table_from_DB()
            print("\nevent_start_time table:")
            event_start_time.print_start_table_from_DB()
            print("\nevent_end_time table:")
            event_end_time.print_end_table_from_DB()

        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Add event API test failed with exception: {e}")
