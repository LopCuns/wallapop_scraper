"""Build statistics of the products data"""
import os
import pandas as pd
import modules.constants as ct
def build_statistics():
    for filename in os.listdir(ct.DATA_DIR):
        ROOT = f'{ct.DATA_PATH}/{filename}'
        if os.path.exists(f'{ROOT}/statistics.xlsx'):
          continue
        df = pd.read_excel(f'{ROOT}/info.xlsx')
        df.describe().to_excel(excel_writer=f'{ROOT}/statistics.xlsx')
build_statistics()