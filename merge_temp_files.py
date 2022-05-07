from astropy.table import Table, vstack, hstack
import os
import glob
import subprocess
import numpy as np
from astropy.io import ascii 
subprocess.call(["ls", "-l"])



subprocess.call(["rsync", "-avzhr", "--max-size=1.5m", "fireball2@fb-luna.astro.columbia.edu:/home/fireball2/data/",'/Users/Vincent/Nextcloud/LAM/FIREBALL/2022/temperatures'])

# rsync -avzhr --max-size=1.5m fireball2@fb-luna.astro.columbia.edu:"/home/fireball2/data/*" /Users/Vincent/Nextcloud/LAM/FIREBALL/2022/temperatures/
# time.sleep(4)
tables = []
tables_press = []
folders = glob.glob("/Users/Vincent/Nextcloud/LAM/FIREBALL/2022/temperatures/22*")
folders.sort()
n=3
for folder in folders[:]:
    print(folder)
    if os.path.isfile(folder + '/alltemps.csv'):
        temp = Table.read(folder + '/alltemps.csv')[::n]
        for col in temp.colnames[1:]:
            temp[col][0]=np.nan 
            temp[col][-1]=np.nan 
        tables.append(temp)


    if os.path.isfile(folder + '/pressure.csv'):
        pressure = Table.read(folder + '/pressure.csv')[::n]
        for col in pressure.colnames[1:]:
            pressure[col][0] = np.nan
            pressure[col][-1] = np.nan
        tables_press.append(pressure)

# tables_styack = vstack(tables,join_type='inner')
tables_styack = vstack(tables,join_type='outer')
tables_press_styack = vstack(tables_press)
# for col in tables_styack.colnames:
#     try:
#         tables_styack[col][(tables_styack[col]== np.ma.core.MaskedConstant).mask]=0#np.inf
#     except AttributeError:
#         pass
temp_path = '/Users/Vincent/Nextcloud/LAM/FIREBALL/2022/temperatures/all/alltemps.csv'
press_path = '/Users/Vincent/Nextcloud/LAM/FIREBALL/2022/temperatures/all/pressure.csv'
tables_styack.write(temp_path,overwrite=True,fill_values=[(ascii.masked, "NaN")])
tables_press_styack.write(press_path, overwrite=True, fill_values=[(np.nan, "null")])

import shutil
shutil.copy(press_path, "/Users/Vincent/Github/pyds9plugin-doc/docs/temperatures/pressure.csv")
shutil.copy(temp_path, "/Users/Vincent/Github/pyds9plugin-doc/docs/temperatures/alltemps.csv")


#%%
