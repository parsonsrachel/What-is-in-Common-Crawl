from datasets import load_dataset
import sqlite3

# Create and or connect to database
con = sqlite3.connect("./data/c4_sample.db")
cur = con.cursor()


continue_prompt = input("Drops and recreates table if it already exists. Continue? (y, n)\n")
if continue_prompt != "y":
	print("Abort.")
	quit()

cur.execute("DROP TABLE IF EXISTS c4_sample")
cur.execute("CREATE TABLE IF NOT EXISTS c4_sample(url, timestamp, content)")
con.commit()

dataset = load_dataset('c4', 'en', split='train', streaming=True)
shuffled_dataset = dataset.shuffle(buffer_size=1, seed=42)
shuffled_dataset_iter = iter(shuffled_dataset)

n = 10_000
for _ in range(n):
    entry = next(shuffled_dataset_iter)
    data = (entry['url'], entry['timestamp'], entry['text'])
    cur.execute(f"INSERT INTO c4_sample VALUES(?,?,?)", data)
con.commit()

print("Database created")
