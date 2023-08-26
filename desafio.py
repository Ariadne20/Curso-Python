menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao =="d":
        print("Depósito")
        valor = float(input('Informe o valor que deseja depositar: '))
        if(valor>0):
            saldo +=valor
            extrato += (f'Depósito no valor de R${valor:.2f}.\n')
            print(f'Depósito no valor de R${valor:.2f} realizado com sucesso')
        else:
            print('Não é possível realizar o depósito no valor informado')

    elif opcao =="s":
        print("Saque")
        valor = float(input('Informe o valor que deseja sacar: '))
        if(valor>limite):
            print('Não é possível realizar o saque, pois, o valor solicitado é maior que o limite disponibilizado')
        elif(numero_saques>=LIMITE_SAQUES):
            print('Não é possível realizar o saque, pois, o número limite de saques diários já foi atingido')
        elif(valor>saldo):
            print('Não é possível realizar o saque, pois, o valor solicitado é maior que o saldo disponível')
        elif(valor<=0):
            print('Não é possível realizar o saque no valor informado')
        else:
            saldo -=valor
            extrato += (f'Saque no valor de R${valor:.2f}. \n')
            numero_saques += 1
            print(f'Saque no valor de R${valor:.2f} realizado com sucesso')

    elif opcao =="e":
        if(extrato != ''):
            print('==================EXTRATO================== \n')
            print(extrato)
            print(f'Saldo atual: R${saldo:.2f} \n')
            print('===========================================')
        else:
            print('Não foram realizadas movimentações')
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")