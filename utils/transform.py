import pandas as pd
import logging

def transform_data(data:dict) -> pd.DataFrame:
    """ Transforms the dataset into desired structure and filters"""

    df = pd.DataFrame(data)
    logging.info(f"Total Number of universities from API: {len(data)}")

    df = df[df["name"].str.contains("California")]
    logging.info(f"Number of universities in california: {len(df)}")
    
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    
    return df[["domains","country","web_pages","name"]]