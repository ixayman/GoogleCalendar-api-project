import sqlite3

from tabulate import tabulate

from database.utils.convert_response_to_object import ConvertResponseToObject


class EventEndTimeDB:
    def __init__(self):
        self.conn = sqlite3.connect('../database.db')
        self.cur = self.conn.cursor()
        # cur.execute('DROP TABLE IF EXISTS end')
        self.cur.execute('CREATE TABLE IF NOT EXISTS end (ID TEXT PRIMARY KEY , '
                         'dateTime TEXT NOT NULL, timeZone TEXT NOT NULL)')

    def add_end_object_to_table_DB(self, new_event):
        converter = ConvertResponseToObject(new_event)
        end = converter.convert_end_to_object()
        self.cur.execute('INSERT INTO end (ID,dateTime, timeZone) VALUES(?,?,?)',
                         (end.id, end.dateTime, end.timeZone))
        self.conn.commit()

    def get_end_table_from_DB(self):
        self.cur.execute('SELECT * FROM end')
        rows = self.cur.fetchall()
        return rows

    def print_end_table_from_DB(self):
        self.cur.execute('SELECT * FROM end')
        rows = self.cur.fetchall()
        headers = ["id", "End DateTime", "End TimeZone"]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    def delete_end_object_from_table_DB(self, event):
        converter = ConvertResponseToObject(event)
        end = converter.convert_end_to_object()
        self.cur.execute('DELETE FROM end WHERE ID = ?', (end.id,))
        self.conn.commit()
