import pandas as pd
from tablename_fetcher import fetch_table_names, extract_expiry_dates, get_expiry_type, spot_table
from query_executer import execute_query

def main():
    # Fetch table names
    df_tables = fetch_table_names()
    if df_tables is None:
        print("Failed to fetch table names. Exiting.")
        return
    
    # Extract expiry dates
    nifty_options_table, sensex_options_table = extract_expiry_dates(df_tables)

    # Create expiry DataFrames
    nifty_expiry = nifty_options_table[['Expiry Date']].dropna().reset_index(drop=True)
    sensex_expiry = sensex_options_table[['Expiry Date']].dropna().reset_index(drop=True)

    # Assign expiry types
    nifty_expiry['expiry_type'] = nifty_expiry['Expiry Date'].apply(get_expiry_type)
    sensex_expiry['expiry_type'] = sensex_expiry['Expiry Date'].apply(get_expiry_type)

    # Get user input
    user_date = input("Enter the date (YYYY-MM-DD): ").strip()
    instrument_name = 'nifty' #input("Enter the instrument name (nifty/sensex): ").strip().lower()
    instrument_type = 'options' #input("Enter the instrument type (options/spot): ").strip().lower()
    spot_instrument_type = 'spot'
    
    user_date_obj = pd.to_datetime(user_date, format='%Y-%m-%d')

    # Select expiry DataFrame based on user input
    if instrument_name == "nifty" and instrument_type == "options":
        expiry_df = nifty_expiry
        options_table = nifty_options_table
    elif instrument_name == "sensex" and instrument_type == "options":
        expiry_df = sensex_expiry
        options_table = sensex_options_table
    else:
        print("Invalid instrument name or type. Exiting.")
        return

    # Get available expiries for the given month
    selected_month_expiries = expiry_df[expiry_df['Expiry Date'].str.startswith(user_date_obj.strftime('%Y_%m'))]

    if selected_month_expiries.empty:
        print(f"No expiry found for {instrument_name} {instrument_type} in {user_date_obj.strftime('%B %Y')}")
        return

    # Display expiry options
    print("\nAvailable Expiries:")
    for i, expiry in enumerate(selected_month_expiries['Expiry Date']):
        print(f"{i + 1}. {expiry}")

    # Ask user to choose an expiry
    try:
        expiry_choice = int(input("\nSelect an expiry (Enter number): ").strip()) - 1
        if expiry_choice < 0 or expiry_choice >= len(selected_month_expiries):
            raise ValueError
    except ValueError:
        print("Invalid choice. Exiting.")
        return

    selected_expiry = selected_month_expiries.iloc[expiry_choice]['Expiry Date']
    print(f"\nYou selected expiry: {selected_expiry}")

    # Fetch table name corresponding to the selected expiry
    expiry_table = options_table[options_table['Expiry Date'] == selected_expiry]['Table Name']

    if expiry_table.empty:
        print(f"No table found for expiry {selected_expiry}")
        return

    print("\n TableName for Selected Expiry:")
    print(expiry_table.to_string(index=False))

    # Ask user for the date to fetch data
    fetch_date = user_date #input("Enter the date to fetch data (YYYY-MM-DD): ").strip()

    # # Execute query
    table_name = expiry_table.values[0]
    df_data = execute_query(table_name, fetch_date)

    if df_data is not None:
        print("\nFetched Data:")
        print(df_data)
    else:
        print("No data found.")

    nifty_spot_table, sensex_spot_table = spot_table(df_tables) 

    # print(nifty_spot_table)
    # print(sensex_spot_table)
 
if __name__ == "__main__":
    main()
