#Installing pip packages
required = {'myconfig'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Detected missing libraries, installing them using pip.")
    print("If this fails, check pip is installed and updated.")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import sys
import subprocess
import pkg_resources
from os.path import exists as file_exists

#Create starting game variables


while True:
    #Read previous data and assign variables
    
    #Check for previous save file.
    if file_exists("saves.txt") == True:
        pass
        #with open("saves.txt", 'r') as reader:

    elif file_exists("saves.txt") == False:
        print("Save file not found, initializing fresh save.")
        
    #Hideout