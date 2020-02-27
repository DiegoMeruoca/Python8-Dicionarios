estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [2001, 1.20],
           "Feijão": [100, 1.50]}  # cria estoque
venda = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]  # cria a lista de itens vendidos
total = 0
print("="*100)
print("Vendas:")
for operacao in venda:  # Para cada Operação nalista venda
    produto, quantidade = operacao
    # lê a lista de vendas setando o produto e quantidade de acordo com a posição apontada pela operação(0,1,2)
    preco = estoque[produto][1]
    # Busca no dicionário estoque o preço do produto indicado informando o produto obtido na lista vendas
    # e a coluna 1 que representa o preço
    custo = preco * quantidade  # Calcula o custo do produto com base no preço e na quantidade
    print("%10s: %d X %6.2f = %6.2f" % (produto, quantidade, preco, custo))
    # imprime as informações do produto atual do laço de repetição
    estoque[produto][0] -= quantidade
    # Acessa o produto na tabela estoque e altera seu campo 0 (quantidade) subtraindo a quantidade comprada
    total += custo  # Acrescenta o custo obtido ao total
print("Custo total: %6.2f\n" % total)  # Imprime o total
print("="*100)
print("Estoque:\n")
for chave, dados in estoque.items():  # Para cada chave e dado nos itens do Dicionário estoque
    print("Descrição: ", chave)  # Imprime a chave
    print("Quantidade: ", dados[0])  # Imprime o dado na posição 0
    print("Preço: %6.2f\n" % dados[1])  # Imprime o dado na posição 1
