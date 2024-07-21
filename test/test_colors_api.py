import unittest
from infra.api_wrapper import APIWrapper
from logic.colors_api import ColorsAPI


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        self.api = ColorsAPI()

    def tearDown(self):
        self.api = None

    def test_calendar_colors_api(self):
        service = self.api.service
        self.assertIsNotNone(service, "Service should not be None")
        colors = self.api.get_calendar_colors()
        self.assertIn("1", colors, "Color ID '1' should be in the colors")
        self.assertIn("foreground", colors["1"], "Foreground color should be present in color ID '1'")
        self.assertEqual(colors["1"]["foreground"], "#1d1d1d")

    def test_event_colors_api(self):
        service = self.api.service
        self.assertIsNotNone(service, "Service should not be None")
        colors = self.api.get_event_colors()
        self.assertIn("1", colors, "Color ID '1' should be in the colors")
        self.assertIn("foreground", colors["1"], "Foreground color should be present in color ID '1'")
        self.assertEqual(colors["1"]["foreground"], "#1d1d1d")
