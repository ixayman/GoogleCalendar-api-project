class EventsList:
    def __init__(self, id: str, summary: str,
                 timeZone: str, item: str, description: str = None):
        self.kind = "calendar#events"
        self.id = id
        self.summary = summary
        self.description = description if description else ""
        self.timeZone = timeZone
        self.item = item

    def to_dict(self):
        return {
            "kind": self.kind,
            "id": self.id,
            "summary": self.summary,
            "description": self.description,
            "timeZone": self.timeZone,
            "item": self.item
        }


class Item:
    def __init__(self, id: str):
        self.id = id
        self.events = "events"


