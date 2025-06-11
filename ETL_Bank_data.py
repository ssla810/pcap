# Code for ETL operations on Top 10 bank data

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

# Extracting bank data from URL
def extract(url, table_columns):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # Find all wikitable tables
    tables = soup.find_all('table', {'class': 'wikitable'})

    # Find the correct table - assuming it's the first or second one
    bank_table = tables[0]

    df = pd.DataFrame(columns=table_columns)

    for row in bank_table.find_all('tr')[1:]:  # skip header row
        cols = row.find_all('td')
        if len(cols) >= 3:
            name = cols[1].text.strip()
            assets_str = cols[2].text.strip().replace(',', '')
            try:
                assets = float(assets_str)
            except:
                continue
            data = {
                'Name': name,
                'MC_USD_BILLION': assets
            }
            df1 = pd.DataFrame([data])
            df = pd.concat([df, df1], ignore_index=True)

    # Top 10 banks only
    df = df.head(10)
    return df

#  Transform Data
def transform_data(df, exchange_rate_csv):
    # Read exchange rates
    rates_df = pd.read_csv(exchange_rate_csv)
    rates = dict(zip(rates_df['Currency'], rates_df['Rate']))

    # Convert and add new columns
    df['MC_GBP_Billion'] = (df['MC_USD_BILLION'] * rates['GBP']).round(2)
    df['MC_EUR_Billion'] = (df['MC_USD_BILLION'] * rates['EUR']).round(2)
    df['MC_INR_Billion'] = (df['MC_USD_BILLION'] * rates['INR']).round(2)
    print(df.columns)
    return df

# Load to CSV
def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

# Load to Database
def load_to_db(df, db, table_nm):
    conn = sqlite3.connect(db)
    df.to_sql(table_nm, conn, if_exists='replace', index=False)
    conn.close()

# Run SQL Queries
def run_queries(db_nm):
    conn = sqlite3.connect(db_nm)

    # a. London (GBP)
    print("\nLondon Office:")
    print(pd.read_sql_query("SELECT Name, MC_GBP_Billion FROM TopBanks", conn))

    # b. Berlin (EUR)
    print("\nBerlin Office:")
    print(pd.read_sql_query("SELECT Name, MC_EUR_Billion FROM TopBanks", conn))

    # c. New Delhi (INR)
    print("\nNew Delhi Office:")
    print(pd.read_sql_query("SELECT Name, MC_INR_Billion FROM TopBanks", conn))

    conn.close()

# setup logfile
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./etl_bank_log.txt","a") as f:
        f.write(timestamp + ' : ' + message + '\n')

# Run ETL process
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
columns = ['Name','MC_USD_BILLION']
exchange_csv = 'C:/Users/SSL/PyCharmProjects/DE_course_exc/exchange_rates.csv'
transformed_data_csv = './Top 10 Banks data.csv'
db_name = 'Banks_data.db'
table_name = 'TopBanks'

log_progress("ETL process started.")

df_extracted = extract(url,columns)
log_progress('Data extracted successfully.')

df_transformed = transform_data(df_extracted,exchange_csv)
log_progress('Data transformed successfully.')

load_to_csv(df_transformed,transformed_data_csv)
log_progress(f"Data loaded to CSV: {transformed_data_csv}")

load_to_db(df_transformed,db_name,table_name)
log_progress(f"Data loaded to database: {db_name}")

run_queries(db_name)
log_progress("Running SQL queries...")

log_progress("ETL process completed.")

