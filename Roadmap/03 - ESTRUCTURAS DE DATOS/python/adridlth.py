# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
# 1. Listas (arrays mutables ordenados)
print("\n--- LISTAS ---")
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

# Inserción
lista.append(6)  # Al final
lista.insert(0, 0)  # En posición específica
print("Después de insertar:", lista)

# Actualización
lista[2] = 20
print("Después de actualizar:", lista)

# Borrado
del lista[0]  # Por índice
lista.remove(6)  # Por valor
ultimo = lista.pop()  # Elimina y retorna el último elemento
print("Después de borrar:", lista)

# Ordenación
lista.sort(reverse=True)  # Descendente
print("Lista ordenada descendente:", lista)

# 2. Tuplas (inmutables)
print("\n--- TUPLAS ---")
tupla = (1, 2, 3, 4, 5)
print("Tupla:", tupla)
# No se pueden modificar, pero se pueden concatenar
nueva_tupla = tupla + (6, 7)
print("Nueva tupla:", nueva_tupla)

# 3. Conjuntos (sets - elementos únicos no ordenados)
print("\n--- CONJUNTOS ---")
conjunto = {1, 2, 3, 4, 5}
print("Conjunto original:", conjunto)

# Inserción
conjunto.add(6)
print("Después de añadir:", conjunto)

# Borrado
conjunto.remove(6)
print("Después de borrar:", conjunto)

# Operaciones de conjunto
otro_conjunto = {4, 5, 6, 7}
print("Unión:", conjunto.union(otro_conjunto))
print("Intersección:", conjunto.intersection(otro_conjunto))

# 4. Diccionarios (pares clave-valor)
print("\n--- DICCIONARIOS ---")
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}
print("Diccionario original:", diccionario)

# Inserción
diccionario["profesion"] = "Programador"
print("Después de insertar:", diccionario)

# Actualización
diccionario["edad"] = 26
print("Después de actualizar:", diccionario)

# Borrado
del diccionario["ciudad"]
print("Después de borrar:", diccionario)

# 5. String (inmutable)
print("\n--- STRINGS ---")
texto = "Python"
print("String original:", texto)

# Operaciones con strings
nuevo_texto = texto.replace("n", "n!")
print("Después de reemplazar:", nuevo_texto)
print("Mayúsculas:", texto.upper())
print("Substring:", texto[1:4])

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de ntactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a ntinuación
#   los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 gitos.
#   (o el número de dígitos que quieras)
# - También se debe proponer una operación de finalización del programa.
def validar_telefono(telefono):
    """Valida que el teléfono sea numérico y tenga máximo 11 dígitos"""
    return telefono.isdigit() and len(telefono) <= 11

def buscar_contacto(agenda, nombre):
    """Busca un contacto por nombre"""
    nombre = nombre.lower()
    return next((contacto for contacto in agenda if contacto["nombre"].lower() == nombre), None)

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    agenda = []
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":  # Añadir contacto
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            
            if not validar_telefono(telefono):
                print("❌ Teléfono inválido. Debe ser numérico y tener máximo 11 dígitos.")
                continue
                
            if buscar_contacto(agenda, nombre):
                print("❌ Ya existe un contacto con ese nombre.")
                continue
                
            agenda.append({"nombre": nombre, "telefono": telefono})
            print("✅ Contacto añadido correctamente.")
            
        elif opcion == "2":  # Buscar contacto
            nombre = input("Nombre a buscar: ")
            contacto = buscar_contacto(agenda, nombre)
            
            if contacto:
                print(f"📞 Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
            else:
                print("❌ Contacto no encontrado.")
                
        elif opcion == "3":  # Actualizar contacto
            nombre = input("Nombre del contacto a actualizar: ")
            contacto = buscar_contacto(agenda, nombre)
            
            if contacto:
                nuevo_telefono = input("Nuevo teléfono: ")
                if validar_telefono(nuevo_telefono):
                    contacto["telefono"] = nuevo_telefono
                    print("✅ Contacto actualizado correctamente.")
                else:
                    print("❌ Teléfono inválido. Debe ser numérico y tener máximo 11 dígitos.")
            else:
                print("❌ Contacto no encontrado.")
                
        elif opcion == "4":  # Eliminar contacto
            nombre = input("Nombre del contacto a eliminar: ")
            contacto = buscar_contacto(agenda, nombre)
            
            if contacto:
                agenda.remove(contacto)
                print("✅ Contacto eliminado correctamente.")
            else:
                print("❌ Contacto no encontrado.")
                
        elif opcion == "5":  # Mostrar todos los contactos
            if agenda:
                print("\n=== LISTA DE CONTACTOS ===")
                for contacto in agenda:
                    print(f"📞 {contacto['nombre']}: {contacto['telefono']}")
            else:
                print("📝 La agenda está vacía.")
                
        elif opcion == "6":  # Salir
            print("👋 ¡Hasta luego!")
            break
            
        else:
            print("❌ Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()