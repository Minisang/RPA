import pandas as pd
import sqlite3

conn = sqlite3.connect('education.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO city (Name, CountryCode, Population) VALUES ("Busan", "KOR", 5000000);')
# cursor.execute('UPDATE city SET Population = 5500000 WHERE Name="Busan" ;')
# cursor.execute('DELETE FROM city WHERE Name = "Busan";')
conn.commit()

cursor.execute('SELECT * FROM city WHERE Name="Busan"')
results = cursor.fetchall()
df = pd.DataFrame(results)
print(df, end="\n\n")

conn.close()
