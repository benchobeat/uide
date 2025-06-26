"""
nombre = "Bienvenidos a la UIDE"    ## Variable de tipo cadena
print(nombre)                       ## Imprime el mensaje en la consola
"""
"""
print("Ingrese su nombre: ")                                                            ## Solicita al usuario que ingrese su nombre
nombre = input("Cual es tu nombre:")                                                    ## Captura el nombre ingresado por el usuario 
edad = input("Cual es tu edad:")                                                        ## Captura la edad ingresada por el usuario
print("Tu nombre es: " + nombre + ", tu edad es" + edad + ", bienvenido a la UIDE")     ## Imprime el nombre ingresado
"""
"""a = int(input(" Ingrese un numero: "))                  ## Solicita al usuario que ingrese un numero y lo convierte a entero
if a % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
"""
"""
a = float(input(" Ingrese un primer numero: "))
b = float(input(" Ingrese un segundo numero: "))
c = float(input(" Ingrese un tercer numero: "))

if a > b and a > c:
    print("El numero mayor es: " + str(a))
elif b > a and b > c:
        print("El numero mayor es: " + str(b))
else:
        print("El numero mayor es: " + str(c))
"""
"""
import random
# Generar un número aleatorio entre 1 y 100
numero_ganador = random.randint(1, 100)
intentos = 0
while True:
    try:
        # Pedir al usuario que ingrese un número
        intento = int(input("\nIngresa tu intento: "))
        intentos += 1
            
        # Verificar el intento
        if intento < numero_ganador:
            print("El número es mayor. ¡Sigue intentando!")
        elif intento > numero_ganador:
            print("El número es menor. ¡Sigue intentando!")
        else:
            print(f"\n¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")
"""
x = 0 

while x <= 100: 

    print(x) 

    x += 1 

    if x == 50: 

        break 

print("Bucle completado") 
"""edad = int(input("Ingresa tu edad: "))

if edad >= 65:
    print("Eres adulto mayor")
else:
    if edad >= 18:
        print("Eres adulto")
    else:
        if edad >= 12:
            print("Eres adolescente")
        else:
            if edad >= 1:
                print("Eres niño")
            else:
                print("Edad no valida")
"""
                
"""b = int(input(" Ingrese otro numero: "))                 ## Solicita al usuario que ingrese otro numero y lo convierte a entero 
c = int(input(" Ingrese otro numero: "))
suma = a + b                                        ## Suma los dos numeros ingresados
print("La suma de los numeros es: " + str(suma)) 5   ## Imprime la suma de los numeros ingresados, convirtiendo el resultado a cadena  
11"""



