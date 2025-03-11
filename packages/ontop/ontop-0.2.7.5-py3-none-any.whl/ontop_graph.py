
from bidi.algorithm import get_display
#from matplotlib.ticker import FuncFormatter
#import matplotlib.pyplot as plt
from IPython.core.display import display, HTML
import numpy as np
import pandas as pd
from io import StringIO
import os

diagram_data = []
savedFigCount = 0
def new_graph():
    global diagram_data
    diagram_data = []
    
def add_bar_to_graph(label, value):
   global diagram_data
    diagram_data = list(filter(lambda data: data['label'] != label, diagram_data))
    diagram_data.append({'label': label, 'value': value})

def draw_graph(title, x_title, center_title="", hidden=False):
    if hidden:
      %matplotlib auto
    else:
      %matplotlib inline

    global savedFigCount
    data = diagram_data
    fig, ax = plt.subplots(figsize=(15, 8))
    dff = pd.DataFrame(data=data, columns=['label', 'value'])
    dff.sort_values(by='value', ascending=False)

    colors = dict(zip(
        dff.label,
        ["#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f", "#eafb50", "#ff3333", "#ff9933", "#336600", "#99ff33", "#33ffff", "#3399ff", "#9933ff", "#ff66b2", "#a0a0a0", "#f7bb5f"]
    ))

    #print(dff)
    ax.barh(dff.label, dff.value, color=[colors[x] for x in dff.label])

    for i, (value, label) in enumerate(zip(dff.value, dff.label)):
        ax.text(0, i, get_display(label), size=14, weight=600, ha='right', va='bottom')
        ax.text(value, i, f'{value:,.0f}', size=14, ha='left', va='center')

    ax.text(1, 0.4, center_title, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, get_display(x_title), transform=ax.transAxes, size=12, color='#777777')
    # ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    # ax.xaxis.set_ticks_position('top')
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.15, get_display(title), transform=ax.transAxes, size=24, weight=600, ha='left', va='top')

    savedFigCount += 1
    plt.savefig('frame' + str(savedFigCount) + '.png', format='png')
    plt.show()
    
    
    
    
    
    
    
    
    
    