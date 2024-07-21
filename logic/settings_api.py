from infra.google_service_provider import GoogleServiceProvider


class SettingsAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()

    def get_user_settings(self):
        # Returns all user settings for the authenticated user
        return self.service.settings().list().execute()

    def get_single_setting(self, setting_id):
        # Returns a single user setting
        return self.service.settings().get(setting=setting_id).execute()
