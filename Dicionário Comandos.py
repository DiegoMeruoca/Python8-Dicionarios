tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}  # Gera a "Tabela"
print(tabela)  # imprime a tabela toda
print("1"+"="*100)  # Divisor
print(tabela["Tomate"])  # Iprime só o preço do tomate
print("2"+"="*100)  # Divisor
tabela["Tomate"] = 2.50  # Altera o preço do tomate para 2.50, pois ja existia a chave "Tomate"
print(tabela)
print("3"+"="*100)  # Divisor
tabela["Cebola"] = 1.20  # Adiciona Cebola 1.20 na tabela, pois a chave "Cebola" não existia
print(tabela)
print("4"+"="*100)  # Divisor
# print(tabela["Manga"])->Esse comando da um erro 'KeyError', pois a chave "Manga" não está na tabela
print("Manga" in tabela)  # Imprime True se a chave Manga estiver na tabela ou False se não estiver
print("5"+"="*100)  # Divisor
print(tabela.keys())  # Imprime as chaves
print(tabela.values())  # Imprime os valores
print("6"+"="*100)  # Divisor
del(tabela["Tomate"])
print(tabela)
print("7"+"="*100)
tabela2 = {"Alface": [1000, 0.45],
           "Batata": [500, 1.20],
           "Tomate": [200, 2.30],
           "Feijão": [100, 1.50]}
# Gera a "Tabela" utilizando lista nos valores
print(tabela2)

