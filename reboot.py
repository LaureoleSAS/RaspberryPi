import os, sys
from datetime import time, datetime

mtn = datetime.now()
hour = mtn.hour
min = mtn.minute
sec = mtn.second

while 1:
    if hour == 2 and min == 00 and sec == 00:
        os.system('sudo reboot')