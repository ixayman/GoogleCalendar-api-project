
class Calendar:
    def __init__(self, summary=None, description=None, location=None, time_zone=None):
        self.summary = summary
        self.description = description
        self.location = location
        self.timeZone = time_zone

    def return_dict(self):
        return self.__dict__

