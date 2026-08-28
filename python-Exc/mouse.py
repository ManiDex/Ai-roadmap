import pyautogui as pag
import random as ra
import time as t

while True:
    x = ra.randint(500, 600)
    y = ra.randint(200,700)
    pag.moveTo(x, y, 0.1)
    t.sleep(0.1)