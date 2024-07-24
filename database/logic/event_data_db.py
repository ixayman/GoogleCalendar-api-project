import sqlite3
from database.utils.convert_response_to_object import ConvertResponseToObject
from tabulate import tabulate


class EventDataDB:
    def __init__(self):
        self.conn = sqlite3.connect('../database.db')
        self.cur = self.conn.cursor()
        # cur.execute('DROP TABLE IF EXISTS event')
        self.cur.execute('CREATE TABLE IF NOT EXISTS event (ID TEXT PRIMARY KEY , summery TEXT NOT NULL,'
                         'location TEXT NOT NULL, start TEXT NOT NULL, end TEXT NOT NULL, description TEXT)')

    def add_event_to_table_DB(self, new_event):
        converter = ConvertResponseToObject(new_event)
        event = converter.convert_event_response_to_object()
        self.cur.execute('INSERT INTO event (ID,summery, location, start, end, description) VALUES(?,?,?,?,?,?)',
                         (event.id, event.summary, event.location,
                          event.start, event.end, event.description))

        self.conn.commit()

    def get_event_table_from_DB(self):
        self.cur.execute('SELECT * FROM event')
        rows = self.cur.fetchall()
        return rows

    def print_event_table_from_DB(self):
        self.cur.execute('SELECT * FROM event')
        rows = self.cur.fetchall()
        headers = ["id", "Summary", "Location", "Start id", "End id", "Description"]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    def delete_event_from_table_DB(self, event):
        self.cur.execute('DELETE FROM event WHERE ID = ?', (event['id'],))
        self.conn.commit()
