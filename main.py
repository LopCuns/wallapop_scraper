"""Main program"""

from modules.get_wallapop import get_wallapop
from modules.build_statistics import build_statistics
from modules.clean_data import clean_data
from modules.categories import cat
def build_wallapop(*products,category=None):
  """Build wallapop info and stats"""
  for product in products:
      df = get_wallapop(product,cat.get(category,None))
      filename = product.replace(' ','_')
      clean_data(df,filename)
      build_statistics(filename)
build_wallapop('vestido rosa',category='Moda')