import sqlite3
import tiktoken

# Calculates the number of tokens in content in the database and adds column with the number of tokens

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

con = sqlite3.connect("./data/c4_sample.db")
cur = con.cursor()

continue_prompt = input("Drops and recreates column if it already exists. Continue? (y, n)\n")
if continue_prompt != "y":
	print("Abort.")
	quit()

# Drop n_tokens column, if it does not exists do nothing
try:
    cur.execute("ALTER TABLE c4_sample DROP COLUMN n_tokens")
except:
     print("Column does not exist")

# Add n_tokens column
cur.execute("ALTER TABLE c4_sample ADD COLUMN n_tokens INTEGER")

# Fetch all rows in database
cur.execute("SELECT url, timestamp, content FROM c4_sample")
rows = cur.fetchall()

# Iterate through rows and update n_tokens column
for row in rows:
    url, timestamp, content = row
    token_integers = encoding.encode(content)
    n_tokens = len(token_integers)

    # Update n_tokens column in the database
    cur.execute("UPDATE c4_sample SET n_tokens = ? WHERE url = ? AND timestamp = ?", (n_tokens, url, timestamp))

# Commit the changes to the database
con.commit()

# Close the database connection
con.close()

print("New column added")