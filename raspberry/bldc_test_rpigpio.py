
#import RPi.GPIO as GPIO
import time

for dc in range(100, 110, 1):

    print("range:"+str(dc))
    time.sleep(0.3);


for dc in range(80, 100, 1):
    lc = 200 - dc
    print("range:"+str(lc))
    time.sleep(0.3);