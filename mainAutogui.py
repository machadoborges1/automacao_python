import time
import pyautogui

caminho_arquivo = 'lista_cad_unico_v10.txt'

cpfs = []
datas_nascimento = []

def carrega_dados_screen(cpf, data):
    time.sleep(3)
    pyautogui.hotkey('f5')
    time.sleep(2)

    for j in range(0, 11):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.write(cpf)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(data)

    for k in range(0, 3):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(30)

    #460, 330, 928, 40 - 100
    #460, 430, 928, 150 - 150
    return pyautogui.screenshot(region=(465, 345, 928, 70))

def consome_dados_screen(cpf, data):
    time.sleep(3)
    pyautogui.hotkey('f5')
    time.sleep(2)

    for j in range(0, 11):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.write(cpf)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(data)

    for k in range(0, 3):
        pyautogui.press('tab')
        time.sleep(0.2)

    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(30)

    return pyautogui.screenshot(region=(465, 345, 928, 70))

pyautogui.hotkey('alt', 'tab')

cadastrado = carrega_dados_screen('12554831645', '08101996')
naoEncontrado = carrega_dados_screen('05126679180', '08011991')
dadosIncorretos = carrega_dados_screen('12554831645', '08121996')


with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        valores = linha.split()
        cpf = valores[0]
        data_nascimento = valores[1]
        cpfs.append(cpf)
        datas_nascimento.append(data_nascimento)

time.sleep(0.2)

nome_arquivo = 'dados.txt'
erro_arquivo = 'dados_erro.txt'

contador = 0

for i in range(374, 494):
    contador += 1
    if contador > 10000:
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)
        pyautogui.hotkey('winleft', 'r')
        time.sleep(1)
        pyautogui.write('msedge')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('f5')
        time.sleep(2)
        contador = 0
    var = consome_dados_screen(cpfs[i], datas_nascimento[i])
    if var == cadastrado:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{cpfs[i]}: Cadastrado\n')
    elif var == naoEncontrado:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{cpfs[i]}: Nao_Encontrado\n')
    elif var == dadosIncorretos:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{cpfs[i]}: Dados_Inconrretos\n')
    else:
        with open(erro_arquivo, 'a') as arquivo:
            arquivo.write(f'{cpfs[i]} {datas_nascimento[i]}\n')
