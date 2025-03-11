import pandas as pd
from processed_option_chain_spa import fetch_and_process_option_chain

def option_chain_atm(start_date: str, expiry_date: str, symbol: str, base_strike: int) -> pd.DataFrame:
    """
    Fetches, processes, and filters option chain data for a given base strike price,
    including 10 strikes up and down.

    :param start_date: The start date for fetching option chain data (YYYY-MM-DD).
    :param expiry_date: The expiry date of the options (YYYY_MM_DD).
    :param symbol: The trading symbol (e.g., 'nifty').
    :param base_strike: The central strike price to filter around.
    :return: A DataFrame with strike prices ranging from (base_strike - 10 steps) to (base_strike + 10 steps).
    """
    # Fetch processed option chain data
    option_chain_df = fetch_and_process_option_chain(start_date, expiry_date, symbol)

    # Ensure the DataFrame is not empty
    if option_chain_df.empty:
        print("No data fetched. Check the inputs or source data.")
        return pd.DataFrame()

    # Identify available unique strikes
    unique_strikes = sorted(option_chain_df['strike'].unique())

    # Ensure the base strike exists in the dataset
    if base_strike not in unique_strikes:
        print(f"Base strike {base_strike} not found in available strikes.")
        return pd.DataFrame()

    # Find the nearest strike interval
    strike_interval = min(abs(unique_strikes[i] - unique_strikes[i - 1]) for i in range(1, len(unique_strikes)))

    # Generate the strike range (10 strikes up & down)
    strike_range = [base_strike + (i * strike_interval) for i in range(-10, 11)]

    # Filter DataFrame for the computed strike range
    filtered_df = option_chain_df[option_chain_df['strike'].isin(strike_range)]
    
    return filtered_df
