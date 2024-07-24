import sqlite3

from tabulate import tabulate

from database.utils.convert_response_to_object import ConvertResponseToObject


class EventStartTimeDB:
    def __init__(self):
        self.conn = sqlite3.connect('../database.db')
        self.cur = self.conn.cursor()
        # cur.execute('DROP TABLE IF EXISTS start')
        self.cur.execute('CREATE TABLE IF NOT EXISTS start (ID TEXT PRIMARY KEY , '
                         'dateTime TEXT NOT NULL, timeZone TEXT NOT NULL)')

    def add_start_object_to_table_DB(self, new_event):
        converter = ConvertResponseToObject(new_event)
        start = converter.convert_start_to_object()
        self.cur.execute('INSERT INTO start (ID,dateTime, timeZone) VALUES(?,?,?)',
                         (start.id, start.dateTime, start.timeZone))

        self.conn.commit()

    def get_start_table_from_DB(self):
        self.cur.execute('SELECT * FROM start')
        rows = self.cur.fetchall()
        return rows

    def print_start_table_from_DB(self):
        self.cur.execute('SELECT * FROM start')
        rows = self.cur.fetchall()
        headers = ["id", "Start DateTime", "Start TimeZone"]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    def delete_start_object_from_table_DB(self, event):
        converter = ConvertResponseToObject(event)
        start = converter.convert_start_to_object()
        self.cur.execute('DELETE FROM start WHERE ID = ?', (start.id,))
        self.conn.commit()
