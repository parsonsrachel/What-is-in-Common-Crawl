import sqlite3

con = sqlite3.connect('c4_sample_2.db')
cur=con.cursor()

#create the column for the copyright information
cur.execute('ALTER TABLE c4_sample ADD copyrighted int')

#update each entry's copyrighted information
#enter a 1 if the content is copyrighted
#enter a 0 if not
cur.execute('SELECT url,content FROM c4_sample')
result_set=cur.fetchall()

for res in result_set:
    text=res[1]
    url=res[0]
    check_cr=text.split('©')
    if len(check_cr)>1:
        cur.execute("UPDATE c4_sample SET copyrighted='1' WHERE url=?;",[url])
        
    else:
        cur.execute("UPDATE c4_sample SET copyrighted='0' WHERE url=?;",[url])

con.commit() 
cur.close()

