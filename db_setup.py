import sqlite3
import pandas as pd

# Corrected CSV file path (since the file is inside the 'data' folder)
csv_file = "data/suicide_data.csv"
df = pd.read_csv(csv_file)

# Connects to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect("data/suicide_data.db")  # Creates or opens the database
cursor = conn.cursor()

# Creates the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS suicide_rates (
        UNIT TEXT,  
        UNIT_NUM INT,
        STUB_NAME TEXT, 
        STUB_NAME_NUM INT,
        STUB_LABEL TEXT,
        STUB_LABEL_NUM INT,
        YEAR INT NOT NULL,
        AGE TEXT,  
        AGE_NUM INT,  
        ESTIMATE FLOAT NOT NULL,
        FLAG TEXT   
    );
""")

# Inserts CSV data into the correct table
df.to_sql("suicides", conn, if_exists="append", index=False)  # Corrected table name

# Commit and close connection
conn.commit()
conn.close()

# print(df.columns)

print("CSV data successfully inserted into the SQLite database!")