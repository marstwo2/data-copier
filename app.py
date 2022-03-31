import os
import pandas as pd

BASE_DIR = '/home/jshernandez05/Projects/data-copier/data/retail_db_json'
table_name = 'order_items'
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp = f'{BASE_DIR}/{table_name}/{file_name}'

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'

def main():
    df = pd.read_json(fp, lines=True)
    print(df.dtypes)

if __name__ == "__main__":
    main()