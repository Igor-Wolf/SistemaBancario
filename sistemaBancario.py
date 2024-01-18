
#-------------------------------------------------------- Variáveis Globais 
import os
from datetime import datetime
auxiliar = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES= 3
AGENCIA = "0001"
usuarios = []
contas = []
numeroConta=1
contasInativas = []


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

def verificarUsuario(cpf, usuarios):
    usuariosFiltrado = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuariosFiltrado[0] if usuariosFiltrado else None

#-------------------------------------------------------- Cabeçalhos 

def cabecalho():
    print("=" * 45 + " BANCO ORIGINAL " +"=" * 45)

def cabecalho1():
    print("=" * 45 + " DEPÓSITO " +"=" * 45)

def cabecalho2():
    print("=" * 47 + " SAQUE " +"=" * 47)

def cabecalho3():
    print("=" * 45 + " EXTRATO " +"=" * 45)

def cabecalho4():
    print("=" * 45 + " NOVA CONTA " +"=" * 45)

def cabecalho5():
    print("=" * 45 + " CONTAS REGISTRADAS " +"=" * 45)

def cabecalho6():
    print("=" * 45 + " NOVO USUÁRIO " +"=" * 45)

def cabecalho7():
    print("=" * 45 + " INATIVAR CONTAS " +"=" * 45)

def cabecalho8():
    print("=" * 45 + " CONTAS INATIVAS " +"=" * 45)

def cabecalho9():
    print("=" * 45 + " REATIVAR CONTAS " +"=" * 45)

#-------------------------------------------------------- Menus
     
def menu():

    print(""" 

    Qual operação deseja efetuar?
      
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Inativar Contas
    [8] Listar Contas Inativas
    [9] Reativar Contas
    [10] Sair

    """)

def menu1(saldo, extrato, /):
    cabecalho1()
    auxiliar= float(input("Digite o valor a ser depositado\n"))
    data = datetime.now()

    if (auxiliar >=0):
        saldo+= auxiliar

        extrato += f"Depósito de R${auxiliar:.2f} \tOperação realizada em: {data.strftime("%d-%m-%Y %H:%M:%S")}\n"
        return saldo, extrato
    else:
        print("Valor incorreto, operação encerrada")
        limpatela()
        return saldo, extrato
        
def menu2(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    cabecalho2()
    data = datetime.now()
    auxiliar= float(input("Digite o valor a ser sacado\n"))
    
    if (saldo >= auxiliar) and (auxiliar <=limite) and (numero_saques <LIMITE_SAQUES) and (auxiliar >=0):
        saldo -=auxiliar
        numero_saques += 1
        extrato += f"Saque de R${auxiliar:.2f} \tOperação realizada em: {data.strftime("%d-%m-%Y %H:%M:%S")}\n"
        return saldo, extrato, numero_saques
    else:
        print("Valor incorreto, operação encerrada")
        limpatela()
        return saldo, extrato, numero_saques
 
def menu3(saldo, /, *, extrato):
    cabecalho3()
    print(f"As operações realizadas foram: \n\n{extrato} \nSeu saldo atual é de R${saldo:.2f}")
    imprimirRecibo()
    limpatela()

def menu4(agencia, numeroConta,usuarios):
    cabecalho4()
    cpf = input("Informe o CPF (somente números)")
    usuario = verificarUsuario(cpf,usuarios)

    if (usuario):
        print("Conta criada com sucesso!")
        limpatela()
        return {"agencia": agencia , "numeroConta": numeroConta,"usuario": usuario , "cpf": cpf}
        
    
    else:
        print("Usuário não cadastrado")
        limpatela()

def menu5(contas):
    cabecalho5()
    print("\n")
    for conta in contas:
        
        print (f"Agencia: \t{conta['agencia']} \nC/C: \t\t{conta['numeroConta']}\nTítular: \t{conta['usuario']["nome"]} \nCPF: \t\t{conta['cpf']}")
        print ("=" * 50)
    limpatela()

def menu6(usuarios):
    cabecalho6()
    cpf = input("Informe o CPF (somente números)")
    usuario = verificarUsuario(cpf,usuarios)

    if usuario:
        print ("Já existe usuário com esse CPF!")

    else:
        nome = input("Infome o nome completo: ")
        dataNascimento= input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco= input("Informe o endereço (logrdouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome,"dataNascimento":dataNascimento, "cpf":cpf, "endereco":endereco })
    limpatela()

def menu7(contas, contasInativas):
    cabecalho7()
    auxiliar= input("Qual conta deseja inativar? ")
    
    for conta in contas:
        
        if (conta['numeroConta'] == int(auxiliar)):
            contasInativas.append(conta)
            contas.remove(conta)
            limpatela()
            return
        
    print("Conta inexistente") 
    limpatela()   

def menu8(contas):
    cabecalho8()
    print("\n")
    for conta in contas:
        
        print (f"Agencia: \t{conta['agencia']} \nC/C: \t\t{conta['numeroConta']}\nTítular: \t{conta['usuario']["nome"]} \nCPF: \t\t{conta['cpf']}")
        print ("=" * 50)
    limpatela()


def menu9(contas, contasInativas):
    cabecalho9()
    auxiliar= input("Qual conta deseja ativar? ")
    
    for conta in contasInativas:
        
        if (conta['numeroConta'] == int(auxiliar)):
            contas.append(conta)
            contasInativas.remove(conta)
            limpatela()
            return

#-------------------------------------------------------- Programa Principal
    
while (True):
    cabecalho()
    menu()
    auxiliar = input()

    if auxiliar == "1":
        limpatela()
        saldo , extrato = menu1(saldo, extrato)#passagem de valores por posição
    elif auxiliar == "2":
        limpatela()
        saldo, extrato, numero_saques = menu2(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES) #passagem de valores por nomeaç
    elif auxiliar == "3":
        limpatela()
        menu3(saldo, extrato=extrato) #passagem de valores por posição e nomeação
    elif auxiliar == "4":
        limpatela()
        conta = menu4(AGENCIA, numeroConta, usuarios)

        if (conta):#verifica se não ocorreu o retorno de contas vazias
            contas.append(conta)
            numeroConta+=1
    elif auxiliar == "5":
        limpatela()
        menu5(contas)
    elif auxiliar == "6":
        limpatela()
        menu6(usuarios)
    elif auxiliar == "7":
        limpatela()
        menu7(contas, contasInativas)
    elif auxiliar == "8":
        limpatela()
        menu8(contasInativas)
    elif auxiliar == "9":
        limpatela()
        menu9(contas, contasInativas)
    elif auxiliar == "10":
        break
    else:
        print("Operação inválida, selecione novamente a opção desejada")
