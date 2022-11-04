import sqlite3
from time import sleep
from datetime import datetime
# read data from sqlite db using python  
con = sqlite3.connect('file:///C:/Users/user/mydatabase.db?mode=ro', uri=True)
cur = con.cursor()
# get all databases:
cur.execute("SELECT * FROM My_Table_name;")
data = cur.fetchall()
i=10
for thing in data:
    tag = thing[2]
    from_time = thing[i]
    to_time = thing[i+2]
    notes= thing[13]
    duration = datetime.fromisoformat(to_time) - datetime.fromisoformat(from_time) 
    print(tag, duration, notes)
    sleep(1)
