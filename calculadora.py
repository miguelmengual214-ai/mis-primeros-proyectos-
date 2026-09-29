print("--- Calculadora de Miguel ---")
nombre = input("¿Cómo te llamas? ")

try:
    n1 = float(input("Dame el primer número: "))
    n2 = float(input("Dame el segundo número: "))

    print(f"\nListo {nombre}, resultados:")
    print(f"Suma: {n1 + n2}")
    print(f"Resta: {n1 - n2}")
    print(f"Multiplicación: {n1 * n2}")
    
    if n2 != 0:
        print(f"División: {n1 / n2}")
    else:
        print("División: No se puede dividir por 0")

except:
    print("Uy, pon solo números porfa")

print("\n¡Primer proyecto listo!")