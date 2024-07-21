import unittest
from infra.api_wrapper import APIWrapper
from logic.events_api import EventsAPI
from logic.data_structures.calendar import Calendar
from logic.data_structures.event import test_event


class TestEventsAPI(unittest.TestCase):
    def setUp(self):
        self.api = EventsAPI()
        self.config = self.api.config

    def tearDown(self):
        self.api = None

    def test_quick_add_event_api(self):
        calendar_id = self.config['test_calendar_id']
        self.assertIsNotNone(self.api.service, "Service should not be None")
        self.api.quick_add_event(calendar_id, "hello")

    def test_get_calendar_events(self):
        self.assertIsNotNone(self.api.service, "Service should not be None")
        c_list = self.api.get_calendar_events(self.config['test_calendar_id'])
        print(c_list)

    def test_add_event(self):
        self.assertIsNotNone(self.api.service, "Service should not be None")
        event = test_event()
        new_event = self.api.insert_event(self.config['test_calendar_id'], event.return_dict())
        self.assertEqual(event.summary, new_event['summary'])
        self.assertEqual(event.description, new_event['description'])
        self.assertEqual(event.location, new_event['location'])
        self.assertEqual(event.start['dateTime'], new_event['start']['dateTime'])
        self.assertEqual(event.end['dateTime'], new_event['end']['dateTime'])

    def test_delete_event(self):
        c_list = self.api.get_calendar_events(self.config['test_calendar_id'])
        event_id = c_list['items'][0]['id']
        items = len(c_list['items'])
        self.assertIsNotNone(self.api.service, "Service should not be None")
        self.api.delete_event(self.config['test_calendar_id'], event_id)
        updated_list = self.api.get_calendar_events(self.config['test_calendar_id'])
        self.assertEqual(items - 1, len(updated_list['items']))
