from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

cpfs = [
    '09491954725', '09946505746', '11012969762', '08265773773', '08550281735',
    '10876069774', '07731927784', '08585072776', '08129707721', '05436768709',
    '07047667792', '08920900736', '13040949799', '05905378738', '01642176656',
    '28440128843', '04199084711', '05558147776', '07357600718', '10846864738'
]

datas_nascimento = [
    '03101982', '30061982', '31101984', '29121974', '19021980',
    '23081980', '08121968', '19031980', '27041976', '11091983',
    '12081975', '07101978', '30051987', '04111987', '16111987',
    '28011977', '10041977', '11101982', '06121976', '12121984'
]

navegador.get("https://cadunico.dataprev.gov.br/#/consultaCpf")

for i in range(0, 20):


    navegador.find_element('xpath', '//*[@id="numeroCpfPessoa"]').send_keys(cpfs[i])
    navegador.find_element('xpath', '//*[@id="mui-1"]').send_keys(datas_nascimento[i])
    time.sleep(2)
    navegador.find_element('xpath', '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/button[2]').click()
    time.sleep(60)






from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

cpfs = [
    '09491954725', '09946505746', '11012969762', '08265773773', '08550281735',
    '10876069774', '07731927784', '08585072776', '08129707721', '05436768709',
    '07047667792', '08920900736', '13040949799', '05905378738', '01642176656',
    '28440128843', '04199084711', '05558147776', '07357600718', '10846864738'
]

datas_nascimento = [
    '03101982', '30061982', '31101984', '29121974', '19021980',
    '23081980', '08121968', '19031980', '27041976', '11091983',
    '12081975', '07101978', '30051987', '04111987', '16111987',
    '28011977', '10041977', '11101982', '06121976', '12121984'
]


servico = Service(ChromeDriverManager().install())

for i in range(12, 19):

    navegador = webdriver.Chrome(service=servico)
    navegador.get("https://cadunico.dataprev.gov.br/#/consultaCpf")

    campo_cpf = navegador.find_element('xpath', '//*[@id="numeroCpfPessoa"]')
    campo_data = navegador.find_element('xpath', '//*[@id="mui-1"]')

    campo_cpf.clear()  # Limpa qualquer conteúdo no campo
    campo_data.clear()  # Limpa qualquer conteúdo no campo

    campo_cpf.send_keys(cpfs[i])
    campo_data.send_keys(datas_nascimento[i])
    time.sleep(2)

    navegador.find_element('xpath', '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/button[2]').click()
    time.sleep(2)

    #navegador.find_element('tag name', 'body').send_keys(Keys.F5)

    navegador.quit()
