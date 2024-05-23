def mostrar_menu():
    menu = """
    [1] Deposito
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    => """
    return input(menu)

def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R$ {valor:.2f} realizado\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou, o valor informado é inválido")

    return saldo, extrato

def saque(*, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
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

def mostrar_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")

    if not extrato:
        print("Não foram realizadas movimentações")

    else:
        print(extrato)
        
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================\n")

def buscar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (xxx.xxx.xxx.xx): ")
    cpf = cpf.translate(str.maketrans('', '', '.-'))
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe cadastro para o CPF informado!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe o nome da rua (sem o número):")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe a sigla do estado: ")
    endereco = (f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })

    print("Usuário criado")

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF (xxx.xxx.xxx.xx): ")
    cpf = cpf.translate(str.maketrans('', '', '.-'))
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\nconta criada!")
        return {"AGENCIA": AGENCIA, "numero_conta" : numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado em nossa base de dados, favor realizar um cadastro!")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agência:{conta['AGENCIA']}
            Conta:{conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(f"\n{linha}")

def main():
    LIMITE_SAQUES, AGENCIA = 3, "0001"
    saldo, limite, extrato, numero_saques, numero_conta = 0, 500, "", 3, 1
    usuarios, contas = [], []

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo... Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()