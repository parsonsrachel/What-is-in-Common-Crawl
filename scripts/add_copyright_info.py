import sqlite3

con = sqlite3.connect('./data/c4_sample.db')
cur = con.cursor()

    
#create the column for the copyright information
cur.execute('ALTER TABLE c4_sample ADD copyrighted int')

#get all url, content pairs
cur.execute('SELECT url, content FROM c4_sample')
result_set = cur.fetchall()

#for each entry in database look for copyright symbol
for res in result_set:
    text=res[1]
    url=res[0]
    check_cr = text.split('©')
    if len(check_cr)>1:
        #if copyright symbol found, make the content as copyrighted
        cur.execute("UPDATE c4_sample SET copyrighted='1' WHERE url=?;",[url])
        
    else:
        #content is not copyrighted
        cur.execute("UPDATE c4_sample SET copyrighted='0' WHERE url=?;",[url])

con.commit() 
cur.close()

