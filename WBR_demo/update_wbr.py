import sqlite3
import pandas as pd
import os

def main():
    db_file = 'events.db'
    sql_file = 'data.sql'
    excel_file = 'WBR.xlsx'
    sheet_name = 'Data'

    if not os.path.exists(db_file):
        print(f"Error: {db_file} not found.")
        return
    if not os.path.exists(sql_file):
        print(f"Error: {sql_file} not found.")
        return
    if not os.path.exists(excel_file):
        print(f"Error: {excel_file} not found.")
        return

    # Read SQL query
    with open(sql_file, 'r') as f:
        query = f.read()

    # Connect to database and execute query
    try:
        conn = sqlite3.connect(db_file)
        df = pd.read_sql_query(query, conn)
        conn.close()
    except Exception as e:
        print(f"Error executing SQL: {e}")
        return

    # Write to Excel
    try:
        # mode='a' appends to existing file, if_sheet_exists='replace' replaces the sheet
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Successfully wrote {len(df)} rows to {sheet_name} in {excel_file}")
    except Exception as e:
        print(f"Error writing to Excel: {e}")

if __name__ == '__main__':
    main()
