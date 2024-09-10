# Programa que calcula temperatura 
while True:
    # Pedir la temperatura inicial y final en grados centígrados
    temp_inicial = int(input("Introduce la temperatura inicial en grados centígrados: "))
    temp_final = int(input("Introduce la temperatura final en grados centígrados: "))

    print("\nConversión de grados Centígrados a Fahrenheit:")

    # Ciclo para realizar la conversión desde temp_inicial hasta temp_final
    for temp_c in range(temp_inicial, temp_final + 1):
        # Convertir de Centígrados a Fahrenheit
        temp_f = (temp_c * 9/5) + 32
        print(f"{temp_c}°C = {temp_f:.2f}°F")

    # Preguntar si el usuario desea repetir el proceso
    repetir = input("\n¿Quieres repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break

print("Programa finalizado.")
