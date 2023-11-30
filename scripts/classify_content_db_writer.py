import sqlite3
from whatsincc import google_cloud_lang

# Requires Google Cloud Authentication

conn = sqlite3.connect("./data/c4_sample.db")
c = conn.cursor()

# Add classification column,, if it already exists do nothing
try:
    c.execute("ALTER TABLE c4_sample ADD COLUMN google_classifier 'text'")
except:
    pass

rows = c.execute('SELECT url, content FROM c4_sample WHERE google_classifier IS NULL').fetchall()
for row in rows:
    c.execute("UPDATE c4_sample SET google_classifier = ? WHERE url = ?;", (str(google_cloud_lang.classify(row[1])), row[0]))
    conn.commit()

c.close()
