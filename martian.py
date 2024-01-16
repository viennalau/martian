import time
import RPi.GPIO as GPIO
from picamera import PiCamera
GPIO.setmode(GPIO.BCM)

char_amt = 0
camera.rotation = 180

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
  "Back": [4, "yellow"],
  "Forward": [4, "green"],
  "Left": [4, "blue" ],
  "Right": [4, "purple"]
}

#Regular LED Setup

#LED setup for the regular LEDs used in encoding
GPIO.setup(4, GPIO.OUT)
red = GPIO.PWM(4, 5)

GPIO.setup(21, GPIO.OUT)
yellow = GPIO.PWM(21, 5)

GPIO.setup(6, GPIO.OUT)
green = GPIO.PWM(6, 5)

GPIO.setup(16, GPIO.OUT)
blue = GPIO.PWM(16, 5)

# LED setup for the flashing red/green LEDs
GPIO.setup(26, GPIO.OUT)
red_bad = GPIO.PWM(26, 5)

GPIO.setup(22, GPIO.OUT)
green_good = GPIO.PWM(22, 5)

# Buzzer Setup
GPIO.setup(20, GPIO.OUT)
buzzer = GPIO.PWM(20, 5)
buzzer.start(0)
buzzer.ChangeDutyCycle(0)


# Multicolor LED Setup for encoding - Orange
GPIO.setup(17, GPIO.OUT)
orange_red_multi = GPIO.PWM(17, 75)
orange_red_multi.start(0)

GPIO.setup(19, GPIO.OUT)
orange_green_multi = GPIO.PWM(19, 75)
orange_green_multi.start(0)

GPIO.setup(5, GPIO.OUT)
orange_blue_multi = GPIO.PWM(5, 75)
orange_blue_multi.start(0)

# Multicolor LED Setup for encoding - Purple

GPIO.setup(12, GPIO.OUT)
purple_red_multi = GPIO.PWM(12, 75)
purple_red_multi.start(0)

GPIO.setup(13, GPIO.OUT)
purple_blue_multi = GPIO.PWM(13, 75)
purple_blue_multi.start(0)




color_dict = {
  "red": [4, 'GPIO.HIGH'],
  "orange": [50, 30, 0],
  "yellow": [21,'GPIO.HIGH'],
  "green": [6, 'GPIO.HIGH'],
  "blue": [16, 'GPIO.HIGH'],
  "purple": [50, 0, 50]
}



def send_message():
  message = input("Enter message: ").upper()
  print(f"Your message is {message}")
  encode_message(message)
  print("Message sent!")

def encode_message(message):
  global martian_dict
  global color
  global char_amt
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
          time.sleep(3.5)
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
        encoding = False
        break
  
def beep_controller(beep_num):
  for i in range(beep_num):
    buzzer.ChangeDutyCycle(50)
    buzzer.ChangeDutyCycle(0)
    print(f"Beep {i+1}")
    
    time.sleep(0.5)

def set_LED(color):
  global color_dict
  if color in ("red", "yellow","green", "blue"):
    pin = color_dict[color][0]
    state = color_dict[color][1]
    GPIO.output(pin, state)
    print(pin,state)
    print("LED set to " + color)
  elif color in ("orange", "purple"):
      color_fullname_red =  color + "_red_multi"
      color_fullname_green = color + "_green_multi"
      color_fullname_blue = color + "_blue_multi"
      color_fullname_red.ChangeDutyCycle(color[0])
      color_fullname_green.ChangeDutyCycle(color[1])
      color_fullname_blue.ChangeDutyCycle(color[2])
      print("LED set to " + color)
  else:
    print("Color not found")
    

### Camera Commands ###

#Live Camera
def live_camera():
  camera.start_preview(fullscreen=False, window=(100, 20, 640, 380))  
  time.sleep(1) 
  input("Press enter to stop live viewing: ")
  camera.stop_preview()
  

# Rotate Camera
def rotate_camera():
  for i in [18, 23, 24, 25]:
    GPIO.setup(i, GPIO.OUT)

  # Forward Turn
  def forward(fTurn):
      for i in range(512*fTurn):
          for i in [18, 23, 24, 25]:
              GPIO.output(i, GPIO.HIGH)
              time.sleep(0.0015)
              GPIO.output(i, GPIO.LOW)
              time.sleep(0.0015)

  # Backward Turn            
  def backward(bTurn):
      for i in range(512*bTurn):
          for i in [25, 24, 23, 18]:
              GPIO.output(i, GPIO.HIGH)
              time.sleep(0.0015)
              GPIO.output(i, GPIO.LOW)
              time.sleep(0.0015)
              
  turn_direction = input("Which direction do you want to turn? Forward or Backward: ").upper()
  turn_amount = input(f"How far do you want to turn {turn_direction}? ")
  if turn_direction == "Forward":
    forward(turn_amount)
  elif turn_direction == "Backward":
    backward(turn_amount)
  
# Exits the program
def exit():
  global slay
  slay = False

# If the Freshmen are doing well
def good():
  for i in range(0,10):
    print(f'{i} good job')
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(22, GPIO.LOW)

# If the Freshmen are doing bad
def bad():
  for i in range(0,10):
    print(f'{i} bad job')
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(26, GPIO.LOW)
  
slay = True

while slay == True:
  print("Command List: Message, Camera, Exit, Good, Bad")
  command = input("Enter command: ").title
  if command == "Message":
    send_message()
  elif command == "Camera":
    cam_command = input("Camera Commands: Live, Rotate").title()
    if cam_command  == "Live":
      live_camera()
    elif cam_command == "Rotate":
      rotate_camera()
    else:
      print("Not a command")
  elif command == "Exit":
    slay = False
  elif command == "Good":
    good()
  elif command == "Bad":
    bad()
  else: 
    print("This is not a command.")

