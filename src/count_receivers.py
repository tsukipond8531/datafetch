import GNSS as gs 
import base as b 
import os

year = 2019


def count_by_doy(
        year, 
        root = os.getcwd()
        ):
    
    out = {}
    
    for doy in range(1, 366):
        
        path = gs.paths(year, doy, root)
        
        df = b.load(path.fn_roti)
        
        out[doy] = df['sts'].unique()

    return out