import unittest
from logic.calendars_api import CalendarsAPI
from logic.calendarlist_api import CalendarListAPI
from logic.data_structures.calnedar import Calendar
from infra.utils import generate_random_string


class TestColorsAPI(unittest.TestCase):
    new_calendar = Calendar(summary='test calendar', location="Haifa",
                            time_zone="Asia/Jerusalem", description="calendar to run tests on").return_dict()

    def setUp(self):
        self.calendarsAPI = CalendarsAPI()
        self.calendars_listAPI = CalendarListAPI()

    def tearDown(self):
        self.api = None

    def test_insert_calendar(self):
        service = self.calendarsAPI
        self.assertIsNotNone(service, "Service should not be None")
        c_list = service.insert_calendar(self.new_calendar)
        self.assertEqual(c_list['summary'], self.new_calendar['summary'])
        self.assertEqual(c_list['location'], self.new_calendar['location'])
        self.assertEqual(c_list['timeZone'], self.new_calendar['timeZone'])
        self.assertEqual(c_list['description'], self.new_calendar['description'])

    def test_delete_calendar(self):
        service = self.calendarsAPI
        calendar = service.insert_calendar(self.new_calendar)
        calendar_id = service.get_calendar_id(self, calendar)
        self.assertIsNotNone(service, "Service should not be None")
        service.delete_calendar(calendar_id)

    def test_get_calendar(self):
        service = self.calendarsAPI
        self.assertIsNotNone(service, "Service should not be None")
        c_list = service.get_calendar('705c5da6880f8a88a3bdfac7803c36fe655fc3ff0778cdc4bc47f1029f0a7331@group.calendar.google.com')
        print(c_list)
