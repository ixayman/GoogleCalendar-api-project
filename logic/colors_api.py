from infra.google_service_provider import GoogleServiceProvider


class ColorsAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()
        self.colors = self.service.colors().get().execute()

    def get_colors(self):
        return self.colors

    def get_calendar_colors(self):
        # Returns calendars colors
        return self.colors['calendar']

    def get_event_colors(self):
        # Returns events colors
        return self.colors['event']
