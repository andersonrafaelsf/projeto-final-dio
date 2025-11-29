from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar(pasta):
    fernet = Fernet(carregar_chave())
    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho):
            with open(caminho, "rb") as file:
                arquivo_cripto = file.read()
            dados = fernet.decrypt(arquivo_cripto)
            with open(caminho, "wb") as file:
                file.write(dados)
    print("[ ✔ ] Arquivos restaurados!")

descriptografar("arquivos_teste")
