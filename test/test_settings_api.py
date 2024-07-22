import unittest
from infra.logger import Logger
from logic.settings_api import SettingsAPI


class TestColorsAPI(unittest.TestCase):

    def setUp(self):
        # Initialize logger and SettingsAPI instance
        self.logger = Logger.setup_logger(__name__)
        self.logger.info("Setting up the test case environment")
        try:
            self.api = SettingsAPI()
        except Exception as e:
            self.logger.error(f"Error during setup: {e}")
            self.fail(f"Setup failed with exception: {e}")

    def tearDown(self):
        # Reset the SettingsAPI instance
        self.logger.info("Tearing down the test case environment")
        self.api = None

    def test_user_settings_api(self):
        # Verify the retrieved settings' kind attribute
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            settings = self.api.get_user_settings()
            self.assertEqual(settings['kind'], self.api.config['object_kind']['settings'])
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"User settings API test failed with exception: {e}")

    def test_single_setting_api(self):
        # Verify the retrieved setting's kind and id attributes
        self.logger.info("Test Case: " + self._testMethodName)
        try:
            setting = self.api.config['calendar_settings'][1]
            settings = self.api.get_single_setting(setting)
            self.assertEqual(settings['kind'], self.api.config['object_kind']['setting'])
            self.assertEqual(settings['id'], setting)
            self.logger.info(self._testMethodName + " - passed")
        except Exception as e:
            self.logger.error(f"Test failed with exception: {e}")
            self.fail(f"Single setting API test failed with exception: {e}")
