import fractions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Fehler: Division durch Null"
    return a / b

def add_fractions(a, b):
    return a + b

def subtract_fractions(a, b):
    return a - b

def multiply_fractions(a, b):
    return a * b

def divide_fractions(a, b):
    if b == 0:
        return "Fehler: Division durch Null"
    return a / b

def main():
    print("Einfacher Rechner")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("5. Brüche Addieren")
    print("6. Brüche Subtrahieren")
    print("7. Brüche Multiplizieren")
    print("8. Brüche Dividieren")

    wahl = input("Wählen Sie eine Option (1/2/3/4/5/6/7/8): ")

    if wahl in ['1', '2', '3', '4']:
        num1 = float(input("Geben Sie die erste Zahl ein: "))
        num2 = float(input("Geben Sie die zweite Zahl ein: "))

        if wahl == '1':
            print(f"Das Ergebnis ist: {add(num1, num2)}")
        elif wahl == '2':
            print(f"Das Ergebnis ist: {subtract(num1, num2)}")
        elif wahl == '3':
            print(f"Das Ergebnis ist: {multiply(num1, num2)}")
        elif wahl == '4':
            print(f"Das Ergebnis ist: {divide(num1, num2)}")

    elif wahl in ['5', '6', '7', '8']:
        num1 = fractions.Fraction(input("Geben Sie den ersten Bruch ein (z.B., 1/2): "))
        num2 = fractions.Fraction(input("Geben Sie den zweiten Bruch ein (z.B., 1/3): "))

        if wahl == '5':
            print(f"Das Ergebnis ist: {add_fractions(num1, num2)}")
        elif wahl == '6':
            print(f"Das Ergebnis ist: {subtract_fractions(num1, num2)}")
        elif wahl == '7':
            print(f"Das Ergebnis ist: {multiply_fractions(num1, num2)}")
        elif wahl == '8':
            print(f"Das Ergebnis ist: {divide_fractions(num1, num2)}")

    else:
        print("Ungültige Eingabe")

if __name__ == "__main__":
    main()