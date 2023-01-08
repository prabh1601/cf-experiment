from db_connection import DbCon

db = DbCon()

contest_id_list = db.fetch_contest_list()

for contest in contest_id_list:
    rating_changes = db.fetch_rating_changes(contest[0])
    break
