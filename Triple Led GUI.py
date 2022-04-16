#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##LED PINS
ledBlue = LED(21)
ledRed = LED (7)
ledGreen = LED(27)

##GUI DEFINITIONS##
win = Tk()
win.title("Triple LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## EVENT FUNCTIONS
def ledToggleBlue():
    if ledBlue.is_lit:
        ledBlue.off()
        ledButton1["text"]= "Turn Blue LED on"
    else:
        ledBlue.on()
        ledButton1["text"]= "Turn Blue LED off"
        ledRed.off()
        ledButton2["text"]= "Turn Red LED on"
        ledGreen.off()
        ledButton3["text"]= "Turn Green LED on"

def ledToggleRed():
    if ledRed.is_lit:
        ledRed.off()
        ledButton2["text"]= "Turn Red LED on"
    else:
        ledRed.on()
        ledButton2["text"]= "Turn Red LED off"
        ledBlue.off()
        ledButton1["text"]= "Turn Blue LED on"
        ledGreen.off()
        ledButton3["text"]= "Turn Green LED on"

def ledToggleGreen():
    if ledGreen.is_lit:
        ledGreen.off()
        ledButton3["text"]= "Turn Green LED on"
    else:
        ledGreen.on()
        ledButton3["text"] = "Turn Green LED off"
        ledRed.off()
        ledButton2["text"]= "Turn Red LED on"
        ledBlue.off()
        ledButton1["text"]= "Turn Blue LED on"
        
    
##WIDGETS###
ledButton1 = Button(win, text = 'Turn Blue LED On', font = myFont, command = ledToggleBlue, bg = 'bisque2', height = 1, width = 24)
ledButton1.grid(row = 0, column = 1)

ledButton2 = Button(win, text = 'Turn Red LED On', font = myFont, command = ledToggleRed, bg = 'bisque2', height = 1, width = 24)
ledButton2.grid(row = 1, column = 1)

ledButton3 = Button(win, text = 'Turn Green LED On', font = myFont, command = ledToggleGreen, bg = 'bisque2', height = 1, width = 24)
ledButton3.grid(row = 2, column = 1)

