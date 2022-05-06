#Installing pip packages
import sys
import subprocess
import pkg_resources

required = {'myconfig'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Detected missing libraries, installing them using pip.")
    print("If this fails, check pip is installed and updated.")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from os.path import exists as file_exists


#Read previous data and assign variables
#Check for previous save file.
if file_exists("data.py") == True:
    print("Save file found, loading game data...")
    from data import *

elif file_exists("data.py") == False:
    print("Save file not found, initializing fresh save.")
    #when finished, create template for new save.

