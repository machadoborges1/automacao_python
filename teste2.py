import time
import pyautogui

for i in range(1,4):
    screen = pyautogui.screenshot()
    screen.save(f'{i}.png')
    time.sleep(10)

