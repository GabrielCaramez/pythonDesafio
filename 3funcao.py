def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def main():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print(f"Soma: {soma(x, y)}")
    print(f"Subtração: {subtrai(x, y)}")

if __name__ == "__main__":
    operacao = input("Escolha a operação (+ para soma, - para subtração): ")
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    if operacao == "+":
        print(f"Soma: {soma(x, y)}")
    elif operacao == "-":
        print(f"Subtração: {subtrai(x, y)}")
    else:
        print("Operação inválida.")