from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

caminho_arquivo = 'cad_unico_v1.txt'
arquivo_escrita = 'cadastro_unico_devedores.txt'

cpfs = []
datas_nascimento = []
cadastros = []

with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        valores = linha.split()
        cpf = valores[0]
        data_nascimento = valores[1]
        cpfs.append(cpf)
        datas_nascimento.append(data_nascimento)

servico = Service(ChromeDriverManager().install())

for i in range(0, 10):
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
    time.sleep(20)

    elemento = navegador.find_element('xpath', '//*[@id="root"]/div[3]/div[2]/div[1]/div[2]/div/span')
    texto = elemento.text
    cadastros.append(texto)

    #navegador.find_element('tag name', 'body').send_keys(Keys.F5)

    time.sleep(2)
    navegador.quit()

with open(arquivo_escrita, 'w') as arquivo:
    for cpf, cadastro in zip(cpfs, cadastros):
        linha = f"{cpf} {cadastro}\n"
        arquivo.write(linha)