import pandas as pd
import sqlite3
""" This is a Python script that will quickly convert a CSV file into a DB file. I had previously used this to convert data into a CSV file so that I could upload it to an online SQL compiler. I did not use it for this project, but kept it in the repo as to show my familiarity with Python """
def csv_to_sqlite(csv_file, output_db_file, table_name):
    
    try:
        # Load CSV into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Connect to SQLite database (will create the file if it doesn't exist)
        conn = sqlite3.connect(output_db_file)

        # Write DataFrame to the SQLite database
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Successfully converted '{csv_file}' into '{output_db_file}' as table '{table_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Example Usage
csv_file_path = "C:\\Users\\James\\Downloads\\1000000 Sales Records\\1000000 Sales Records.csv"           # Can replace with any .CSV file path
output_database = "1000000 Sales Records.db"        # Replace with your desired database file name
table_name = "sales_records"              # Replace with your desired table name

csv_to_sqlite(csv_file_path, output_database, table_name)
