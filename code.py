# Write your code here :-)
import re
import keypad
import board
real_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']
km = keypad.KeyMatrix(
    row_pins=(board.GP2, board.GP7, board.GP6, board.GP4),
    column_pins=(board.GP3, board.GP1, board.GP5),
)

while True:
    event = km.events.get()
    if event:
        
        if 'pressed>' in str(event):
        #print(event)
        
            pressed = real_keys[int(str(event).replace('<Event: key_number', '').replace('pressed>',''))]
            print(pressed)
