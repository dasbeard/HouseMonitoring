from picamera import PiCamera, Color
from time import sleep
#import dropbox
#dbx = dropbox.Dropbox('qjLFeIUqjLFeIUYs6wAAAAAAAAI1wAO2ZzzJ9Z2RVXtUs7zAp1vGs2uOA7Io8Qkl-oj5doxYs6wAAAAAAAAI1wAO2ZzzJ9')
#dbx.users_get_current_account()

camera = PiCamera()

camera.rotation = 180
#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.annotate_text = 'Hello World'
#camera.annotate_text_size = 85
camera.brightness = 55

#camera.annotate_background = Color('white')
#camera.annotate_foreground = Color('pink')

camera.start_preview()
for i in range(1):
    sleep(1.5)
    camera.capture('/home/pi/Downloads/TestFolder/image%s.jpg' % i)
camera.stop_preview()