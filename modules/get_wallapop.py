"""Python scraper"""

from playwright.sync_api import sync_playwright
import pandas as pd
from time import sleep
import os
import modules.constants as ct
def get_wallapop(product):
    with sync_playwright() as p:
      # Lanzar el navegador
      browser = p.chromium.launch()
      # Abrir la página
      page = browser.new_page()
      page.goto('https://wallapop.com/app')
      # Aceptar las cookies
      page.locator('#onetrust-accept-btn-handler').click()
      # Buscar el producto
      page.locator('[type=search]').fill(product)
      page.keyboard.press('Enter')
      # Obtener los precios, los títulos y los enlaces de las ofertas
      # Esperar a que carge la página
      sleep(4)
      titles = page.locator('.ItemCard__title').all_text_contents()
      prices = page.locator('.ItemCard__price').all_text_contents()
      urls = page.locator('.ItemCardList__item').all()
      products_info = [{ 
        'Title':product[0],
        'Price':float(product[1][:-2].replace('.','').replace(',','.')),
        'Url':product[2].get_attribute('href') }
       for product in zip(titles,prices,urls)
       ]
      # Clasificar la información en un pandas DataFrame
      products_df = pd.DataFrame(products_info)
      # Crear un nuevo directorio para guardar los datos
      directory_path = f'{ct.DATA_PATH}/{product.replace(" ","_")}'
      if not os.path.exists(directory_path):
        os.mkdir(directory_path)
      # Crear un archivo de excel con los datos
      products_df.sort_values(by='Price').to_excel(excel_writer=f'{directory_path}/info.xlsx',index=False)
