import pandas as pd
import sqlite3

conn = sqlite3.connect('education.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM city ORDER BY population DESC LIMIT 4;')
results = cursor.fetchall()

df = pd.DataFrame(results)
print(df, end="\n\n")

conn.close()
