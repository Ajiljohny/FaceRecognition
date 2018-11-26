import sqlite3
from datetime import *
conn = sqlite3.connect("FaceBase1.db")
cmd = "SELECT * FROM People"
cursor = conn.execute(cmd)

for row in cursor:
    print(row)

conn.commit()

today = date.today()
dy=str(today)

print(dy)