import concurrent.futures
import time
from typing import Dict, Tuple, List, Union
from bullscatch_backtest.option_chain_spa import get_option_chain

class OptionDataFetcher:
    def __init__(self, max_workers: int = 10):
        """
        Initializes the OptionDataFetcher with a specified number of worker threads.
        """
        self.max_workers = max_workers

    def fetch_data(self, date_to_fetch: str, expiry_date: str) -> Tuple[Tuple[str, str], Union[dict, str]]:
        """
        Fetches option chain data for a given date and expiry.

        :param date_to_fetch: The date to fetch data for.
        :param expiry_date: The expiry date of the option contract.
        :return: A tuple containing (date, expiry) and the fetched data or an error message.
        """
        try:
            return (date_to_fetch, expiry_date), get_option_chain(date_to_fetch, expiry_date, "nifty")
        except Exception as e:
            return (date_to_fetch, expiry_date), f"Error: {e}"

    def fetch_all_data(self, date_expiry_pairs: List[Tuple[str, str]]) -> Dict[Tuple[str, str], Union[dict, str]]:
        """
        Fetches option chain data for multiple date-expiry pairs concurrently.

        :param date_expiry_pairs: List of tuples containing (date, expiry).
        :return: Dictionary mapping (date, expiry) to fetched data.
        """
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.fetch_data, date, expiry): (date, expiry) for date, expiry in date_expiry_pairs}
            
            for future in concurrent.futures.as_completed(futures):
                (date, expiry), data = future.result()
                results[(date, expiry)] = data
                print(f"Fetched data for {date} - {expiry}")
        
        return results
