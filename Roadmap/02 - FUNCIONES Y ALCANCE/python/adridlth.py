# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# Comprueba si puedes crear funciones dentro de funciones.
#  - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  - Debes hacer print por consola del resultado de todos los ejemplos.
# 1. Función sin parámetros y sin retorno
def saludar():
    print("¡Hola mundo!")

# 2. Función con un parámetro y sin retorno
def saludar_persona(nombre):
    print(f"¡Hola {nombre}!")

# 3. Función con múltiples parámetros y sin retorno
def imprimir_datos_persona(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

# 4. Función sin parámetros con retorno
def obtener_fecha_actual():
    from datetime import date
    return date.today()

# 5. Función con un parámetro y retorno
def calcular_cuadrado(numero):
    return numero ** 2

# 6. Función con múltiples parámetros y retorno
def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# 7. Función con parámetros por defecto
def crear_perfil(nombre, edad=18, ciudad="Desconocida"):
    return f"Perfil: {nombre}, {edad} años, de {ciudad}"

# 8. Función con número variable de argumentos
def sumar_numeros(*args):
    return sum(args)

# 9. Función con argumentos nombrados variables
def crear_usuario(**kwargs):
    return kwargs

# Ejemplos de uso:
print("\n--- Ejemplos de uso ---")

# Ejemplo 1
saludar()  # Salida: ¡Hola mundo!

# Ejemplo 2
saludar_persona("Ana")  # Salida: ¡Hola Ana!

# Ejemplo 3
imprimir_datos_persona("Carlos", 25, "Madrid")

# Ejemplo 4
fecha = obtener_fecha_actual()
print(f"Fecha actual: {fecha}")

# Ejemplo 5
resultado = calcular_cuadrado(5)
print(f"El cuadrado de 5 es: {resultado}")  # Salida: 25

# Ejemplo 6
promedio = calcular_promedio(10, 8, 9)
print(f"El promedio es: {promedio}")  # Salida: 9.0

# Ejemplo 7
perfil1 = crear_perfil("Laura")
perfil2 = crear_perfil("Pedro", 25, "Barcelona")
print(perfil1)
print(perfil2)

# Ejemplo 8
suma = sumar_numeros(1, 2, 3, 4, 5)
print(f"La suma es: {suma}")  # Salida: 15

# Ejemplo 9
usuario = crear_usuario(nombre="María", edad=30, email="maria@email.com")
print(usuario)


# Variable global
contador_global = 0

def funcion_externa():
    # Variable local a funcion_externa
    x = 10
    
    def funcion_interna():
        # Variable local a funcion_interna
        y = 5
        print(f"Función interna puede acceder a x: {x}")
        print(f"Variable local y: {y}")
    
    print(f"Variable local x: {x}")
    # No podemos acceder a y aquí porque es local a funcion_interna
    funcion_interna()

# Ejemplo con variable global
def modificar_contador():
    global contador_global
    contador_global += 1
    
    def mostrar_contador():
        print(f"Valor actual del contador global: {contador_global}")
    
    mostrar_contador()

# Ejemplo usando función built-in len()
def procesar_lista(lista):
    def obtener_longitud():
        return len(lista)
    
    def obtener_primero():
        return lista[0] if lista else None
    
    print(f"Longitud de la lista: {obtener_longitud()}")
    print(f"Primer elemento: {obtener_primero()}")

# Ejemplo con closure (función que recuerda valores del entorno)
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    
    return multiplicar

print("\n--- Ejemplo 1: Funciones anidadas básicas ---")
funcion_externa()

print("\n--- Ejemplo 2: Uso de variable global ---")
print(f"Contador inicial: {contador_global}")
modificar_contador()
modificar_contador()
print(f"Contador final: {contador_global}")

print("\n--- Ejemplo 3: Funciones anidadas con built-in ---")
mi_lista = [1, 2, 3, 4, 5]
procesar_lista(mi_lista)
procesar_lista([])  # Lista vacía para probar el caso edge

print("\n--- Ejemplo 4: Closure ---")
multiplicar_por_dos = crear_multiplicador(2)
multiplicar_por_tres = crear_multiplicador(3)

print(f"2 x 5 = {multiplicar_por_dos(5)}")
print(f"3 x 5 = {multiplicar_por_tres(5)}")

# Ejemplo adicional con nonlocal
def contador():
    cuenta = 0
    
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    
    def obtener_valor():
        return cuenta
    
    return incrementar, obtener_valor

print("\n--- Ejemplo 5: nonlocal con múltiples funciones internas ---")
incrementar, obtener = contador()
print(f"Valor inicial: {obtener()}")
print(f"Después de incrementar: {incrementar()}")
print(f"Después de incrementar otra vez: {incrementar()}")
print(f"Valor final: {obtener()}")



# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

def one_to_hundred():
    # Iteramos del 1 al 100
    for n in range(1, 101):
        # Primero verificamos el caso de FizzBuzz (múltiplo de ambos)
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        # Luego verificamos si es múltiplo de 3
        elif n % 3 == 0:
            print("Fizz")
        # Después verificamos si es múltiplo de 5
        elif n % 5 == 0:
            print("Buzz")
        # Si no es múltiplo de ninguno, imprimimos el número
        else:
            print(n)

# Llamamos a la función
one_to_hundred()