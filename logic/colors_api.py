from infra.google_service_provider import GoogleServiceProvider


class ColorsAPI(GoogleServiceProvider):


    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()
        self.colors = self.service.colors().get().execute()

    def print_colors(self):
        print(self.colors)

    def get_calendar_colors(self):
        return self.colors['calendar']

    def get_event_colors(self):
        return self.colors['event']

