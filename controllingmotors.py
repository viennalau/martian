import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for i in [18, 23, 24, 25]:
    GPIO.setup(i, GPIO.OUT)
    
def forward(fTurn):
    for i in range(512*fTurn):
        for i in [18, 23, 24, 25]:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.0015)
            GPIO.output(i, GPIO.LOW)
            time.sleep(0.0015)
            
def backward(bTurn):
    for i in range(512*bTurn):
        for i in [25, 24, 23, 18]:
            GPIO.output(i, GPIO.HIGH)
            time.sleep(0.0015)
            GPIO.output(i, GPIO.LOW)
            time.sleep(0.0015)
forward(3)
backward(3)
