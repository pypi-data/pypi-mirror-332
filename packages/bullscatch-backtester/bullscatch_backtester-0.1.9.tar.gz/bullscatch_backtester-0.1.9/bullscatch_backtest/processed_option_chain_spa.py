import pandas as pd
from bullscatch_backtest.option_chain_spa import get_option_chain

def fetch_and_process_option_chain(start_date: str, expiry_date: str, symbol: str) -> pd.DataFrame:
    """
    Fetches the option chain data and processes it with forward-filled timestamps.

    :param start_date: The date to fetch data for (YYYY-MM-DD format).
    :param expiry_date: The expiry date of the option contract (YYYY_MM_DD format).
    :param symbol: The symbol to fetch option chain data for (e.g., "nifty").
    :return: A processed pandas DataFrame with forward-filled timestamps.
    """
    option_chain_df = get_option_chain(start_date, expiry_date, symbol)

    # Convert timestamp column to pandas datetime format
    option_chain_df["timestamp"] = pd.to_datetime(option_chain_df["timestamp"])

    complete_dfs = []

    for (strike, option_type), group in option_chain_df.groupby(["strike", "option_type"]):
        # Generate a full range of timestamps at 1-second intervals
        all_timestamps = pd.date_range(start=group["timestamp"].min(), 
                                       end=group["timestamp"].max(), freq="s")
        
        timestamps_df = pd.DataFrame({"timestamp": all_timestamps})
        timestamps_df["strike"] = strike
        timestamps_df["option_type"] = option_type

        # Merge with original data and forward-fill missing values
        merged_df = pd.merge(timestamps_df, group, on=["timestamp", "strike", "option_type"], how="left")
        merged_df.ffill(inplace=True)

        complete_dfs.append(merged_df)

    # Combine all processed data into a single DataFrame
    final_option_chain_df = pd.concat(complete_dfs).reset_index(drop=True)
    
    return final_option_chain_df
