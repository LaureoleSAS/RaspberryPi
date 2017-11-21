import os, sys

path = "/home/pi/Videos/"
dirs = os.listdir(path)

for file in dirs:
	file_split = file.split('.')
	if '.h264' in file:
		os.system('MP4Box -add Videos/' + file + ' ' + 'Videos/' + file_split[0] + '.mp4')

os.system('sudo python raspberryCameraRemove.py')
