import pandas as pd
from sqlalchemy import create_engine

def load_data(df:pd.DataFrame)-> None:
    """ Loads data into a sqllite database"""
    disk_engine = create_engine('sqlite:///my_lite_stores.db')
    df.to_sql('cal_uni', disk_engine, if_exists='replace')
