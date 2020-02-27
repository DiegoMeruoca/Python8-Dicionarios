def imprime_estoque():
    print("="*100)
    print("Estoque Atual:\n")
    for chave, dados in estoque.items():  # Para cada chave e dado nos itens do Dicionário estoque
        print("Descrição: ", chave)  # Imprime a chave
        print("Quantidade: ", dados[0])  # Imprime o dado na posição 0
        print("Preço: %6.2f\n" % dados[1])  # Imprime o dado na posição 1
    print("=" * 100)


def compra_produto(p):
    quantidade = int(input("Digite a quantidade deste produto: "))
    preco = estoque[p][1]
    # Busca no dicionário estoque o preço do produto indicado informando o produto obtido na lista vendas
    # e a coluna 1 que representa o preço
    c = preco * quantidade  # Calcula o custo do produto com base no preço e na quantidade
    print("%10s: %d X %6.2f = %6.2f" % (p, quantidade, preco, c))
    # imprime as informações do produto atual do laço de repetição
    estoque[produto][0] -= quantidade
    # Acessa o produto na tabela estoque e altera seu campo 0 (quantidade) subtraindo a quantidade comprada
    return c  # Acrescenta o custo obtido ao total


# Inicio do programa principal
estoque = {"Tomate": [100, 2.30],
           "Alface": [150, 0.45],
           "Batata": [200, 1.20],
           "Feijão": [100, 1.50]}  # cria estoque
total = 0
imprime_estoque()
while True:
    produto = input("Digite o produto comprado, ou digite fim para sair: ").capitalize()
    if produto.upper() == "FIM":
        break
    elif produto in estoque:
        custo = compra_produto(produto)
        total += custo
    else:
        print("Este produto não faz parte do nosso estoque!")
if total != 0:
    print("=" * 100)
    print("Custo total: %6.2f" % total)  # Imprime o total
    print("=" * 100)
op = input("Deseja visualizar o estoque atualizado? Digite Sim ou Não: ").upper()
if op.upper() == "SIM":
    imprime_estoque()
print("Obrigado! Volte sempre!!!")
