#from bidi.algorithm import get_display
#from matplotlib.ticker import FuncFormatter
#import matplotlib.pyplot as plt
from IPython.core.display import display, HTML
#import numpy as np
import pandas as pd
from io import StringIO
import os
#import requests


def read_table(url):
  return pd.read_csv(url, encoding='utf-8')
  
def filter_data(data, field, value, to_value=None):
    if str(value).isnumeric():
      value = int(value)
    if to_value is None:
        return data[data[field].eq(value)]
    else:
        if str(to_value).isnumeric():
          to_value = int(to_value)
        ge = data[data[field].ge(value)]
        return ge[ge[field].le(to_value)]

def print_column(data, field):
    print('\n'.join(data[field]))

def print_column_no_duplicates(data, field):
    print('\n'.join(data[field].unique()))

def print_top(data, count):
    data['link'] = data['link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    data.style.set_properties(**{'text-align': 'center'}).set_table_styles(  [{'selector': 'th', 'props': [('font-size', '16px'), ('text-align', 'center')]}])
    display(HTML(data.head(count).to_html(escape=False)))
   
def return_top(data, count):
    return data.head(count)

def count_data(data):
    return len(data)
 