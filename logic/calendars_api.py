from infra.google_service_provider import GoogleServiceProvider


class CalendarsAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()

    def insert_calendar(self, calendar):
        # Creates a secondary calendar
        return self.service.calendars().insert(body=calendar).execute()

    def get_calendar(self, calendar_id):
        # Returns metadata for a calendar
        return self.service.calendars().get(calendarId=calendar_id).execute()

    @staticmethod
    def create_calendar_object(description=None, location=None, summary=None, timeZone=None):
        # Creates a calendar object
        calendar_list_entry = {}
        if description is not None:
            calendar_list_entry['description'] = description
        if location is not None:
            calendar_list_entry['location'] = location
        if summary is not None:
            calendar_list_entry['summary'] = summary
        if timeZone is not None:
            calendar_list_entry['timeZone'] = timeZone
        return calendar_list_entry

    @staticmethod
    def get_calendar_id(self, calendar):
        return calendar['id']

    def patch_calendar(self, calendar_id, calendar_object):
        # Updates parts of an existing calendar
        return self.service.calendars().patch(calendarId=calendar_id, body=calendar_object).execute()

    def update_calendar(self, calendar_id, calendar_object):
        # refill an existing calendar data
        return self.service.calendars().update(calendarId=calendar_id, body=calendar_object).execute()

    def delete_calendar(self, calendar_id):
        # Deletes a secondary calendar
        self.service.calendars().delete(calendarId=calendar_id).execute()


