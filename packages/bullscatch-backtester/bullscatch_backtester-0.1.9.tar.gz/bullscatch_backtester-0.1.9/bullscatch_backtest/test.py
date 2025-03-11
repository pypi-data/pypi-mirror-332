from spot_fetch_spa import get_spot_data
from expiry_list_spa import get_expiries

user_date = "2024-03-07"
instrument_name = "nifty"
instrument_type = "options"

# date_str = "2024-03-07"
# instrument_type = "sensex"

# data = get_spot_data(date_str, instrument_type)

# Get available expiry dates
expiries = get_expiries(instrument_name, instrument_type, user_date)

# Display expiry options
if expiries is not None and not expiries.empty:
        print("\nAvailable Expiries:")
        for i, expiry in enumerate(expiries['Expiry Date']):
            print(f"{i + 1}. {expiry}")
else:
        print(f"No expiry found for {instrument_name} {instrument_type} in {user_date}.")

# if data is not None:
#     print("\nFetched Data:")
#     print(data)
# else:
#     print("No data found.")



# from option_chain_spa import get_option_chain

# # Define the date you want to fetch data for
# fetch_date = "2024-03-14"
# instrument = "nifty"  # or "sensex"

# # Fetch the option chain data
# option_chain_df = get_option_chain(fetch_date, instrument)

# # Display the data
# if option_chain_df is not None:
#     print(option_chain_df)
# else:
#     print("No data available.")
