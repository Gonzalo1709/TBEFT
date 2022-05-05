from os.path import exists as file_exists

#Create starting game variables


while True:
    #Read previous data and assign variables
    
    #Check for previous save file.
    if file_exists("saves.txt") == True:
        pass
        with open("saves.txt", 'r') as reader:

    elif file_exists("saves.txt") == False:
        print("Save file not found, initializing fresh save.")
        
    #Hideout
