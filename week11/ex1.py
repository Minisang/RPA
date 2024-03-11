import pandas as pd
import sqlite3

conn = sqlite3.connect('education.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM city')
results = cursor.fetchall()
df = pd.DataFrame(results)
print(df.head(20), end="\n\n")

conn.close()
