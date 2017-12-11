import os, sys

path = "/home/pi/Documents/Serveur/Videos/copy/"
dirs = os.listdir(path)

for file in dirs:
    if '.h264' in file:
        file_split = file.split('.')
        os.system('sudo MP4Box -add '+path+file+' '+path+file_split[0]+'.mp4')
        os.system('sudo rm ' + path + file)

for file in dirs:
    if '.mp4' in file:
        file_split = file.split('-')
        os.system('sudo cp ' + path + file + ' /home/pi/Documents/Serveur/Videos/'+ file_split[0] + '_' + file_split[1] + '/' + file)
        os.system('sudo rm ' + path + file)
