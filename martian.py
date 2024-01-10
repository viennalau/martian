import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
char_amt = 0

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

GPIO.setup('PIN', GPIO.OUT)
red = GPIO.PWM('PIN', 5)
GPIO.setup(5, GPIO.OUT)
yellow = GPIO.PWM(5, 5)
GPIO.setup(4, GPIO.OUT)
green = GPIO.PWM(4, 5)
GPIO.setup(5, GPIO.OUT)
blue = GPIO.PWM(5, 5)



# Buzzer Setup
GPIO.setup('BuzzerPin#', GPIO.OUT)


# Multicolor LED Setup - Orange

GPIO.setup(21, GPIO.OUT)
red_multi = GPIO.PWM(21, 75)
GPIO.setup(20, GPIO.OUT)
green_multi = GPIO.PWM(20, 75)
GPIO.setup(16, GPIO.OUT)
blue_multi = GPIO.PWM(16, 75)

# Multicolor LED Setup - Purple

GPIO.setup(21, GPIO.OUT)
red_multi = GPIO.PWM(21, 75)
GPIO.setup(20, GPIO.OUT)
green_multi = GPIO.PWM(20, 75)
GPIO.setup(16, GPIO.OUT)
blue_multi = GPIO.PWM(16, 75)

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
    


def live_camera():
  camera.start_preview()
  time.sleep(10)
  input("Press enter to stop live viewing: ")
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
  
send_message()
slay = True

while slay == True:
  print("Command List: Message, Camera, Exit, Good, Bad")
  command = input("Enter command: ")
  if command == "Message":
    send_message()
  elif command == "Camera":
    cam_command = input("Your command list is: Live ").upper()
    if cam_command == "Live":
      live_camera()
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

