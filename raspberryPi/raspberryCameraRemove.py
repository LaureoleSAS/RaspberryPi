import os, sys

path="/home/pi/Videos/"
dirs = os.listdir(path)

for file in dirs:
	if '.h264' in file:
		os.remove('/home/pi/Videos/' + file)
