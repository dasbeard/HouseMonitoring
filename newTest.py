from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(4)
button = Button(14)

print('Ready..')
led.on()
sleep(2)
led.off()

def closed(button):
    led.on()
    print(str(button.pin.number) + ' closed')

def open(button):
    led.off()
    print(str(button.pin.number) + ' open')
    

button.when_pressed = closed
button.when_released = open

pause()
