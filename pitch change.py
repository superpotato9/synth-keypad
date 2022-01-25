
import keypad
import time
import board
import digitalio
import pwmio
x = 1
# serial welcome messages and credits
print('welcome to keeb synth serial')
print('version 1.5')
print('copright nathan koliha 2022 released under the Mit license')

# defining of static and changing variables 
piezo = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=440, variable_frequency=True)# setup code for the piezo disc output 

real_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']# list of keys that code uses to convert presses to a value

km = keypad.KeyMatrix(
    row_pins=(board.GP2, board.GP7, board.GP6, board.GP4),
    column_pins=(board.GP3, board.GP1, board.GP5),
)# matrix used to get key presses 
led = digitalio.DigitalInOut(board.LED)# led pin defining 
led.direction = digitalio.Direction.OUTPUT# more led pin setup
TONE_FREQ = { '1':262,  # C4
              '2':294,  # D4
              '3':330,  # E4
              '4':349,  # F4
              '5':392,  # G4
              '6':440,  # A4
              '7':494,
              '8':523,
              '9':586,
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
            print('key', pressed)
            if pressed == '*':
                x += 5
            if pressed == '#':
                x = x - 5
                if x < -20:
                    x = -20
                
            if pressed not in ['*', '#', '0']:# this block and on plays the notes 
                f = TONE_FREQ[pressed]
                piezo.frequency = f + x
                piezo.duty_cycle = 65535 // 2  # On 50%
                time.sleep(0.07)  # On for 1/4 second
        piezo.duty_cycle = 0# Off

