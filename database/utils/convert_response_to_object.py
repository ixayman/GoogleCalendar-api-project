from database.objects import event_data, event_start_time, event_end_time


class ConvertResponseToObject:
    def __init__(self, response):
        self.response = response

    def convert_start_to_object(self):
        return event_start_time.StartTime(id=f'start{self.response["id"]}', dateTime=self.response['start']['dateTime'],
                                          timeZone=self.response['start']['timeZone'])

    def convert_end_to_object(self):
        return event_end_time.EndTime(id=f'end{self.response["id"]}', dateTime=self.response['end']['dateTime'],
                                      timeZone=self.response['end']['timeZone'])

    def convert_event_response_to_object(self):
        start = self.convert_start_to_object()
        end = self.convert_end_to_object()
        return event_data.Event(id=self.response['id'], summary=self.response['summary'],
                                location=self.response['location']
                                , start=start.id, end=end.id,
                                description=self.response['description'])
