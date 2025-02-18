import sqlite3

# Connect to the database
conn = sqlite3.connect("data/suicide_data.db")
cursor = conn.cursor()

# Fetch first 5 rows
cursor.execute("SELECT * FROM suicide_rates LIMIT 5;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
