# -*- coding: utf-8 -*-
#!/usr/bin/python3
# IMPORTS AQUI
import socket, sys, select
import time
import pyautogui
import subprocess
import urllib
import os
import platform
import getpass
import requests
import random
from random import choice
import re
from datetime import datetime
import json
import urllib3
from datetime import date
# IMPORTS ACABAM AQUI
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Corzinha de gay...
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
# Corzinha de gay acaba aqui...
def spamkk():
    os.system('figlet FLOODER')
    quantidade = input(f'{B}Quantidade De Vezes Que Voce Quer Enviar A Mensagem: {G}')
    mensagem = input(f'{B}Qual Mensagem Voce Quer Enviar: {G}')
    print(f'{B}Agora Abra A Aba Ou Aplicativo Desejado E Clique Uma  Vez Encima Da Caixa De Texto E Aguarde 30 Segundos...{C}')
    for segundos in range(1, 11):
        sys.stdout.write("\r{} Segundos Passados...".format(segundos))
        time.sleep(1)
        if segundos == 10:
           print(f'\n{B}Iniciando Flood...{C}')
           for nobru in range(int(quantidade)):
            pyautogui.typewrite(str(mensagem))
            pyautogui.press("enter")
def auto_clicker():
    numclicks = input(f'{B}QUANTOS CLICKS?: {G}')
    print(f'{B}Agora Abra A Aba Ou Aplicativo Desejado E Aguarde 10 Segundos...{C}')
    for segundos in range(1, 11):
        sys.stdout.write("\r{} Segundos Passados...".format(segundos))
        time.sleep(1)
        if segundos == 10:
           print(f'\n{B}Iniciando Auto Clicker...{C}')
           for nobru in range(int(numclicks)):
            pyautogui.click()
def pedra_papel():
    escolha_usuario = input(f'{B}Escolha: {G}Pedra Papel Ou Tesoura: {G}')
    pedra = 'pedra'
    papel = 'papel'
    Tesoura = 'tesoura'
    tudo = [pedra, papel, Tesoura]
    escolha = random.choice(tudo)
    if escolha_usuario.lower() == escolha:
        print(f'{B}Ooops Parece Que Tivemos Um {G}Empate\n{B}Minha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha_usuario.lower() == 'pedra' and escolha == 'papel':
        print(f'{B}Oba eu {G}GANHEI...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha_usuario.lower() == 'tesoura' and escolha == 'pedra':
        print(f'{B}Oba eu {G}GANHEI...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha_usuario.lower() == 'papel' and escolha == 'tesoura':
        print(f'{B}Oba eu {G}GANHEI...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha == 'pedra' and escolha_usuario.lower() == 'papel':
        print(f'{B}Oba voce {G}GANHOU...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha == 'tesoura' and escolha_usuario.lower() == 'pedra':
        print(f'{B}Oba voce {G}GANHOU...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    elif escolha == 'papel' and escolha_usuario.lower() == 'tesoura':
        print(f'{B}Oba voce {G}GANHOU...{B}\nMinha Escolha: {G}{escolha}\n{B}Sua Escolha:{G}{escolha_usuario}')
    time.sleep(3)
    menudeopcao2()
def consultacpf1():
    os.system('figlet CPF')
    cpfoda = input(f"{B}DIGITE O CPF: {G}")
    try:
     cpf = re.sub('[^0-9]+', '', cpfoda)
     apicpfoda = "https://oc-129-150-70-222.compute.oraclecloud.com/rest/venda-online/v2/propostas/ConsultaBaseCpf?cpf=" + cpfoda
     headerfoda = {
        'Host': 'oc-129-150-70-222.compute.oraclecloud.com',
        'Accept': '*/*',
        'Authorization': 'Basic c29hY3NpbnRlZ3JhdGlvbnVzZXI6Y2Y3WlB4VlY2ajZLeEx3VA==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept-Language': 'pt-BR,pt;q=0.9',
     }
     rcpf = requests.get(apicpfoda, headers=headerfoda, verify=False)
     resultscpf = json.loads(rcpf.content)
     if str(resultscpf['NomeCompleto']) != 'None':
        print(f"""{B}CPF: {G}{cpfoda}\n{B}NOME:  {G}{str(
            resultscpf['NomeCompleto'])}\n{B}DATA DE NASCIMENTO: {G}{str(resultscpf['DataNascimento'])}\n{B}SEXO: {G}{str(resultscpf['Sexo'])}\n{B}TELEFONE CELULAR: {G}{str(resultscpf['TelefoneCelular'])}\n{B}TELEFONE RESIDENCIAL: {G}{str(resultscpf['TelefoneResidencial'])}\n{B}MAE: {G}{str(resultscpf['NomeMae'])}\n{B}RUA: {G}{str(resultscpf['Logradouro'])}\n{B}NUMERO: {G}{str(resultscpf['Numero'])}\n{B}BAIRRO: {G}{str(resultscpf['Bairro'])}\n{B}CIDADE: {G}{str(resultscpf['Cidade'])}\n{B}ESTADO: {G}{str(resultscpf['Estado'])}\n{B}CRITICA: {G}{str(resultscpf['mensagemRetorno'])}""")
    except:
        print(f'{R}ALGUM ERRO OCORREU(PROVAVELMENTE A BASE NAO ESTA MAIS ONLINE :( )')
def infomaquina():
    now = datetime.now()
    os.system('figlet INFO')
    userkk = getpass.getuser()
    data_agora = date.today()
    ipkk = socket.gethostbyname(socket.gethostname())
    print(f"""{B}DATA: {G}{data_agora}\n{B}HORA: {G}{now.hour}\n{B}MINUTOS: {G}{now.minute}\n{B}SEGUNDOS: {G}{now.second}{B}\nUSER: {G}{userkk}{B}\nSISTEMA: {G}{platform.system()}{B}\nARQUITETURA DO PROCESSADOR {G}{platform.machine()}{B}\nNOME DO PC: {G}{platform.node()}{B}\nDISTRIBUICAO: {G}{platform.platform()}\n{B}PROCESSADOR:  {G}{os.system("cat /proc/cpuinfo | sed '5!d'")}
""")
    time.sleep(3)
    menudeopcao2()

def extrairhtml():
    os.system('figlet EXTRAIR')
    url = input(f"{B}DIGITE A URL DO SITE: {G}")
    alvo = urllib.request.urlopen(url)
    print(f"{B}Resultado:\n{G}{alvo.read()}")
    time.sleep(3)
    menudeopcao2()
def gerarpessoas():
        linksla = requests.get('http://geradorapp.com/api/v1/cpf/generate?token=4f8d9149be4858c837b8b38f5c0d194a')
        semideia = linksla.json
        resposta = semideia()['data']['number_formatted']
        print(f'{B}CPF GERADO COM {G}SUCESSO!{B}\nCPF: {G}{resposta}{C}')
        time.sleep(3)
        menudeopcao2()
def consultaplaca():
    os.system('figlet PLACA')
    placa = input(f'{B}DIGITE A PLACA A SER  CONSULTADA: {B}')
    try:
        api2267placa = "https://apicarros.com/v1/consulta/" + placa + "/json"
        rplaca = requests.get(api2267placa, verify=False)
        resultadoplaca = json.loads(rplaca.content)
        if str(resultadoplaca["cor"]) != 'LIMITE DE CONSULTA ATINGIDO':
            if str(resultadoplaca['ano']) == "":
                resultadoplaca['ano'] = 'SEM INFORMACAO'

            if str(resultadoplaca['chassi']) == "":
                resultadoplaca['chassi'] = 'SEM INFORMACAO'

            if str(resultadoplaca['cor']) == "":
                resultadoplaca['cor'] = 'SEM INFORMACAO'

            if str(resultadoplaca['data']) == "":
                resultadoplaca['data'] = 'SEM INFORMACAO'

            if str(resultadoplaca['dataAtualizacaoAlarme']) == "":
                resultadoplaca['dataAtualizacaoAlarme'] = 'SEM INFORMACAO'

            if str(resultadoplaca['dataAtualizacaoCaracteristicasVeiculo']) == "":
                resultadoplaca['dataAtualizacaoCaracteristicasVeiculo'] = 'SEM INFORMACAO'

            if str(resultadoplaca['dataAtualizacaoRouboFurto']) == "":
                resultadoplaca['dataAtualizacaoRouboFurto'] = 'SEM INFORMACAO'

            if str(resultadoplaca['marca']) == "":
                resultadoplaca['marca'] = 'SEM INFORMACAO'

            if str(resultadoplaca['modelo']) == "":
                resultadoplaca['modelo'] = 'SEM INFORMACAO'

            if str(resultadoplaca['uf']) == "":
                resultadoplaca['uf'] = 'SEM INFORMACAO'

            if str(resultadoplaca['situacao']) == "":
                resultadoplaca['situacao'] = 'SEM INFORMACAO'
            if str(resultadoplaca["cor"]) != 'LIMITE DE CONSULTA ATINGIDO':
                ano = resultadoplaca['ano']
                chassi = resultadoplaca['chassi']
                cor = resultadoplaca['cor']
                data = resultadoplaca['data']
                alarme = resultadoplaca['dataAtualizacaoAlarme']
                veiculo = resultadoplaca['dataAtualizacaoCaracteristicasVeiculo']
                roubo = resultadoplaca['dataAtualizacaoRouboFurto']
                marca = resultadoplaca['marca']
                modelo = resultadoplaca['modelo']
                municipio = resultadoplaca['municipio']
                uf = resultadoplaca['uf']
                situacao = resultadoplaca['situacao']
                print(
                f'{B}PLACA: {G}{placa}{B}\nANO: {G}{ano}{B}\nCHASSI: {G}{chassi}{B}\nCOR: {G}{cor}{B}\nDATA: {G}{data}{B}\nALARME: {G}{alarme}{B}\nVEICULO: {G}{veiculo}{B}\nROUBO: {G}{roubo}{B}\nMARCA: {G}{marca}{B}\nMODELO: {G}{modelo}{B}\nMUNICIPIO: {G}{municipio}{B}\nUF: {G}{uf}{B}\nSITUACAO: {G}{situacao}{B}{C}')
                time.sleep(3)
                menudeopcao2()
        else:
            print(
                f'{B}A PLACA {G}{placa}{B}{R}NAO{B} FOI CONSULTADA POIS LEVAMOS TIMEOUT, TENTANDO NOVAMENTE EM: 1 MINUTO...{C}')
            for segundos in range(0, 61):
                segundos2 = sys.stdout.write("\r{} Segundos Passados...".format(segundos))
                sys.stdout.flush()
                time.sleep(1)
            if segundos2 == '60':
               consultaplaca()
    except:
        print(f'{R}ALGUM ERRO OCORREU!!!')
def menudeopcao2():
    print(f'{B} ESCOLHA: {C}')
    print(f"""
    {B} {G}1{B} - FLOODER {C}(ENVIA MENSAGENS AUTOMATICAMENTE) 
    {B} {G}2{B} - INFORMACOES SOBRE SUA MAQUINA
    {B} {G}3{B} - CONSULTAR PLACA{C}(OBTEM ALGUMAS INFORMACOES APARTIR DE UMA PLACA DE CARRO)
    {B} {G}4{B} - CONSULTA CPF{C}(OBTEM ALGUMAS INFORMACOES APARTIR DO CPF)
    {B} {G}5{B} - AUTO CLICKER{C}(CLICA AUTOMATICAMENTE)
    {B} {G}6{B} - GERADOR DE PESSOAS FISICAS{C}(CPF)
    {B} {G}7{B} - EXTRAI CONTEUDO DE UMA PAGINA{C}(INCLUSIVE O HTML)
    {B} {G}8{B} - PEDRA PAPEL TESOURA""")
    ferramenta_sele = input(f'{B}SELECIONE UMA DAS OPCOES: {G}')
    if ferramenta_sele == '1':
        spamkk()
    elif ferramenta_sele == '2':
        infomaquina()
    elif ferramenta_sele == '3':
        consultaplaca()
    elif ferramenta_sele == '4':
        consultacpf1()
    elif ferramenta_sele == '5':
        auto_clicker()
    elif ferramenta_sele == '6':
        gerarpessoas()
    elif ferramenta_sele == '7':
        extrairhtml()
    elif ferramenta_sele == '8':
        pedra_papel()
    else:
        print(f'{B}[{R}-{B}] {R}SELECAO INVALIDA.{C}')
        time.sleep(1)
        menudeopcao2()
os.system('figlet HELIOR MULTI TOOL')
print(f'{B}Inicializando Em: {G}10{B} Segundos...{C}')
for segundos in range(1, 11):
    sys.stdout.write("\r{} Segundos Passados...".format(segundos))
    time.sleep(1)
    if segundos == 10:
        menudeopcao2()
