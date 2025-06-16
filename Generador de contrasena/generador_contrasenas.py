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
    
    Returns:
        str: La opción seleccionada por el usuario ('1', '2' o '3')
    """
    print("\n=== Generador de Contraseñas ===")
    print("1. Generar por Nivel de Seguridad")
    print("2. Personalizar configuración")
    print("3. Salir")
    return input("Seleccione una opción: ")

def configurar_nivel_seguridad():
    """
    Muestra el menú de niveles de seguridad y devuelve la configuración correspondiente.
    
    Returns:
        tuple: Una tupla con la cantidad de (minúsculas, mayúsculas, números, especiales)
              según el nivel de seguridad seleccionado.
    """
    print("\nSeleccione el nivel de seguridad:")
    print("1. Bajo")
    print("2. Medio")
    print("3. Alto")
    
    nivel = input("Opción: ")
    
    if nivel == "1":
        return 6, 0, 2, 0  # minúsculas, mayúsculas, números, especiales
    elif nivel == "2":
        return 5, 2, 3, 2
    elif nivel == "3":
        return 7, 3, 3, 3
    else:
        print("Opción no válida. Usando nivel Medio por defecto.")
        return 5, 2, 3, 2

def configurar_personalizado():
    """
    Solicita al usuario que ingrese la cantidad deseada de cada tipo de carácter.
    
    Returns:
        tuple: Una tupla con la cantidad de (minúsculas, mayúsculas, números, especiales)
              ingresados por el usuario. Retorna (0,0,0,0) si hay algún error.
    """
    try:
        minu = int(input("Cantidad de minúsculas: "))
        mayu = int(input("Cantidad de mayúsculas: "))
        num = int(input("Cantidad de números: "))
        esp = int(input("Cantidad de caracteres especiales: "))
        return minu, mayu, num, esp
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
        return 0, 0, 0, 0


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
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            continue
        
        # Verificar que se hayan ingresado valores válidos
        if minu + mayu + num + esp > 0:
            # Aqui debemos llamar a nuestra futura función
            print("Generando contraseña. Minúsculas: "+str(minu)+" Mayúsculas: "+str(mayu)+" Números: "+str(num)+" Caracteres especiales: "+str(esp))
            
        else:
            print("No se pudo generar la contraseña. Verifique los valores ingresados.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
