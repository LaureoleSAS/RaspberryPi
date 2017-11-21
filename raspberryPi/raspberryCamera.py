from picamera import PiCamera
import os, sys

path = "/home/pi/Videos/"
nb_rep = 0
dirs = os.listdir(path)
for file in dirs:
	if '.h264' in file:
		nb_rep = nb_rep + 1

num_vid = nb_rep + 1
list = ["my","video", num_vid]

camera = PiCamera()
camera.resolution=(960,960)
camera.start_preview()
camera.start_recording('Videos/'+ list[0] + '_' + list[1] + '_' + str(list[2]) + '.h264')
camera.wait_recording(30)
camera.stop_recording()
camera.stop_preview()

os.system('sudo python raspberryCameraMp4.py')
