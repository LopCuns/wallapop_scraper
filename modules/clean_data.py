"""Limpiar los datos antes de hacer las analíticas"""
import pandas as pd
import modules.constants as ct
import os
def clean_data(data,filename):
  # Crear un nuevo directorio para guardar los datos
  directory_path = f'{ct.DATA_PATH}/{filename}'
  if not os.path.exists(directory_path):
      os.mkdir(directory_path)
  # Crear un archivo de excel con los datos si el precio del producto es mayor a 0$
  data[data['Price'] > 0].to_excel(excel_writer=f'{directory_path}/info.xlsx',index=False)