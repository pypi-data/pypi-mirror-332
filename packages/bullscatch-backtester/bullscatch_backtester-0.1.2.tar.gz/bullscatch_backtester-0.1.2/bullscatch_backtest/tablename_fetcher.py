import psycopg2
import pandas as pd
from config import DB_CONFIG

def fetch_table_names():
    """Fetch all table names from the database and return as a DataFrame."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """)

        tables = cursor.fetchall()
        df_tables = pd.DataFrame(tables, columns=['Table Name'])

        cursor.close()
        conn.close()
        return df_tables

    except Exception as e:
        print(f"Error fetching table names: {e}")
        return None

def extract_expiry_dates(df_tables):
    """Extract expiry dates from table names."""
    nifty_options_table = df_tables[df_tables['Table Name'].str.contains(r'^nifty_.*_options$', case=False)].copy()
    sensex_options_table = df_tables[df_tables['Table Name'].str.contains(r'^sensex_.*_options$', case=False)].copy()


    nifty_options_table['Expiry Date'] = nifty_options_table['Table Name'].str.extract(r'_(\d{4}_\d{2}_\d{2})_options$')
    sensex_options_table['Expiry Date'] = sensex_options_table['Table Name'].str.extract(r'_(\d{4}_\d{2}_\d{2})_options$')

    return nifty_options_table, sensex_options_table

def get_expiry_type(date_str):
    """Determine whether the expiry is monthly ('m') or a specific weekly expiry."""
    date = pd.to_datetime(date_str, format='%Y_%m_%d')
    week_number = (date.day - 1) // 7 + 1  
    last_expiry = (date + pd.DateOffset(weeks=1)).month != date.month
    return 'm' if last_expiry else str(week_number)

def spot_table(df_tables):
    """Extract spot table name from table names."""
    nifty_spot_table = df_tables[df_tables['Table Name'].str.contains(r'^nifty_.*_spot$', case=False)].copy()
    sensex_spot_table = df_tables[df_tables['Table Name'].str.contains(r'^sensex_.*_spot$', case=False)].copy()
    return nifty_spot_table, sensex_spot_table