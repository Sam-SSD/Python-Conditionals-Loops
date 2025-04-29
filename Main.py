import random


# Ejercicios de condicionales y bucles en Python

# Ejercicio 1: Clasificador de números
def clasificador_numero():
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es cero.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")


# Ejercicio 2: Aprobado o reprobado
def aprobado_reprobado():
    try:
        calificacion = float(input("Ingrese la calificación del estudiante (0 a 100): "))
        if 0 <= calificacion < 60:
            print("Reprobado")
        elif 60 <= calificacion <= 100:
            print("Aprobado")
        else:
            print("Calificación fuera de rango. Debe estar entre 0 y 100.")
    except ValueError:
        print("Por favor, ingrese una calificación válida.")


# Ejercicio 3: Tabla de multiplicar
def tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Por favor, ingrese un número válido.")


# Ejercicio 4: Contador regresivo
def contador_regresivo():
    try:
        numero = int(input("Ingrese un número positivo para iniciar la cuenta regresiva: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        while numero >= 0:
            print(numero)
            numero -= 1
    except ValueError:
        print("Por favor, ingrese un número válido.")


# Ejercicio 5: Adivina el número
def adivina_numero():
    numeroRandom = random.randint(1, 10)
    intentos = 3
    print("Adivina el número entre 1 y 10. Tienes 3 intentos.")

    while intentos > 0:
        try:
            adivinanza = int(input("Ingrese su adivinanza: "))
            if adivinanza < 1 or adivinanza > 10:
                print("Por favor, ingrese un número entre 1 y 10.")
                continue

            if adivinanza == numeroRandom:
                print("¡Correcto! Has adivinado el número.")
                break
            elif adivinanza < numeroRandom:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            intentos -= 1
            if intentos == 0:
                print(f"Lo siento, has agotado tus intentos. El número era {numeroRandom}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


# Menú de opciones
def menu():
    while True:
        print("\n----------Menú de opciones----------")
        print("Seleccione una opción:")
        print("1. Clasificador de números")
        print("2. Aprobado o reprobado")
        print("3. Tabla de multiplicar")
        print("4. Contador regresivo")
        print("5. Adivina el número")
        print("6. Salir")
        print("-----------------------------------")

        opcion = input("Ingrese su opción: ")
        return opcion


# Programa principal
print("----------Bienvenido al programa de ejercicios de Python----------")
while True:
    try:
        opcion = menu()
        if opcion == '1':
            clasificador_numero()
        elif opcion == '2':
            aprobado_reprobado()
        elif opcion == '3':
            tabla_multiplicar()
        elif opcion == '4':
            contador_regresivo()
        elif opcion == '5':
            adivina_numero()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
    except ValueError:
        print("Opción no válida, intente nuevamente.")

print("----------Gracias por usar el programa----------")
