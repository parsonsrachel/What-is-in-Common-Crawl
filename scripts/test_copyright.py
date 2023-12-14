import sqlite3

con = sqlite3.connect('c4_sample_2.db')
cur = con.cursor()

#select all content
cur.execute("SELECT content FROM c4_sample WHERE copyrighted='1'")
result_set = cur.fetchall()

for res in result_set:
    c_symbol_set = res[0].split('©')
    #assert that symbol was found
    assert(len(c_symbol_set) > 1)

con.commit() 
cur.close()
