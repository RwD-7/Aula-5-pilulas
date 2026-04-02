import random
import datetime

def menu():
    nome_arq = "log.txt"
    while True:
        print("menu\n")
        print("1- gerar logs")
        print("2- analisar logs")
        print("3- gerar e analizar logs")
        print("4- sair")
        opc = int(input("Escolha uma opcao :"))
        gerarArquivos(nome_arq,qtd)
        if opc == 1:
            try:
                qtd = int(input("quantidade de logs (registros):"))
                gerarArquivo(nome_arq,qtd)
            except:
                print("entrada invalida")
        elif opc == 2:
            analisarlogs(nome_arq)
        elif opc == 3:
            try:
                qtd = int(input("quantidade de logs (registros):"))
                gerarArquivo(nome_arq,qtd)
                analisarLogs(nome_arq)
            except:
                print("entrada invalida")
        elif opc == 4:
            print ("ate mais")
            break
        else:
            print ("opcao invalida")

def gerarAquivo(nome_arq,qtd):
    with open(nome_arq,"w",encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarlog(i)+"\n")
        print("log gerado")

def montarlog(i):
    data = gerardata(i)
    ip = gerarip(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerartempo(i)
    agente = gerarAgente(i)
    protocolo = gerarprotocolo(i)
    tamanho = gerartamanho(i)
    return f'[{data}]{ip} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente} - /home'

def gerarData(i):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds= i* random.randint(5,20))
    return (base + delta).strftime("%d/%m/%Y %H:%M:%S")

def gerarIp(i):
    if i >= 20 and i <= 50:
        return '203.120.45.7'
    alse:
        return f"{random.randint(10,200)}.{random.randint(100,200)}.{random.randint(0,250)}.{random.randit(1,250)}"


