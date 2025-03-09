import psycopg2
import pandas as pd
from config import DB_CONFIG

def execute_query(table_name, fetch_date):
    """Execute a query to fetch data from a given table on a specified date."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = f"SELECT * FROM {table_name} WHERE timestamp::date = '{fetch_date}' LIMIT 10;"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert to DataFrame
        df_data = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
        spot = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])


        cursor.close()
        conn.close()
        return df_data, spot

    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def spot_query(table_name, input_date):
    """Execute a query to fetch spot data for a given instrument on a specified date."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Use double quotes for case-sensitive table names
        spot_query = f'SELECT * FROM "{table_name}" WHERE timestamp::date = %s LIMIT 10;'
        cursor.execute(spot_query, (input_date,))  # Use parameterized query for safety
        rows = cursor.fetchall()

        # Convert to DataFrame
        spot_data = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

        cursor.close()
        conn.close()
        return spot_data

    except Exception as e:
        print(f"Error executing query: {e}")
        return None
