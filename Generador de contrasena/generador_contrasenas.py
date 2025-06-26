# Módulos necesarios
import random  # Para generar números aleatorios y mezclar caracteres
import string  # Para trabajar con cadenas de caracteres predefinidas

# Constantes globales para los conjuntos de caracteres
MINUSCULAS = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
MAYUSCULAS = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMEROS = string.digits             # '0123456789'
ESPECIALES = '!@#$%^&*()_+-=[]{}|;:,.<>?'  # Caracteres especiales comunes

def mostrar_menu():
    """
    Muestra el menú principal del programa y devuelve la opción seleccionada por el usuario.
    """
    print("\n=== Generador de Contraseñas ===")
    print("1. Generar por Nivel de Seguridad")
    print("2. Personalizar configuración")
    print("3. Salir")
    return input("Seleccione una opción: ")

def configurar_nivel_seguridad():
    """
    Muestra el menú de niveles de seguridad y devuelve la configuración correspondiente.
    """
    print("\nSeleccione el nivel de seguridad:")
    print("1. Bajo")
    print("2. Medio")
    print("3. Alto")
    
    nivel = input("Opción: ")
    
    if nivel == "1":
        return 8, 2, 3, 1  # Básico: 14 caracteres
    elif nivel == "2":
        return 10, 3, 4, 3  # Medio: 20 caracteres
    elif nivel == "3":
        return 12, 4, 5, 3  # Alto: 24 caracteres
    else:
        print("Opción no válida. Usando nivel Medio por defecto.")
        return 10, 3, 4, 3  # Nivel medio por defecto: 20 caracteres

def configurar_personalizado():
    """
    Solicita al usuario que ingrese la cantidad deseada de cada tipo de carácter.
    """
    while True:
        try:
            minu = int(input("Cantidad de minúsculas (0-64): "))
            if minu < 0:
                print("Error: El número no puede ser negativo.\n")
                continue
                
            mayu = int(input("Cantidad de mayúsculas (0-64): "))
            if mayu < 0:
                print("Error: El número no puede ser negativo.\n")
                continue
                
            num = int(input("Cantidad de números (0-64): "))
            if num < 0:
                print("Error: El número no puede ser negativo.\n")
                continue
                
            esp = int(input("Cantidad de caracteres especiales (0-64): "))
            if esp < 0:
                print("Error: El número no puede ser negativo.\n")
                continue
            
            total = minu + mayu + num + esp
            
            if total > 64:
                print(f"\nError: La suma total de caracteres es {total}, pero el máximo permitido es 64.")
                print(f"Por favor, ingrese valores que sumen 64 o menos.\n")
                continue
                
            if total < 6:
                print("\nError: La contraseña debe tener al menos 6 caracteres.")
                print(f"Total actual: {total} caracteres. Por favor, ingrese más caracteres.\n")
                continue
                
            return minu, mayu, num, esp
            
        except ValueError:
            print("\nError: Por favor ingrese solo números enteros.\n")
            
        # Si llegamos aquí, hubo un error inesperado
        print("\nError inesperado. Volviendo al menú principal.")
        return 0, 0, 0, 0

def generar_contrasena(minu, mayu, num, esp):
    """
    Genera una contraseña con la cantidad especificada de cada tipo de carácter.
    """
    # Generar los caracteres de cada tipo
    caracteres = []
    caracteres.extend(random.choice(MINUSCULAS) for _ in range(minu))
    caracteres.extend(random.choice(MAYUSCULAS) for _ in range(mayu))
    caracteres.extend(random.choice(NUMEROS) for _ in range(num))
    caracteres.extend(random.choice(ESPECIALES) for _ in range(esp))
    
    # Mezclar los caracteres para mayor aleatoriedad
    random.shuffle(caracteres)
    
    # Unir los caracteres en una cadena
    contrasena = ''.join(caracteres)
    
    # Asegurarse de que la contraseña no exceda 64 caracteres (por si acaso)
    return contrasena[:64]


def preguntar_otra_vez():
    """
    Pregunta al usuario si desea generar otra contraseña.
    
    Returns:
        bool: True si el usuario quiere generar otra contraseña, False en caso contrario.
    """
    while True:
        respuesta = input("\n¿Desea generar otra contraseña? (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor, responda con 's' para sí o 'n' para no.")

def main():
    """
    Función principal que maneja el flujo del programa.
    Muestra el menú, procesa la selección del usuario y genera las contraseñas
    hasta que el usuario decida salir.
    """
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            minu, mayu, num, esp = configurar_nivel_seguridad()
        elif opcion == "2":
            minu, mayu, num, esp = configurar_personalizado()
        elif opcion == "3":
            print("\n¡Hasta luego!")
            return  # Salir de la función main
        else:
            print("Opción no válida. Intente nuevamente.")
            continue
        
        # Verificar que se hayan ingresado valores válidos
        total_caracteres = minu + mayu + num + esp
        if total_caracteres >= 6:  # Mínimo 6 caracteres
            print(f"\nConfiguración de la contraseña:")
            print(f"- Minúsculas: {minu}")
            print(f"- Mayúsculas: {mayu}")
            print(f"- Números: {num}")
            print(f"- Caracteres especiales: {esp}")
            print(f"- Longitud total: {total_caracteres} caracteres")
            
            contrasena = generar_contrasena(minu, mayu, num, esp)
            print(f"\nContraseña generada: {contrasena}")
            print(f"Longitud: {len(contrasena)} caracteres")
            
            # Preguntar si desea generar otra contraseña
            if not preguntar_otra_vez():
                print("\n¡Gracias por usar el generador de contraseñas!")
                return  # Salir del programa
                
            # Si llega aquí, el usuario quiere otra contraseña
            # Volvemos al inicio del bucle principal para mostrar el menú de nuevo
            print("\nVolviendo al menú principal...\n")
        else:
            print("No se pudo generar la contraseña. Verifique los valores ingresados.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
