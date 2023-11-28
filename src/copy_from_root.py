import GNSS as gs 
import os
import shutil 
from tqdm import tqdm 

def run_years():
    
    for year in range(2013, 2019):
        ...
    
def copy_file(dst, src, sts):
    
    try:
        dst1 = dst.fn_rinex(sts[:4], index = 0)
        src1 = src.fn_rinex(sts[:4], index = 0)
        
        shutil.copy(src1, dst1)
    except:
        dst1 = dst.fn_rinex(sts[:4], index = 1)
        src1 = src.fn_rinex(sts[:4], index = 1)
        
        shutil.copy(src1, dst1)
         
         
def run_by_year(year):
    

    for doy in tqdm(range(1, 366, 1), str(year)):

        dst = gs.paths(year, doy, root = 'F:\\')
        src = gs.paths(year, doy)
        
        
        
        try:
            for sts in os.listdir(src.rinex):
                                
                try:
                   copy_file(dst, src, sts)
                        
                except:
                    continue
        except:
            continue 
    
# run_by_year(2022)