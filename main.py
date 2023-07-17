"""Main program"""

from modules.get_wallapop import get_wallapop
from modules.build_statistics import build_statistics
def build_wallapop(*products):
  """Build wallapop info and stats"""
  for product in products:
      get_wallapop(product)
  # TODO liampiar los datos
  build_statistics()

build_wallapop()