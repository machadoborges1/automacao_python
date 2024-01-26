def compare_bmp_files(file):
    with open('imagens/0.bmp', 'rb') as f1, open('imagens/1.bmp', 'rb') as f2, open('imagens/2.bmp', 'rb') as f3, open(file, 'rb') as fl:
        content1 = f1.read()
        content2 = f2.read()
        content3 = f3.read()
        arquivo = fl.read()

        if content1 == arquivo:
            return 'Cadastrado'
        elif content2 == arquivo:
            return 'Dados_Incorretos'
        elif content3 == arquivo:
            return 'Não_Cadastrado'
        else:
            return 'Captcha'

file_path2 = 'imagens/14576630660.bmp'

result = compare_bmp_files(file_path2)

print(result)
