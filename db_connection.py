import sqlite3


class DbCon:
    def __init__(self):
        self.db = sqlite3.connect("tle-db/cache.db")
        self.create_tables()

    def create_tables(self):


    def fetch_contest_list(self):
        return self.db.execute(
            """select id from contest 
            where phase="FINISHED"
            order by start_time desc"""
        ).fetchall()

    def fetch_rating_changes(self, id):
        return self.db.execute(
            """select handle, old_rating, new_rating
            from rating_change
             where contest_id = ?
            """, (id,)
        ).fetchall()

# user -> handle, rating, no_of_contest, start_time, last_contest
# ranks -> rank, handle, no_of_contest, time