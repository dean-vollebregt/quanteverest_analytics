import pandas as pd
from numpy import array

def prepare_brent():
    brent = pd.read_csv('./data/brent.csv').iloc[::-1]
    brent = brent['WCOILBRENTEU'].values[::-1]
    return array(brent[-200:])

def prepare_woodside():
    woodside = pd.read_csv('./data/WPL.csv')
    woodside = woodside['close'].values[::-1]
    return array(woodside[-200:])


