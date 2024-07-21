from infra.google_service_provider import GoogleServiceProvider


class CalendarListAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()

    def delete_calendar(self, calendar_id):
        # Removes a calendar from the user's calendar list
        self.service.calendarList().delete(calendarId=calendar_id).execute()

    def get_calendar(self, calendar_id):
        # Returns a calendar from the user's calendar list
        return self.service.calendarList().get(calendarId=calendar_id).execute()

    def insert_calendar(self, calendar):
        # Inserts an existing calendar into the user's calendar list
        self.service.calendarList().insert(body=calendar).execute()

    def get_calendar_list(self):
        # Returns the calendars on the user's calendar list
        return self.service.calendarList().list().execute()

    def update_calendar_summery(self, calendar_id, summary):
        # Updates an existing calendar summery
        calendar_list_entry = self.get_calendar(calendar_id)
        calendar_list_entry['summaryOverride'] = summary
        self.service.calendarList().update(calendarId=calendar_id, body=calendar_list_entry).execute()
