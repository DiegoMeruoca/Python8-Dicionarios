tabimc = {"Muito abaixo do peso": [0.00, 17.00],
          "Abaixo do peso": [17.10, 18.49],
          "Peso normal": [18.50, 24.99],
          "Acima do peso": [25.00, 29.00],
          "Obesidade I": [30.00, 34.99],
          "Obesidade II (severa)": [35.00, 39.99],
          "Obesidade III (mórbida)": [40.00, 1000.00]}

altura = (float(input("Digite sua altura em metros:")))
peso = float(input("Digite seu peso em quilogramas:"))
imc = peso / (altura * altura)
for chave, dados in tabimc.items():  # Para cada chave e dado nos itens do Dicionário imc
    if dados[0] <= imc <= dados[1]:
        print("Seu IMC é %5.2f, portanto seus tatus é: %s" % (imc, chave))
