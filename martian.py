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


color_dict = {
  "red": ['gpioPinHere', 'GPIO.HIGH'],
  "orange": ['gpioPinHere', '[100, 100, 0]'],
  "yellow": ['gpioPinHere', 'GPIO.HIGH'],
  "green": ['gpioPinHere', 'GPIO.HIGH'],
  "blue": ['gpioPinHere', 'GPIO.HIGH'],
  "purple": ['gpioPinHere', '[100, 0, 100]']
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
    #buzzer.start(0)
    #buzzer.ChangeDutyCycle(50)
    print(f"Beep {i+1}")
    time.sleep(0.5)

def set_LED(color):
  if color in ("red", "yellow","green", "blue"):
    #pin = color_dict[color][0]
    #state = color_dict[color][1]
    # something like GPIO.pin(pin, state)
    print("LED set to " + color)
  elif color in ("orange", "purple"):
    print("LED set to " + color)
    

def rotate_camera():
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

  turn_direction = input("Which direction do you want to turn? Forward or Backward: ").upper()
  turn_amount = input(f"How far do you want to turn {turn_direction}? ")
  if turn_direction == "Forward":
    forward(turn_amount)
  elif turn_direction == "Backward":
    backward(turn_amount)
  
  
  
  camera.start_preview(fullscreen=False, window=(100, 20, 640, 380))  
  time.sleep(1) 
  input("Press enter to stop live viewing: ")
  camera.stop_preview()
  camera.start_preview()

def exit():
  global slay
  slay = False

def good():
  for i in range(0,10):
    print('good job')
    #GPIO.output(led_pin_for_green, GPIO.HIGH)
    #time.sleep(0.5)
    #GPIO.output(led_pin_for_green, GPIO.LOW)

def bad():
  for i in range(0,10):
    print(f'{i} bad job')
    #GPIO.output(led_pin_for_red, GPIO.HIGH)
    #time.sleep(0.5)
    #GPIO.output(led_pin_for_red, GPIO.LOW)
  
slay = True

while slay == True:
  print("Command List: Message, Camera, Exit, Good, Bad")
  command = input("Enter command: ").title
  if command == "Message":
    send_message()
  elif command == "Camera":
    cam_command = input("Camera Commands Live, Rotate").ttitle()
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

