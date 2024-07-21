import unittest
from infra.api_wrapper import APIWrapper
from logic.calendarlist_api import CalendarListAPI
from logic.calendars_api import CalendarsAPI
from logic.data_structures.calnedar import Calendar


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        self.api = CalendarListAPI()
        self.calendarsAPI = CalendarsAPI()

    def tearDown(self):
        self.api = None

    def test_get_calendar_list_api(self):
        service = self.api.service
        self.assertIsNotNone(service, "Service should not be None")
        c_list = self.api.get_calendar_list()
        print(c_list)


