class Event:
    def __init__(self, summary=None, location=None, description=None, start=None, end=None, ):
        self.summary = summary
        self.location = location
        self.description = description
        self.start = start or {}
        self.end = end or {}

    def return_dict(self):
        return self.__dict__


def test_event():
    return Event(summary="test event", location="Asia/Jerusalem", description="hello, this is a test event",
                 start={'dateTime': "2024-07-25T06:00:00+03:00", "timeZone": "Asia/Jerusalem"},
                 end={'dateTime': "2024-07-25T08:00:00+03:00", "timeZone": "Asia/Jerusalem"})
