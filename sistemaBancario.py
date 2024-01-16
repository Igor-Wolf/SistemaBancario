
#-------------------------------------------------------- Variáveis Globais 
import os
from datetime import datetime
auxiliar = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES= 3


#-------------------------------------------------------- Funções Auxiliares


def limpatela():
    input("\nPressione qualquer tecla para continuar...\n\n")
    os.system('cls')



def imprimirRecibo():
    texto_a_salvar = "=" * 45 + " EXTRATO " +"=" * 45 + "\n\n"
    texto_a_salvar += f"As operações realizadas foram: \n\n{extrato} \nSeu saldo atual é de R${saldo:.2f}"
    nome_do_arquivo = "recibo.txt"

    # Abre o arquivo em modo de escrita (w)
    with open(nome_do_arquivo, 'w') as arquivo:
        # Escreve a string no arquivo
        arquivo.write(texto_a_salvar)

    print(f"O conteúdo foi salvo no arquivo {nome_do_arquivo}.")

#-------------------------------------------------------- Cabeçalhos 

def cabecalho():
    print("=" * 45 + " BANCO ORIGINAL " +"=" * 45)

def cabecalho1():
    print("=" * 45 + " DEPÓSITO " +"=" * 45)

def cabecalho2():
    print("=" * 47 + " SAQUE " +"=" * 47)

def cabecalho3():
    print("=" * 45 + " EXTRATO " +"=" * 45)

#-------------------------------------------------------- Menus
     
def menu():

    print(""" 

    Qual operação deseja efetuar?
      
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair

    """)

def menu1():
    cabecalho1()
    global saldo, extrato
    auxiliar= float(input("Digite o valor a ser depositado\n"))
    data = datetime.now()

    if (auxiliar >=0):
        saldo+= auxiliar

        extrato += f"Depósito de R${auxiliar:.2f} Operação realizada em: {data.strftime("%d-%m-%Y %H:%M:%S")}\n"
    else:
        print("Valor incorreto, operação encerrada")
    limpatela()

def menu2():
    cabecalho2()
    global saldo, limite, extrato,numero_saques, LIMITE_SAQUES
    data = datetime.now()
    auxiliar= float(input("Digite o valor a ser sacado\n"))
    
    if (saldo >= auxiliar) and (auxiliar <=limite) and (numero_saques <LIMITE_SAQUES) and (auxiliar >=0):
        saldo -=auxiliar
        numero_saques += 1
        extrato += f"Saque de R${auxiliar:.2f} Operação realizada em: {data.strftime("%d-%m-%Y %H:%M:%S")}\n"
    else:
        print("Valor incorreto, operação encerrada")
    limpatela()

def menu3():
    cabecalho3()
    global extrato, saldo
    print(f"As operações realizadas foram: \n\n{extrato} \nSeu saldo atual é de R${saldo:.2f}")
    imprimirRecibo()
    limpatela()

#-------------------------------------------------------- Programa Principal
while (True):
    cabecalho()
    menu()
    auxiliar = input()

    if auxiliar == "1":
        limpatela()
        menu1()
    elif auxiliar == "2":
        limpatela()
        menu2()
    elif auxiliar == "3":
        limpatela()
        menu3()
    elif auxiliar == "4":
        break
    else:
        print("Operação inválida, selecione novamente a opção desejada")
