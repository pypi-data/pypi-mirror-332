import pandas as pd
from datetime import datetime
from tablename_fetcher import fetch_table_names, spot_table

def get_table_name(df, input_date):
    """Find the matching table name based on input date."""
    input_year = input_date.year
    input_month = input_date.strftime('%b').upper()  # Convert month to uppercase short name
    pattern = f"_{input_year}_{input_month}_"

    matching_table = df[df["Table Name"].str.contains(pattern, na=False, regex=False)]

    return matching_table.iloc[0]["Table Name"] if not matching_table.empty else "No matching table found."

def main():
    # Fetch table names
    df_tables = fetch_table_names()
    if df_tables is None:
        print("Failed to fetch table names. Exiting.")
        return

    # Get spot tables
    nifty_spot_table, sensex_spot_table = spot_table(df_tables)

    # User input
    user_date = input("Enter date (YYYY-MM-DD): ")
    instrument = input("Enter instrument (nifty/sensex): ").strip().lower()

    try:
        input_date = datetime.strptime(user_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    # Determine the table name
    if instrument == "nifty":
        table_name = get_table_name(nifty_spot_table, input_date)
    elif instrument == "sensex":
        table_name = get_table_name(sensex_spot_table, input_date)
    else:
        print("Invalid instrument. Choose 'nifty' or 'sensex'.")
        return

    print("Matching Table Name:", table_name)

if __name__ == "__main__":
    main()
