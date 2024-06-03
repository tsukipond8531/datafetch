import os 
import shutil
from tqdm import tqdm 
import base as b 
import datetime as dt
import core as c 

infile = 'D:/ionograms/07/'

def copy_all_in_folder(infile):
    
    for folder in tqdm(os.listdir(infile)):
        
        path_out = os.path.join(infile, folder[-1])
        b.make_dir(path_out)
        path_folder = os.path.join(infile, folder)
        
        if 'B' in folder:
        
            for file in os.listdir(path_folder):
                src = os.path.join(path_folder, file)
                dst = os.path.join(path_out, file)
                
                if file.endswith('SAO'):
                    shutil.copy(src, dst)
                    
                    

def copy_by_dates(dates, site):
    
    PATH =  'database/ionogram/'

    b.make_dir(f'{PATH}/{site}')
    
    
    for dn in dates:
        
        folder = dn.strftime(f'%Y%m%d{site}')
        
        path_out = os.path.join(PATH, folder[-1])
        
        path_folder = os.path.join(PATH, folder)
        
        t = dn.strftime('%m/%d')
        
        for file in tqdm(os.listdir(path_folder), t):
            src = os.path.join(path_folder, file)
            dst = os.path.join(path_out, file)
            
            if file.endswith('SAO'):
                try:
                    shutil.copy(src, dst)
                except:
                    continue 
                
# for site in ['S', 'B']:
    
date = dt.date(2015, 12, 20)

dates = c.undisturbed_days(date, threshold = 18).index 


site = 'B'

copy_by_dates(dates, site)