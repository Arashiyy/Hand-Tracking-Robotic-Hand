import pyfirmata2
import time

board = pyfirmata2.Arduino('COM3')  # double check your port

it = pyfirmata2.util.Iterator(board)
it.start()


servo = board.get_pin('d:10:s')

time.sleep(1)  # extra wait after pin setup

servo.write(180)  # start at middle, not 0 or 180
time.sleep(2)

servo.write(0)
time.sleep(2)

servo.write(180)
time.sleep(2)

board.exit()