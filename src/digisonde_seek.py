import os 
import shutil
from tqdm import tqdm 
import base as b 


infile = 'D:/ionograms/07/'


for folder in tqdm(os.listdir(infile)):
    
    path_out = os.path.join(infile, folder[-1])
    b.make_dir(path_out)
    path_folder = os.path.join(infile, folder)
    
    for file in os.listdir(path_folder):
        src = os.path.join(path_folder, file)
        dst = os.path.join(path_out, file)
        
        if file.endswith('SAO'):
            shutil.copy(src, dst)