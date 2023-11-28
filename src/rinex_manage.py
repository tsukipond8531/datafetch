import os 
import GNSS as gs
import base as b
from tqdm import tqdm 
import shutil 
import Webscrape as wb 

def year_from_fname(f):
    
    if '_' in f:
        ext = f.split('_')
        ext = ext[1].split('.')
        year_str = '20' + ext[1][:2]
    else:
        ext = f.split('.')
        year_str = '20' + ext[1][:2]
        
        
    doy = ext[0][-4:-1]
    
    return doy, year_str


def move_rinex_files(PATH_IN):
    for year in os.listdir(PATH_IN)[1:]:
        year_path = os.path.join(PATH_IN, year)

        for doy in tqdm(os.listdir(year_path), year):
            doy_path = os.path.join(year_path, doy)
            path = gs.paths(year, doy)

            for rinex_f in os.listdir(doy_path):
                move_rinex_file(doy_path, rinex_f, path.rinex)

def move_rinex_file(source_dir, rinex_filename, destination_dir):
    b.make_dir(destination_dir)

    src = os.path.join(source_dir, rinex_filename)
    dst = os.path.join(destination_dir, rinex_filename)

    try:
        shutil.move(src, dst)
    except Exception as e:
        print(f"Error moving {rinex_filename}: {str(e)}")

def remove_bad(file_path):
    # 1 KB = 1024 bytes
    file_size = os.path.getsize(file_path) 
    
    if (file_size == 162):
        os.remove(file_path)

def move_files(PATH_IN):
    
    for file in os.listdir(PATH_IN):
        
        file_path = os.path.join(
            PATH_IN, 
            file
            )
        
        doy, year = year_from_fname(file)      
        
        path = gs.paths(
            int(year), 
            int(doy)
            )
                    
        dst = path.rinex
        
        b.make_dir(dst)
        print(file)
        shutil.move(file_path, dst)
       
        
      
PATH_IN = 'D:\\database\\GNSS\\rinex\\bolivia\\tmp5XTjSG\\'

def unzip_and_convert(PATH_IN):
    for file in os.listdir(PATH_IN):
        
        file_path = os.path.join(
            PATH_IN, 
            file
            )
        
        try:
            if file.endswith('Z'):
                print(file)
                file_out = wb.unzip_Z(file_path)
                wb.crx2rnx(file_out)
                
                
            elif file.endswith('zip'):
                print(file)
                file_out = wb.unzip_ZIP(file_path)
                wb.crx2rnx(file_out)
            
        except:
            print(file_path, 'doest work')
            continue
            
        


def run(year = 2021, root = 'D:\\'):
    
    print('[check unzipped rinex]', year)
    
    
    for doy in tqdm(range(1, 315)):
        
        PATH_IN = gs.paths(
            year, doy, root
            ).rinex
        
        unzip_and_convert(PATH_IN)
        
# run(year = 2023)
