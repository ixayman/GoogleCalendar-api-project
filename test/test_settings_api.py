import unittest
from infra.api_wrapper import APIWrapper
from logic.settings_api import SettingsAPI


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        self.api = SettingsAPI()

    def tearDown(self):
        self.api = None

    def test_user_settings_api(self):
        service = self.api.service
        self.assertIsNotNone(service, "Service should not be None")
        settings = self.api.get_user_settings()
        # print(settings)

    def test_single_setting_api(self):
        service = self.api.service
        self.assertIsNotNone(service, "Service should not be None")
        settings = self.api.get_single_setting('format24HourTime')
        print(settings)
