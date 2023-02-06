#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:35:43 2023

@author: josep
"""

import pandas as pd
import utils_visualize as uv
import datetime

# ---------------------
# 1. Index Price
# ---------------------

# Descargamos los datos de Eurostat y filtramos por país
url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/PRC_HPI_Q?format=SDMX-CSV'
df = pd.read_csv(url)
df = df[(df.geo == 'FR') | (df.geo == 'ES') | (df.geo == 'IT') | (df.geo == 'DE') | (df.geo == 'EA20')]

df_index = df[df.unit == 'I10_Q']


# filtramos por tipologíaT otal
df_total = df_index[df_index.purchase == 'TOTAL']

tl = 'House price index'
st1 = 'Total'
st2 = '2015 = 100 - Eurostat'

uv.lines_sns(df_total, tl, st1, st2)

# filtramos por tipología Nueva

df_nueva = df_index[df_index.purchase == 'DW_NEW']

tl = 'House price index'
st1 = 'Nueva'
st2 = '2015 = 100 - Eurostat'

uv.lines_sns(df_nueva, tl, st1, st2)

# filtramos por tipología Usada

df_segunda = df_index[df_index.purchase == 'DW_EXST']

tl = 'House price index'
st1 = 'Segunda mano'
st2 = '2015 = 100 - Eurostat'

uv.lines_sns(df_segunda, tl, st1, st2)

# Nos centramos en la variación de los últimos trimestres

df_rch_a = df[df.unit == 'RCH_A']
df_rch_a['fecha'] = pd.to_datetime(df_rch_a['TIME_PERIOD'])

today = datetime.datetime.now()
ano = today.year - 3

df_rch_a = df_rch_a.loc[df_rch_a['fecha'].dt.year > ano]
df_rch_a.OBS_VALUE = df_rch_a.OBS_VALUE.round(2)

tl = 'House price index'
st1 = 'Total'
st2 = 'Annual rate of change - Eurostat'

uv.bar_sns(df_rch_a, tl, st1, st2)

# ---------------------
# 2. Volumen compraventas
# ---------------------

# Descargamos los datos de Eurostat y filtramos por país
url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/PRC_HPI_HSVA?format=SDMX-CSV'
df = pd.read_csv(url)
df = df[df.unit == 'RCH_A_AVG']
df = df[df.TIME_PERIOD > 2016]

df = df[(df.geo == 'FR') | (df.geo == 'ES') | (df.geo == 'IT') | (df.geo == 'DE') | (df.geo == 'EA20')]

# filtramos por tipologíaT otal

tl = 'House sales index of number of transactions'
st1 = 'Total'
st2 = 'Annual average rate of change - Eurostat'

uv.bar_sns(df, tl, st1, st2)




