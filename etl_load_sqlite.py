import sqlite3
import pandas as pd
import os

def load_data():
    # Ensure the database directory exists
    os.makedirs('data/db', exist_ok=True)
    
    # Load CSV and save to SQLite
    df = pd.read_csv('data/raw/customers_raw.csv')
    conn = sqlite3.connect('data/db/analytics.db')
    df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    conn.close()
    print("Successfully loaded data from CSV to SQLite database.")

if __name__ == "__main__":
    load_data()