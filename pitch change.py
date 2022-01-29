# imports!

import keypad
import time
import board
import digitalio
import pwmio
from adafruit_debouncer import Debouncer
x = 1
high = 0
f = 0
wonky = False
# serial welcome messages and credits
print('welcome to keeb synth serial')
print('version 2.0')
print('copright nathan koliha 2022 released under the Mit license')

# defining of static and changing variables 
piezo = pwmio.PWMOut(board.GP14, duty_cycle=0, frequency=440, variable_frequency=True)# setup code for the piezo disc output 

real_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']# list of keys that code uses to convert presses to a value

km = keypad.KeyMatrix(
    row_pins=(board.GP2, board.GP7, board.GP6, board.GP4),
    column_pins=(board.GP3, board.GP1, board.GP5),
)# matrix used to get key presses 
led = digitalio.DigitalInOut(board.LED)# led pin defining 
led.direction = digitalio.Direction.OUTPUT# more led pin setup
TONE_FREQ = { '1':220,
              '2':250,
              '3':262,
              '4':294,  # C4
              '5':330,  # D4
              '6':349,  # E4
              '7':392,  # F4
              '8':440,  # G4
              '9':500, 
              '0':523 # A4               
            } # list of frequencys and their corsponding number 
last = ''# records last event that occured 

# the main code 
while True:# main loop that code runs in
    event = km.events.get()# listens for events on keys 
    led.value = False
    if event:# basically this block sees if a key was pressed and if it was plays that keys note or does it's action(s)
        last = event
	
        while 'released>' not in str(event):
            
            event = km.events.get()
            led.value = True
            pressed = real_keys[int(str(last).replace('<Event: key_number', '').replace('pressed>',''))]#defines what key was pressec
            print('key', pressed, wonky)
            if pressed == '*':
                wonky += 1
                if wonky >= 4:
                    wonky = 3
            if pressed == '#':
               wonky = wonky - 1
               if wonky <= 0:
                   wonky = 1
               
            
              
            
            if pressed not in ['*', '#']:# this block and on plays the notes 
                if wonky == 1:
                    
                    x = TONE_FREQ[pressed]+30
                    piezo.frequency = x 
                    piezo.duty_cycle = 65535 // 2  # On 50%
                elif wonky == 2:
                    x = TONE_FREQ[pressed]-30
                    piezo.frequency = x 
                    piezo.duty_cycle = 65535 // 2  # On 50%
                else:
                    x = TONE_FREQ[pressed]
                    piezo.frequency = x 
                    piezo.duty_cycle = 65535 // 2  # On 50%
                
                
                
                
                
                  # On for 1/4 second
        piezo.duty_cycle = 0# Off


