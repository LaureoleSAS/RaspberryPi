import os, sys

path = "/home/pi/Documents/Serveur/Videos/copy/"
dirs = os.listdir(path)

for file in dirs:
    if '.mp4' in file:
        nom_split = file.split('-')
        os.system('sudo cp '+ path + file + ' /home/pi/Documents/Serveur/Videos/'+nom_split[0]+'_'+nom_split[1]+'/')
        os.system('sudo rm ' + file)
    if '.h264' in file:
        os.system('sudo rm ' + file)