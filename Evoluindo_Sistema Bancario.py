def exibir_menu():
    menu = """\
 MENU 
[d]Depositar
[s]Sacar
[e]Extrato
[nc]Nova conta
[lc]Listar contas
[nu]Novo usuário
[q]Sair
=> """
    return input(menu)


def efetuar_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito efetuado! Valor: R$ {valor:.2f}\n"
        print("\nDepósito concluído")
    else:
        print("\nOperação falhou! O valor inserido é inválido.")

    return saldo, extrato


def sacar_recursos(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! Valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque efetuado! Valor: R$ {valor:.2f}\n"
        num_saques += 1
        print("\nSaque realizado")

    else:
        print("\nOperação falhou! O valor inserido é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("Nenhuma transação registrada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
  
def cadastrar_usuario(usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (rua, nº - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")


def encontrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def abrir_conta(ramo, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"ramo": ramo, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado. Processo de abertura de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        dados = f"""\
Ramo: {conta['ramo']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
"""
        print(dados)


def main():
    LIMITE_SAQUES = 3
    RAMO = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = efetuar_deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar_recursos(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = abrir_conta(RAMO, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida. Por favor, selecione uma opção válida.")


main()
