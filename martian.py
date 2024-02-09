import time
import RPi.GPIO as GPIO
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)
camera = PiCamera()
camera.rotation = 180
char_amt = 0

# Key = Letter
# Value = amount of beeps and the LED color
martian_dict = {
  "A": [0, "red"],
  "B": [0, "orange"],
  "C": [0, "yellow"],
  "D": [0, "green"],
  "E": [0, "blue"],
  "F": [0, "purple"],
  "G": [1, "red"],
  "H": [1, "orange"],
  "I": [1, "yellow"],
  "J": [1, "green"],
  "K": [1, "blue"],
  "L": [1, "purple"],
  "M": [2, "red"],
  "N": [2, "orange"],
  "O": [2, "yellow"],
  "P": [2, "green"],
  "Q": [2, "blue"],
  "R": [2, "purple"],
  "S": [3, "red"],
  "T": [3, "orange"],
  "U": [3, "yellow"],
  "V": [3, "green"],
  "W": [3, "blue"],
  "X": [3, "purple"],
  "Y": [4, "red"],
  "Z": [4, "orange"],
}

### Regular LED Setup ###

## LED setup for the regular LEDs used in encoding ##

# Red
GPIO.setup(4, GPIO.OUT)
red = GPIO.PWM(4, 5)

# Yellow
GPIO.setup(21, GPIO.OUT)
yellow = GPIO.PWM(21, 5)

# Green
GPIO.setup(6, GPIO.OUT)
green = GPIO.PWM(6, 5)

# Blue
GPIO.setup(16, GPIO.OUT)
blue = GPIO.PWM(16, 5)

## LED setup for the flashing red/green LEDs ##
# Red
GPIO.setup(26, GPIO.OUT)
red_bad = GPIO.PWM(26, 75)

# Green
GPIO.setup(22, GPIO.OUT)
green_good = GPIO.PWM(22, 100)

## Buzzer Setup ##
GPIO.setup(20, GPIO.OUT)
buzzer = GPIO.PWM(20, 5)
buzzer.start(0)
buzzer.ChangeDutyCycle(0)

## Multicolor LED Setup for encoding ##

## Orange LED
# Red
GPIO.setup(27, GPIO.OUT)
orange_red_multi = GPIO.PWM(27, 75)
orange_red_multi.start(0)

# Green
GPIO.setup(12, GPIO.OUT)
orange_green_multi = GPIO.PWM(12, 75)
orange_green_multi.start(0)

# Blue
GPIO.setup(19, GPIO.OUT)
orange_blue_multi = GPIO.PWM(19, 75)
orange_blue_multi.start(0)

# Multicolor LED Setup - Purple

# Red
GPIO.setup(17, GPIO.OUT)
purple_red_multi = GPIO.PWM(17, 75)
purple_red_multi.start(0)

# Blue
GPIO.setup(5, GPIO.OUT)
purple_blue_multi = GPIO.PWM(5, 75)
purple_blue_multi.start(0)

# Associates the color with a GPIO pin turns the LED on
color_dict = {
  "red": [4, GPIO.HIGH],
  "orange": [100, 5, 0],
  "yellow": [21,GPIO.HIGH],
  "green": [6, GPIO.HIGH],
  "blue": [16, GPIO.HIGH],
  "purple": [50, 0, 50]
}

#Takes a message and passes it to encode_message
def send_message():
  message = input("Enter message: ").upper()
  print(f"Your message is {message}")
  bad()
  encode_message(message)
  good()
  print("Message sent!")

# Takes in the message, and for every character in the message it finds its corresponding value in color_dict to translate it into colors and beeps.
# Then, beeps a certain amount and sets the LED color
def encode_message(message):
  global martian_dict
  global color
  global char_amt
  global beep_amt
  encoding = True
  while encoding == True:
    for char in message:
      if char_amt < len(message):
        if char in martian_dict:
          print(' ')
          print(char)
          print(martian_dict[char])
          beep_amt = martian_dict[char][0]
          color = martian_dict[char][1]
          beep_controller(beep_amt)
          set_LED(color)
          time.sleep(2.5)
          char_amt += 1
          continue
        elif char == " ":
          char_amt += 1
          time.sleep(5)
          continue
        else: 
          print("Error: Invalid character")
      elif char_amt >= len(message):
        print("Message encoding complete.")
        char_amt = 0
        encoding = False
        break
        
# Turns the buzzer on and off
def beep_controller(beep_amt):
  for i in range(beep_amt):
    buzzer.ChangeDutyCycle(15)
    time.sleep(0.2)
    buzzer.ChangeDutyCycle(0)
    time.sleep(0.2)
    
# Changes the LED color
def set_LED(color):
  global color_dict
  # These specific colors are here because they are single LEDs and not multicolor
  if color in ("red", "yellow","green", "blue"):
    pin = color_dict[color][0]
    state = color_dict[color][1]
    GPIO.output(pin, state)
    print("LED set to " + color)
    time.sleep(2.5)
    GPIO.output(pin, GPIO.LOW)
    
  # These are multicolor LEDs so we have to use ChangeDutyCycle instead of GPIO.output
  elif color in ("orange", "purple"):
      if color == "orange":
          orange_red_multi.ChangeDutyCycle(color_dict[color][0])
          orange_green_multi.ChangeDutyCycle(color_dict[color][1])
          time.sleep(2.5)
          orange_red_multi.ChangeDutyCycle(0)
          orange_green_multi.ChangeDutyCycle(0)          
      elif color == "purple":
          purple_red_multi.ChangeDutyCycle(color_dict[color][0])
          purple_blue_multi.ChangeDutyCycle(color_dict[color][2])
          time.sleep(2.5)
          purple_red_multi.ChangeDutyCycle(0)
          purple_blue_multi.ChangeDutyCycle(0)
      print("LED set to " + color)
  else:
    print("Color not found")
    

### Camera Commands ###

## Live Camera ##
def live_camera():
  camera.start_preview(fullscreen=False, window=(100, 20, 640, 380))  
  time.sleep(1) 
  input("Press enter to stop live viewing: ")
  camera.stop_preview()

# If the Freshmen are doing well
def good():
  for i in range(0,5):
    time.sleep(.5)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(22, GPIO.LOW)

# If the Freshmen are doing bad
def bad():
  for i in range(0,8m):
    time.sleep(.25)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(.25)
    GPIO.output(26, GPIO.LOW)
  
programOn = True
while programOn == True:
  print("-----------------------------------------------------")
  print("Command List: Message, Camera, Exit, Good, Bad")
  command = input("Enter command: ")
  if command.title() == "Message":
      send_message()
  elif command.title() == "Camera":
      camera_commands = True
      while camera_commands == True:
          print("-----------------------------------------------------")
          print("Camera Commands: Live, Exit")
          cam_command = input("Enter camera command: ")
          if cam_command.title()  == "Live":
              live_camera()
          elif cam_command.title() == "Exit":
              camera_commands = False
          else:
              print("Invalid command.")
  elif command == "Exit":
      programOn = False
  elif command.title() == "Good":
      good()
  elif command.title() == "Bad":
      bad()
  else:
      print("Invalid command.")

