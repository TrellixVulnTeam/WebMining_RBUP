import sqlite3
con = sqlite3.connect('searchindex.db')
cur = con.cursor()
cur.execute('select w0.urlid,w0.location from wordlocation w0 where w0.wordid=4')
res = cur.fetchall()
for line in res:
    print(line)