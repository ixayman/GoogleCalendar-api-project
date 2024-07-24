class Event:
    def __init__(self, id: str, summary: str, location: str,
                 start: str, end: str, description: str = None):
        self.kind = "calendar#event"
        self.id = id
        self.summary = summary
        self.description = description if description else ""
        self.location = location
        self.start = start
        self.end = end

    def to_dict(self):
        return {
            "kind": self.kind,
            "id": self.id,
            "summary": self.summary,
            "description": self.description,
            "location": self.location,
            "start": self.start,
            "end": self.end
        }

