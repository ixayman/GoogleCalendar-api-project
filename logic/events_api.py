from infra.google_service_provider import GoogleServiceProvider


class EventsAPI(GoogleServiceProvider):

    def __init__(self):
        super().__init__()
        self.service = self.authenticate_google_service()

    def delete_event(self, calendar_id, event_id):
        # Deletes an event
        self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()

    def get_event(self, calendar_id, event_id):
        # Returns an event based on its Google Calendar ID
        return self.service.events().get(calendarId=calendar_id, eventId=event_id).execute()

    def import_event(self, calendar_id, event):
        # Imports an event
        return self.service.events().import_(calendarId=calendar_id, body=event).execute()

    def insert_event(self, calendar_id, event):
        # Creates an event
        return self.service.events().insert(calendarId=calendar_id, body=event).execute()

    def event_instances(self, calendar_id, event_id):
        # Returns instances of the specified recurring event
        return self.service.events().instances(calendarId=calendar_id, eventId=event_id).execute()

    def get_calendar_events(self, calendar_id):
        # Returns events on the specified calendar
        return self.service.events().list(calendarId=calendar_id).execute()

    def move_event(self, calendar_id, event_id, destination_calendar_id):
        # Moves an event to another calendar
        return self.service.events().move(calendarId=calendar_id, eventId=event_id,
                                          destination=destination_calendar_id).execute()

    def quick_add_event(self, calendar_id, text):
        # Creates an event based on a simple text string
        return self.service.events().quickAdd(calendarId=calendar_id, text=text).execute()

    def update_event(self, calendar_id, event):
        # Updates an event
        return self.service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
