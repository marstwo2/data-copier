import os
import sys

import pandas as pd

print(sys.executable)
print('test 2')
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
