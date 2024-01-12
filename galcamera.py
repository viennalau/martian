from picamera import PiCamera
import time

camera = PiCamera()
camera.rotation = 180

camera.start_preview(fullscreen=False, window=(100, 20, 640, 380))
time.sleep(5)
camera.capture('/home/pi/Desktop/picture1.jpg')
time.sleep(5)
input("Press enter to stop: ")
camera.stop_preview()