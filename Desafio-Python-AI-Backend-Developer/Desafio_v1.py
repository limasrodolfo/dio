def mostrar_menu():
    menu = """
    [1] Deposito
    [2] Sacar
    [3] Extrato
    [0] Sair

    => """
    return input(menu)

def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R$ {valor:.2f} realizado\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou, o valor informado é inválido")

    return saldo, extrato

def saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente!")

    elif excedeu_limite:
        print("Valor do saque excede o limite")

    elif excedeu_saques:
        print("Quantidade de saques excedida")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f} realizado\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou, o valor informado é inválido")

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")

    if not extrato:
        print("Não foram realizadas movimentações")

    else:
        print(extrato)
        
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================\n")

def main():
    saldo, limite, extrato, numero_saques, LIMITE_SAQUES = 0, 500, "", 0, 3

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

        elif opcao == "3":
            mostrar_extrato(saldo, extrato)

        elif opcao == "0":
            print("Saindo... Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()