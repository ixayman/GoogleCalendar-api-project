from logic.calendars_api import CalendarsAPI
from logic.events_api import EventsAPI


def example_calendar_object():
    # create calendar object with given parameters
    return CalendarsAPI.create_calendar_object(description="calendar to run tests on", location="Haifa",
                                               summary="test calendar", timeZone="Asia/Jerusalem")


def example_event_object():
    # create event object with given parameters
    return EventsAPI.create_event_object(summary="test event", location="Asia/Jerusalem",
                                         description="hello, this is a test event",
                                         start={'dateTime': "2024-07-25T06:00:00+03:00", "timeZone": "Asia/Jerusalem"},
                                         end={'dateTime': "2024-07-25T08:00:00+03:00", "timeZone": "Asia/Jerusalem"})


def example_event_object_to_update():
    # create event object with given parameters
    return EventsAPI.create_event_object(summary="test event updated", location="Asia/Jerusalem",
                                         start={'dateTime': "2024-07-25T10:00:00+03:00", "timeZone": "Asia/Jerusalem"},
                                         end={'dateTime': "2024-07-25T12:00:00+03:00", "timeZone": "Asia/Jerusalem"})


def get_actual_calendar_summaries():
    # get list of actual calendar summaries
    return {"calendar for testing", "QA Automation", "Holidays in Israel"}
