import os 
import Webscrape as wb 
from base import make_dir
import shutil
import GNSS as gs
from tqdm import tqdm 


def unzip_and_convert(dst):
    
    for fname in os.listdir(dst):
        print('[unziping]', fname)
        
        try:
            wb.unzip_orbit(dst + fname)
          
        except:
            pass
    
    for file in os.listdir(dst):
        print('[converting]', file)
        wb.crx2rnx(dst + file)
 


def get_year_doy(filename):
    ars = filename.split('.')
    year = int('20' + ars[1][:2])
    doy = int(ars[0][4:-1])

    return year, doy


def copy_from_dst(src):

    for filename in os.listdir(src):
    
        year, doy = get_year_doy(filename)
        
        dst = gs.paths(year, doy).rinex
        make_dir(dst)
        print('[copying]', filename)
        shutil.copy(src + filename, 
                    os.path.join(dst, filename))
        


def get_sao_date(fname):
    
    arg = fname.split('_')[-1][:-4]
    
    year = int(arg[:4])
    doy = int(arg[4:])
    return gs.date_from_doy(year, doy)


    
yr = 2014
    
src = f'D:\\database\\jic\\sao{yr}\\'
dst = 'D:\\database\\jic\\temp\\'

def run_files(month_path, dst ):

    for filename in os.listdir(month_path):
        src_in = os.path.join(month_path, filename)
        shutil.copy(src_in, dst)

for folder in tqdm(os.listdir(src), str(yr)):
    
    if folder == '02':
        pass
    else:
        month_path = os.path.join(
            src, folder
            )
        
        run_files(month_path, dst)
            
        
                
 