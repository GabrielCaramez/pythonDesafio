def maximo(a: int, b: int) -> int:
    if a >= b:
        return a
    else:
        return b
def minimo(a: int, b: int) -> int:
        if a <= b:
            return a
        else:
            return b
if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print(f"Maior: {maximo(x, y)}")
    print(f"Menor: {minimo(x, y)}")
