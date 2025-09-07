txt_menu = """
[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

MAX_VALOR_SAQUE = 500
MAX_SAQUES_DIARIO = 3

saldo = 0
extrato = ""
num_saque = 0
valor_saque = 0
valor_deposito = 0

def autentica_valor(funcao):
    while True:
        try:
            valor = float(input(f"Digito o valor para {funcao}: "))
            if valor > 0:
                return valor
            else:
                print("Valor invalido, digite um valor maior do zero \n")
        except:
            print("Valor invalido, tente novamente. \n") 
           
def autentica_saque():
    global saldo, num_saque, MAX_SAQUES_DIARIO, MAX_VALOR_SAQUE
    while True:
        
        valor = autentica_valor('saque')

        if valor <= MAX_VALOR_SAQUE and saldo >= valor and num_saque < MAX_SAQUES_DIARIO:
            num_saque += 1
            return valor
            break

        elif valor > MAX_VALOR_SAQUE :
            print(F"Valor ultrapassa o valor limite de saque, que é de {MAX_VALOR_SAQUE} \n")

        elif saldo < valor :
            print(F"Saldo insuficiente, seu saldo atual é de {saldo} \n")
            escolha =  input("Deseja depositar [s/n]: \n").lower()
            match escolha:
                case "s":
                    deposito()
                case "n":
                    print('\n')
                    continue
        
        elif num_saque >= MAX_SAQUES_DIARIO :
            print(F"Limite de saques ultrassado, que é de {MAX_SAQUES_DIARIO}, tente novamente amanha.")
            menu()

def deposito():
    global saldo, valor_deposito, extrato

    valor =  float(autentica_valor("deposito"))
    saldo += valor
    valor_deposito += valor


    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f'Depósito realizado com sucesso, seu saldo é de: R$ {saldo:.2f}')

def saque():
    global valor_saque, saldo, extrato
    valor = float(autentica_saque())
        
    saldo -= valor
    valor_saque += valor

    extrato += f"Saque: R$ {valor:.2f}\n"
    print(f'Saque realizado com sucesso, seu saldo é de: R$ {saldo:.2f}')

def exibe_saque():
    txt = ' EXTRATO '

    print(txt.center(35,"="))
    print(f'\nMovimentações realizadas: \n{extrato}\n')

    print(f"Total depositado: {valor_deposito:.2f}")
    print(f"Total sacado: {valor_saque:.2f}")
    print(f"Saldo atual: {saldo:.2f} \n")
    print("="*35)

    menu()


def menu():
    global txt_menu
    while True:
        opcao = input(txt_menu).lower()
        
        match opcao:
            case "d":
                deposito()
            case "s":
                saque()
            case "e":
                exibe_saque()
            case "q":
                print('Encerrando programa ...')
                break
            case _:
                print('Opcão inválida, favor tentar novamente')

menu()
        