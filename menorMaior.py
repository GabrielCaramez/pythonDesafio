# Programa para encontrar o menor e o maior valor de um conjunto de inteiros usando array (lista)

valores = []

while True:
    try:
        valor = int(input("Digite um valor inteiro (0 para sair): "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    if valor == 0:
        break

    valores.append(valor)

if not valores:
    print("Nenhum valor foi informado.")
else:
    menor = sorted(valores)[0]
    maior = sorted(valores)[-1]
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")