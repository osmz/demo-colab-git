def sumar(a, b):
    return a + b

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = sumar(num1, num2)
    print(f"La suma es: {resultado}")

if __name__ == "__main__":
    main()