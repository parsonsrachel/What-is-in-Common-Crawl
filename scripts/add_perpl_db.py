import sqlite3
import pyplexity
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--model",action='store',
                         dest='model_str',default='bigrams-bnc',
                         help='Model to use (case sensitive; options are bigrams-cord19, bigrams-bnc, trigrams-cord19, trigrams-bnc, default bigrams-bnc)')

args = argParser.parse_args()

print("Model: " + args.model_str)
model = pyplexity.PerplexityModel.from_str(args.model_str)

con = sqlite3.connect("./data/c4_sample.db")
cur = con.cursor()

continue_prompt = input("Drops and recreates column if it already exists. Continue? (y, n)\n")
if continue_prompt != "y":
	print("Abort.")
	quit()

col_model = args.model_str.replace("-", "_")

try:
    cur.execute("ALTER TABLE c4_sample DROP COLUMN " + col_model)
except:
     print("Column does not exist")

cur.execute("ALTER TABLE c4_sample ADD COLUMN " + col_model + " FLOAT")

cur.execute("SELECT url, timestamp, content FROM c4_sample")
rows = cur.fetchall()

# Iterate through rows and update n_tokens column
for row in rows:
    url, timestamp, content = row
    perpl = model.compute_sentence(content)

    # Update n_tokens column in the database
    cur.execute("UPDATE c4_sample SET " + col_model + " = ? WHERE url = ? AND timestamp = ?", (perpl, url, timestamp))

# Commit the changes to the database
con.commit()

# Close the database connection
con.close()

print("New column added")