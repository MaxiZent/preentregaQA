# CALCULADORA BÁSICA LINEAL

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("❌ Error: No se puede dividir por cero.")
        return None

# Diccionario de operaciones
operaciones = {
    '1': ('Sumar', sumar),
    '2': ('Restar', restar),
    '3': ('Multiplicar', multiplicar),
    '4': ('Dividir', dividir)
}

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingresá un número.")

def calculadora():
    print("\n🧮 --- CALCULADORA PYTHON ---")
    while True:
        try:
            a = pedir_numero("Primer número: ")
            b = pedir_numero("Segundo número: ")

            print("\nOperaciones disponibles:")
            for clave, (nombre, _) in operaciones.items():
                print(f"{clave}) {nombre}")

            opcion = input("Elegí una opción (1-4): ")

            if opcion in operaciones:
                nombre_op, funcion = operaciones[opcion]
                resultado = funcion(a, b)
                if resultado is not None:
                    print(f"✅ Resultado de {nombre_op}: {resultado}\n")
            else:
                print("⚠️ Opción inválida.\n")

        except Exception as e:
            print(f"❌ Error inesperado: {e}")

        finally:
            print("✅ Operación finalizada.\n")

        repetir = input("¿Querés hacer otra operación? (s/n): ").lower()
        if repetir != 's':
            print("👋 ¡Gracias por usar la calculadora!")
            break

if __name__ == '__main__':
    calculadora()