import os
import imager as im 
import digisonde as dg




def get_closest_iono(fn_sky, iono_dir):
            
    files = os.listdir(iono_dir)
    
    iono_files = sorted(
        [dg.ionosonde_fname(fn) 
         for fn in files if 'PNG' in fn]
        )
    
    dn = min(iono_files, 
             key = lambda x: 
                 abs(x - im.imager_fname(fn_sky).datetime)
                 )
    
    code = files[0].split('_')[0]
        
    return dn.strftime(f"{code}_%Y%m%d(%j)%H%M%S.PNG")
