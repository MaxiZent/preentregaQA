# Definimos las variables y solicitamos los datos al usuario
nombre = input("Por favor, ingresá tu nombre: ")
edad = input("¿Cuántos años tenés? ")
profesion = input("¿Cuál es tu profesión? ")

# Imprimimos el mensaje personalizado
print(f"\n¡Hola {nombre}! Tenés {edad} años y trabajás como {profesion}. ¡Gracias por compartir tus datos!")

# Inicializamos un contador
contador = 0
numero = 0

print("Los primeros 10 números pares son:")

# Usamos un bucle while para encontrar los primeros 10 pares
while contador < 10:
    if numero % 2 == 0:
        print(numero)
        contador += 1
    numero += 1


