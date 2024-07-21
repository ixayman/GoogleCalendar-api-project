from infra.google_service_provider import GoogleServiceProvider


class CalendarsAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()

    def clear_primary_calendar(self):
        # Clears a primary calendar.
        # This operation deletes all events associated with the primary calendar of an account
        return self.service.calendars().clear('primary').execute()

    def delete_calendar(self, calendar_id):
        # Deletes a secondary calendar
        self.service.calendars().delete(calendarId=calendar_id).execute()

    def get_calendar(self, calendar_id):
        # Returns metadata for a calendar
        return self.service.calendars().get(calendarId=calendar_id).execute()

    @staticmethod
    def get_calendar_id(self, calendar):
        return calendar['id']

    def insert_calendar(self, calendar):
        # Creates a secondary calendar
        return self.service.calendars().insert(body=calendar).execute()

    def update_calendar(self, calendar_id, description=None, location=None, summary=None, timeZone=None):
        # Updates an existing calendar summery
        calendar_list_entry = self.get_calendar(calendar_id)
        if description is not None:
            calendar_list_entry['description'] = description
        if location is not None:
            calendar_list_entry['location'] = location
        if summary is not None:
            calendar_list_entry['summary'] = summary
        if timeZone is not None:
            calendar_list_entry['timeZone'] = timeZone
        self.service.calendars().update(calendarId=calendar_id, body=calendar_list_entry).execute()
