#Imports for packages. When bundled as aplication this wont be equired
import sys
import subprocess
import pkg_resources
import time

required = {'myconfig'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Detected missing libraries, installing them using pip.")
    print("If this fails, check pip is installed and updated.")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from armors import *
from enemies import *
from guns import *
from fighting import fight
from myself import *
import os

clear = lambda: os.system("cls")

from os.path import exists as file_exists

#Read previous data and assign variables
#Check for previous save file.
if file_exists("data.py") == True:
    #print("Save file found, loading game data...")
    from data import *
    #save files not yet implemented

elif file_exists("data.py") == False:
    print("Save file not found, initializing fresh save.")
    #when finished, create template for new save.

stash = {
    "Roubles": 500000,
    "USD": 1000,
    "EUR": 500,
    paca: 1,
    mp5: 1    
}

clear()

fight(Scav(), "mefirst")