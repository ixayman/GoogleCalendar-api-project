import unittest
from logic.colors_api import ColorsAPI


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        # Initialize ColorsAPI instance and retrieve colors
        self.api = ColorsAPI()
        self.colors = self.api.get_colors()

    def tearDown(self):
        # Reset the ColorsAPI instance
        self.api = None

    def test_get_colors_api(self):
        # Verify the retrieved colors contain expected keys and kind
        # assert
        self.assertEqual(self.colors["kind"], "calendar#colors")
        self.assertIn("calendar", self.colors)
        self.assertIn("event", self.colors)

