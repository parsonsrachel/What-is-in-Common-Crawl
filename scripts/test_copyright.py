import sqlite3

con = sqlite3.connect('c4_sample_2.db')
cur = con.cursor()

cur.execute("SELECT content FROM c4_sample WHERE copyrighted='1'")
result_set = cur.fetchall()

for res in result_set:
    c_symbol_set = res[0].split('©')
    assert(len(c_symbol_set) > 1)
