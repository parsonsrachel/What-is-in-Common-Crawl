import sqlite3
import pyplexity
import argparse

# Calculates the perplexity score of content in the database and adds column with the perplexity score
# The LM can be chosen: British National Corpus (BNC) or CORD-19, and either bigrams or trigrams

# Takes in a model argument
argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--model",action='store',
                         dest='model_str',default='bigrams-bnc',
                         help='Model to use (case sensitive; options are bigrams-cord19, bigrams-bnc, trigrams-cord19, trigrams-bnc, default bigrams-bnc)')

args = argParser.parse_args()

print("Model: " + args.model_str)
model = pyplexity.PerplexityModel.from_str(args.model_str)

# Connects to the database
con = sqlite3.connect("./data/c4_sample.db")
cur = con.cursor()

continue_prompt = input("Drops and recreates column if it already exists. Continue? (y, n)\n")
if continue_prompt != "y":
	print("Abort.")
	quit()

col_model = args.model_str.replace("-", "_")

# Drop perplexity column, if it does not exists do nothing
# Column name is the model name
try:
    cur.execute("ALTER TABLE c4_sample DROP COLUMN " + col_model)
except:
     print("Column does not exist")

# Add perplexity column
cur.execute("ALTER TABLE c4_sample ADD COLUMN " + col_model + " FLOAT")

# Fetch all rows in database
cur.execute("SELECT url, timestamp, content FROM c4_sample")
rows = cur.fetchall()

# Iterate through rows and update perplexity column
for row in rows:
    url, timestamp, content = row
    perpl = model.compute_sentence(content)

    # Update perplexity column in the database
    cur.execute("UPDATE c4_sample SET " + col_model + " = ? WHERE url = ? AND timestamp = ?", (perpl, url, timestamp))

# Commit the changes to the database
con.commit()

# Close the database connection
con.close()

print("New column added")