from gpiozero import LED, Button
from time import sleep
from sys import exit
import threading

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("helpinghoursadm@gmail.com", "HelpingHours12")

led = LED(4)

button = Button(14)


#print('Ready..')
led.on()
sleep(2)
led.off()

def closed(button):
    led.on()
#    msg = "Garage Door Closed"
#    server.sendmail("helpinghoursadm@gmail.com", "thebeard@me.com", msg)
#    server.quit()
    print(str(button.pin.number) + ' closed')


def open(button):
    led.off()
#    msg = "Garage Door Open"
#    server.sendmail("helpinghoursadm@gmail.com", "thebeard@me.com", msg)
#    server.quit()
    print(str(button.pin.number) + ' open')
    

button.when_pressed = closed

button.when_released = open
