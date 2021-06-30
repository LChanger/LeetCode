from pymouse import PyMouse
import time
# from pykeyboard import PyKeyboard
m = PyMouse()
# k = PyKeyboard()
# m.position()
m.move(3457, 711)

for i in range(10):
    m.click(3457, 711,1)
    time.sleep(120)
