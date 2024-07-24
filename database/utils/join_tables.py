import sqlite3
from tabulate import tabulate


class JoinTables:
    def __init__(self):
        self.conn = sqlite3.connect('../database.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
            SELECT event.ID, event.summery, event.location,
                   start.dateTime AS startDateTime, start.timeZone AS startTimeZone,
                   end.dateTime AS endDateTime, end.timeZone AS endTimeZone ,event.description
            from event
            INNER JOIN start ON event.start = start.id
            INNER JOIN end ON event.end = end.id
        ''')

        rows = self.cur.fetchall()
        headers = ["id", "Summary", "Location", "Start DateTime", "Start TimeZone", "End DateTime",
                   "End TimeZone", "Description"]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))
