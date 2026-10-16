from model.owner import Owner
from error import Missing, Duplicate
import sqlite3

conn = sqlite3.connect('db/data.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def get_all() -> list[Owner]:
    try:
        cur.execute("SELECT * FROM Owner")
    except Exception as err:
        Missing(msg=f"Owner not found")

    qres = cur.fetchall()

    return list(map(
        lambda a: 
            Owner(
                id=a["id"], 
                name=a["name"], 
                surname=a["surname"],
                iin=a["iin"]), 
        qres))

def get_one(owner_id: int) -> Owner:
    try:
        cur.execute("SELECT * FROM Owner WHERE id = ?", owner_id)
    except Exception as err:
        Missing(msg=f"Owner {name} not found")

