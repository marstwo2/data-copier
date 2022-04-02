import os
import sys

from read import get_json_reader
from write import load_db_table


def process_tables(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])

def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(' ')
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    for table_name in table_names:
        process_tables(BASE_DIR, conn, table_name)

if __name__ == "__main__":
    main()



# def get_json_reader(BASE_DIR, table_name, chunksize=1000):
#     file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
#     fp = f'{BASE_DIR}/{table_name}/{file_name}'
#     return pd.read_json(fp, lines=True, chunksize=chunksize)


# if __name__ == '__main__':
#     # This code will only run when we run the program.
#     # When we import, the program will not run.
#     BASE_DIR = os.environ.get('BASE_DIR')
#     table_name = os.environ.get('TABLE_NAME')
#     json_reader = get_json_reader(BASE_DIR, table_name)
#     for idx, df in enumerate(json_reader):
#         print(f'Number of records in chunk with index {idx} is {df.shape[0]}')


# # BASE_DIR = '/home/jshernandez05/Projects/data-copier/data/retail_db_json'
# # table_name = 'order_items'
# # file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
# # fp = f'{BASE_DIR}/{table_name}/{file_name}'

# # conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'

# # def main():
# #     df = pd.read_json(fp, lines=True)
# #     print(df.dtypes)

# if __name__ == "__main__":
#     main()
