"""Python scraper"""

from playwright.sync_api import sync_playwright
import pandas as pd
from time import sleep
import os
import modules.constants as ct
def get_wallapop(product,category):
    with sync_playwright() as p:
      # Lanzar el navegador
      browser = p.chromium.launch()
      # Abrir la página
      page = browser.new_page()
      page.goto('https://wallapop.com/app')
      # Aceptar las cookies
      page.locator('#onetrust-accept-btn-handler').click()
      # Seleccionar categoría
      if category:
        page.locator('tsl-bubble').nth(1).click()
        page.get_by_text(category).click()
      # Buscar el producto 
      page.locator('[type=search]').fill(product)
      page.keyboard.press('Enter')
      # Obtener los precios, los títulos y los enlaces de las ofertas
      # Esperar a que carge la página
      sleep(4)
      # TODO tener en cuenta los selectores de cards largas (wide) ej. Coches,inmobiliaria...
      if page.locator('.ItemCardWide').all():
        titles = page.locator('.ItemCardWide__title').all_text_contents()
        prices = page.locator('.ItemCardWide__price').all_text_contents()
      else:  
        titles = page.locator('.ItemCard__title').all_text_contents()
        prices = page.locator('.ItemCard__price').all_text_contents()
      urls = page.locator('.ItemCardList__item').all()
      products_info = [{ 
        'Title':product[0],
        'Price':float(product[1].strip()[:-1].replace('.','').replace(',','.')),
        'Url':product[2].get_attribute('href') }
       for product in zip(titles,prices,urls)
       ]
      # Clasificar la información en un pandas DataFrame
      return pd.DataFrame(products_info)
