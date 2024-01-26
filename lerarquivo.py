caminho_arquivo = 'cad_unico_v1.txt'
caminhoArquivo = 'cad_unico_v2.txt'

cpfs = []
datas_nascimento = []
cadastro = ['nome1', 'nome2', 'nome3']

with open(caminho_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        valores = linha.split()
        cpf = valores[0]
        data_nascimento = valores[1]
        cpfs.append(cpf)
        datas_nascimento.append(data_nascimento)

with open(caminhoArquivo, 'w') as arquivo:
    for cpf, data, nome in zip(cpfs, datas_nascimento, cadastro):
        linha = f"{cpf} {data} {cadastro}\n"
        arquivo.write(linha)

print("CPFs:", cpfs[0])
print("CPFs:", cpfs[1])
print("CPFs:", cpfs[2])
