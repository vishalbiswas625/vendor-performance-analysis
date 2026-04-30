import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="C:/data/logs/ingestion.log",  #### logging use for knowing warnings:
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, engine):  ### to make database create function
    """This function will ingest dataframe into db table"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
    """Load CSVs and ingest into DB"""
    start = time.time()

    for file in os.listdir("C:/data"):
        if file.endswith('.csv'):
            df = pd.read_csv('C:/data/' + file)
    logging.info(f'Ingesting {file} in db')
    ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start) / 60

    logging.info(
        '---------Ingestion Complete-------')  ## [:-4 String slicing to find .csv charater slicing] (1st make db fuction then call )
    logging.info(f'Total time taken : {total_time} minutes')


if __name__ == '__main__':
    load_raw_data()