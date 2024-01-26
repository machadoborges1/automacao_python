import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
# Aguarde alguns segundos antes de começar a simulação
time.sleep(5)

# Fechar o Microsoft Edge usando Alt+F4
pyautogui.hotkey('alt', 'f4')

# Aguarde um pouco antes de abrir novamente
time.sleep(2)

# Abrir o Microsoft Edge (ou substitua pela sequência de atalhos do seu sistema operacional)
pyautogui.hotkey('winleft', 'r')  # Pressionar Win+R para abrir a caixa de execução
time.sleep(1)
pyautogui.write('msedge')  # Digitar 'msedge' (ou o comando correto para o Microsoft Edge)
pyautogui.press('enter')  # Pressionar Enter para abrir o Microsoft Edge
