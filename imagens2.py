import time
import pyautogui

cpfs = ['12554831645', '12554831645', '05126679180']
datas_nascimento = ['08101996','08101997','08011991']

pyautogui.hotkey('alt', 'tab')
time.sleep(1)

for i in range(0,2):
    pyautogui.hotkey('f5')
    time.sleep(2)

    for j in range(0,11):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.write(cpfs[i])
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(datas_nascimento[i])


    for k in range(0, 3):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

    # 250 500

    screenshot = pyautogui.screenshot(region=(465, 345, 928, 70))
    screenshot.save(f'imagens/{i}.bmp')
    time.sleep(5)


