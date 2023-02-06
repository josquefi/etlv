#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:04:18 2023

@author: josep
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


sns.set(rc={'figure.figsize':(15,10)})
#sns.color_palette("viridis", as_cmap=True)
sns.set_palette("cubehelix")
sns.set_style("darkgrid")

def lines_sns(df, titol, subtitol, subtitol2):
    '''Realiza un gráfico de líneas para las columnas llamadas var de los 4 dataframes '''

    
    fig, ax = plt.subplots()
    
    sns.lineplot(data=df, y='OBS_VALUE', x='TIME_PERIOD', hue='geo', errorbar=None)

    ax.legend()
    
    ax.text(x=0.5, y=1.1, s=titol, fontsize=25, weight='bold', ha='center', va='bottom', transform=ax.transAxes)
    ax.text(x=0.5, y=1.05, s=subtitol, fontsize=18, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes)
    ax.text(x=0.5, y=1, s=subtitol2, fontsize=18, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes)    

    ax.set_xlabel('')
    ax.set_ylabel('')
    
    ax.xaxis.set_major_locator(plt.MaxNLocator(45))
    plt.xticks(rotation=90, ha='right')
    
    plt.tight_layout()
    
    salvar = 'grafics/graf_{}_{}.png'.format(titol, subtitol)
    plt.savefig(salvar)   


def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

    
def bar_sns(df, titol, subtitol, subtitol2):
    '''Realiza un gráfico de barras para las columnas llamadas var de los 4 dataframes '''

    
    fig, ax = plt.subplots()
    
    ax = sns.barplot(data=df, x="TIME_PERIOD", y="OBS_VALUE", hue="geo", errorbar=None)
    show_values(ax)


    ax.legend()
    
    ax.text(x=0.5, y=1.1, s=titol, fontsize=25, weight='bold', ha='center', va='bottom', transform=ax.transAxes)
    ax.text(x=0.5, y=1.05, s=subtitol, fontsize=18, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes)
    ax.text(x=0.5, y=1, s=subtitol2, fontsize=18, alpha=0.75, ha='center', va='bottom', transform=ax.transAxes)    

    ax.set_xlabel('')
    ax.set_ylabel('')
    
    
    plt.tight_layout()
    
    salvar = 'grafics/graf_{}_{}.png'.format(titol, subtitol)
    plt.savefig(salvar)   