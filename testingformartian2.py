import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Regular LED Setup

GPIO.setup(4, GPIO.OUT)
red = GPIO.PWM(4, 5)

GPIO.setup(21, GPIO.OUT)
yellow = GPIO.PWM(21, 5)


GPIO.setup(6, GPIO.OUT)
green = GPIO.PWM(6, 5)

GPIO.setup(16, GPIO.OUT)
blue = GPIO.PWM(16, 5)


# # Buzzer Setup
# GPIO.setup(20, GPIO.OUT)
# buzzer = GPIO.PWM(20, 5)
# buzzer.start(0)
# buzzer.ChangeDutyCycle(0)
# 
# Multicolor LED Setup - Orange
GPIO.setup(17, GPIO.OUT)
orange_red_multi = GPIO.PWM(17, 75)
orange_red_multi.start(0)

GPIO.setup(19, GPIO.OUT)
orange_green_multi = GPIO.PWM(19, 75)
orange_green_multi.start(0)

GPIO.setup(5, GPIO.OUT)
orange_blue_multi = GPIO.PWM(5, 75)
orange_blue_multi.start(0)

# Multicolor LED Setup - Purple

GPIO.setup(12, GPIO.OUT)
purple_red_multi = GPIO.PWM(12, 75)
purple_red_multi.start(0)

GPIO.setup(13, GPIO.OUT)
purple_blue_multi = GPIO.PWM(13, 75)
purple_blue_multi.start(0)
# 
# color_dict = {
#   "red": ['gpioPinHere', 'GPIO.HIGH'],
#   "orange": ['gpioPinHere', '[100, 100, 0]'],
#   "yellow": ['gpioPinHere', 'GPIO.HIGH'],
#   "green": ['gpioPinHere', 'GPIO.HIGH'],
#   "blue": ['gpioPinHere', 'GPIO.HIGH'],
#   "purple": ['gpioPinHere', '[100, 0, 100]']
# }
# 
# # Starts the multicolor LED

def turn_on_LEDS():
    purple_red_multi.ChangeDutyCycle(50)
    purple_blue_multi.ChangeDutyCycle(50)

    orange_red_multi.ChangeDutyCycle(50)
    orange_green_multi.ChangeDutyCycle(30)
    orange_blue_multi.ChangeDutyCycle(0)

    GPIO.output(4, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)

def turn_off_LEDS():
    purple_red_multi.ChangeDutyCycle(0)
    purple_blue_multi.ChangeDutyCycle(0)

    orange_red_multi.ChangeDutyCycle(0)
    orange_green_multi.ChangeDutyCycle(0)
    orange_blue_multi.ChangeDutyCycle(0)

    GPIO.output(4, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    
# turn_on_LEDS()
# turn_off_LEDS()