def verificasenha(c):
    while True:
        s = int(input("Digite sua senha:"))
        if banco[c][2] == s:
            return True
        else:
            print("Senha errada, tente novamente!")


def saldo(c):
    if verificasenha(c):
        print("=" * 1000)
        print("Seu saldo é R$ %8.2f" % banco[c][1])


def saque(c):
    valor = float(input("Digite o valor a ser sacado: "))
    if verificasenha(c):
        if valor <= banco[c][1]:
            banco[c][1] -= valor
            print("=" * 1000)
            print("Você sacou R$ %8.2f" % valor)
        else:
            print("=" * 1000)
            print("Seu saldo não é suficiente!!!")


def deposito(c):
    valor = float(input("Digite o valor a ser depositado: "))
    if verificasenha(c):
        banco[c][1] += valor
        print("=" * 1000)
        print("Você depositou R$%8.2f" % valor)


# Inicio do programa principal
banco = {1527: ["Peter Oliveira Parker", 140.00, 1234],
         2231: ["Barry Francisco Allen", 1250.00, 4321],
         2971: ["Oliver da Silva Queen", 2200.00, 5678],
         3313: ["Bruce dos Santos Wayne", 2900.00, 8765],
         3327: ["Tony Aparecido Stark", 2500.00, 0000]}

while True:
    conta = int(input("Digite o número de sua conta: "))
    if conta in banco:
        print("=" * 1000)
        print("Bem vindo(a) %s" % banco[conta][0])
        break
    else:
        print("Conta inexistente, tente novamente!")

while True:
    print("="*1000)
    op = int(input("Escolha uma das opções: \n1-Saldo 2-Saque 3-Depósito 4-Sair: "))
    if op == 1:
        saldo(conta)
    elif op == 2:
        saque(conta)
    elif op == 3:
        deposito(conta)
    elif op == 4:
        print("=" * 1000)
        print("Seção encerrada!")
        print("=" * 1000)
        break
    else:
        print("=" * 1000)
        print("Digite uma opção válida!")
