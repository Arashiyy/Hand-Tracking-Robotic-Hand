from pyfirmata2 import Arduino
import time

board = Arduino('COM3')
servo = board.get_pin('d:6:s')

servo.write(0)
time.sleep(1)

servo.write(30)
time.sleep(1)

servo.write(60)
time.sleep(1)

servo.write(90)
time.sleep(1)

servo.write(105)
time.sleep(1)



# MAX
# INDEX MAX - 90
# MIDDLE MAX - 55
# RING MAX - 105
# PINKY MAX - 90