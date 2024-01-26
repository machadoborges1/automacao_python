from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time

caminho_arquivo = 'cad_unico_dev_2023-2.txt'
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


servico = webdriver.FirefoxService(executable_path=GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)
navegador.get("https://cadunico.dataprev.gov.br/#/consultaCpf")

for i in range(2, 6):

    campo_cpf = navegador.find_element('xpath', '//*[@id="numeroCpfPessoa"]')
    campo_data = navegador.find_element('xpath', '//*[@id="mui-1"]')

    campo_cpf.clear()  # Limpa qualquer conteúdo no campo
    campo_data.clear()  # Limpa qualquer conteúdo no campo

    campo_cpf.send_keys(cpfs[i])
    campo_data.send_keys(datas_nascimento[i])
    time.sleep(4)

    navegador.find_element('xpath', '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/button[2]').click()
    time.sleep(30)

    elemento = navegador.find_element('xpath', '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div/span')
    texto = elemento.text
    cadastros.append(texto)

    navegador.find_element('tag name', 'body').send_keys(Keys.F5)

with open(arquivo_escrita, 'w') as arquivo:
    for cpf, data, cadastro in zip(cpfs, datas_nascimento, cadastros):
        linha = f"{cpf} {data} {cadastro}\n"
        arquivo.write(linha)
