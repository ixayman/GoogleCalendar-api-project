class Calendar:
    def __init__(self, id: str, summary: str,
                 location: str, description: str = None):
        self.kind = "calendar#events"
        self.id = id
        self.summary = summary
        self.description = description if description else ""
        self.location = location
        self.events_list = ""

    def to_dict(self):
        return {
            "kind": self.kind,
            "id": self.id,
            "summary": self.summary,
            "description": self.description,
            "location": self.location,
            "events_list": self.events_list
        }

