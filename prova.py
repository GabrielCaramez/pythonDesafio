total_peso = 0
menos_70kg = 0

for i in range(1, 26):
    while True:
        try:
            peso = float(input(f"Digite o peso da pessoa {i}: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número válido para o peso.")
    total_peso += peso
    if peso < 70:
        menos_70kg += 1

print(f"\nSoma total dos pesos: {total_peso:.2f} kg")
print(f"Quantidade de pessoas com menos de 70 kg: {menos_70kg}")