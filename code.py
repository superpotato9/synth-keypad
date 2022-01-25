
         # Pause between notes
         
print('welcome to keeb synth serial')
print('version 1.0')
print('copright nathan koliha 2022 released under the Mit license')
import re
import keypad
import time
import board
import digitalio
import pwmio
piezo = pwmio.PWMOut(board.GP16, duty_cycle=0, frequency=440, variable_frequency=True)
real_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']
km = keypad.KeyMatrix(
    row_pins=(board.GP2, board.GP7, board.GP6, board.GP4),
    column_pins=(board.GP3, board.GP1, board.GP5),
)
d = .2
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
TONE_FREQ = { '1':262,  # C4
              '2':294,  # D4
              '3':330,  # E4
              '4':349,  # F4
              '5':392,  # G4
              '6':440,  # A4
              '7':494,
              '8':523,
              '9':586,
              '*':0,
              '0':0,
              '#':0
            } # B4
last = ''
while True:
    event = km.events.get()
    led.value = False
    if event:
        last = event
	
        while 'released>' not in str(event):
            #time.sleep(.3)
            #print(event)
            time.sleep(.2)
            event = km.events.get()
            led.value = True
           


            pressed = real_keys[int(str(last).replace('<Event: key_number', '').replace('pressed>',''))]
            print('key', pressed)
            f = TONE_FREQ[pressed]
            piezo.frequency = f
            piezo.duty_cycle = 65535 // 2  # On 50%
            time.sleep(0.05)  # On for 1/4 second
        piezo.duty_cycle = 0# Off
            
            
