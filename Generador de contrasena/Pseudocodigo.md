# 🔐 Generador de Contraseñas Seguras – Pseudocódigo

Este pseudocódigo representa el flujo de un programa que genera contraseñas seguras según nivel de seguridad o configuración personalizada.

---

## 📌 Constantes
```pseudocode
CONSTANTE MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
CONSTANTE MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CONSTANTE NUMEROS = "0123456789"
CONSTANTE ESPECIALES = "!@#$%^&*()_+-=[]{}|;:,.<>?"
```

## 📌 Variables
```pseudocode
VARIABLE eleccion_usuario: CADENA
VARIABLE nivel_seguridad: CADENA

VARIABLE num_minusculas: ENTERO
VARIABLE num_mayusculas: ENTERO
VARIABLE num_numeros: ENTERO
VARIABLE num_especiales: ENTERO

VARIABLE lista_caracteres: LISTA DE CARACTERES
VARIABLE contrasena_final: CADENA
```

---

## ▶️ Inicio del Proceso
```pseudocode
INICIO

MOSTRAR "Seleccione el modo de generación:"
MOSTRAR "1 - Por Nivel de Seguridad"
MOSTRAR "2 - Personalizado"
LEER eleccion_usuario
```

---

## 🔀 Condicional Principal
```pseudocode
SI eleccion_usuario == "1" ENTONCES
    MOSTRAR "Seleccione el nivel: Bajo, Medio, Alto"
    LEER nivel_seguridad

    SEGUN nivel_seguridad HACER
        CASO "Bajo":
            num_minusculas ← 6
            num_mayusculas ← 0
            num_numeros    ← 2
            num_especiales ← 0
        CASO "Medio":
            num_minusculas ← 5
            num_mayusculas ← 2
            num_numeros    ← 3
            num_especiales ← 2
        CASO "Alto":
            num_minusculas ← 7
            num_mayusculas ← 3
            num_numeros    ← 3
            num_especiales ← 3
        POR DEFECTO:
            MOSTRAR "Error: Nivel no válido."
            TERMINAR
    FIN_SEGUN

SINO SI eleccion_usuario == "2" ENTONCES
    MOSTRAR "Ingrese la cantidad de minúsculas:"
    LEER num_minusculas
    MOSTRAR "Ingrese la cantidad de mayúsculas:"
    LEER num_mayusculas
    MOSTRAR "Ingrese la cantidad de números:"
    LEER num_numeros
    MOSTRAR "Ingrese la cantidad de caracteres especiales:"
    LEER num_especiales

SINO
    MOSTRAR "Error: Opción no válida."
    TERMINAR
FIN_SI
```

---

## ⚙️ Generación de Caracteres
```pseudocode
lista_caracteres ← lista vacía

PARA i DESDE 1 HASTA num_minusculas HACER
    caracter ← SELECCIONAR_ALEATORIO(MINUSCULAS)
    AGREGAR caracter A lista_caracteres
FIN_PARA

PARA i DESDE 1 HASTA num_mayusculas HACER
    caracter ← SELECCIONAR_ALEATORIO(MAYUSCULAS)
    AGREGAR caracter A lista_caracteres
FIN_PARA

PARA i DESDE 1 HASTA num_numeros HACER
    caracter ← SELECCIONAR_ALEATORIO(NUMEROS)
    AGREGAR caracter A lista_caracteres
FIN_PARA

PARA i DESDE 1 HASTA num_especiales HACER
    caracter ← SELECCIONAR_ALEATORIO(ESPECIALES)
    AGREGAR caracter A lista_caracteres
FIN_PARA
```

---

## 🔄 Mezcla y Ensamblaje
```pseudocode
MEZCLAR lista_caracteres ALEATORIAMENTE
contrasena_final ← UNIR(lista_caracteres)

MOSTRAR "Su contraseña generada es: " + contrasena_final
FIN
```