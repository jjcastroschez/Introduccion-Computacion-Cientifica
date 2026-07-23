"""
Ejercicio 6 — Agenda telefónica con diccionario.

Implementa las cuatro operaciones básicas sobre una agenda:
  - AÑADIR contacto (nombre → teléfono).
  - BUSCAR teléfono por nombre.
  - MODIFICAR teléfono de un contacto existente.
  - ELIMINAR contacto.

Todo con un DICCIONARIO como estructura de datos: la clave es el
nombre y el valor es el teléfono.

Tema 6 - Introducción a la Computación Científica (ICC).
"""


def anadir(agenda: dict, nombre: str, telefono: str) -> None:
    """Añade un contacto. Si ya existe, avisa pero no lo sobreescribe.
    :param agenda: diccionario de contactos
    :param nombre: nombre del contacto
    :param telefono: teléfono del contacto
    """ 
    if nombre in agenda:
        print(f"  ⚠️ '{nombre}' ya está en la agenda con el teléfono {agenda[nombre]}.")
        print(f"      Usa modificar() si quieres cambiarlo.")
    else:
        agenda[nombre] = telefono
        print(f"  ✅ Añadido '{nombre}' → {telefono}")


def buscar(agenda: dict, nombre: str) -> str:
    """Devuelve el teléfono, o None si no existe.
    :param agenda: diccionario de contactos
    :param nombre: nombre del contacto
    :return: teléfono del contacto o None si no existe
    """
    tel = agenda.get(nombre)
    if tel is None:
        print(f"  ❌ '{nombre}' no está en la agenda.")
    else:
        print(f"  📞 '{nombre}' → {tel}")
    return tel


def modificar(agenda: dict, nombre: str, nuevo_telefono: str) -> None:
    """Cambia el teléfono. Solo funciona si el contacto existe.
    :param agenda: diccionario de contactos
    :param nombre: nombre del contacto
    :param nuevo_telefono: nuevo teléfono del contacto"""
    if nombre not in agenda:
        print(f"  ❌ '{nombre}' no existe. Usa anadir() para crearlo.")
    else:
        antiguo = agenda[nombre]
        agenda[nombre] = nuevo_telefono
        print(f"  🔄 '{nombre}': {antiguo} → {nuevo_telefono}")


def eliminar(agenda: dict, nombre: str) -> None:
    """Elimina un contacto (con confirmación si no existe).
    :param agenda: diccionario de contactos
    :param nombre: nombre del contacto"""
    if nombre not in agenda:
        print(f"  ❌ '{nombre}' no está en la agenda.")
    else:
        tel = agenda.pop(nombre)   # pop devuelve el valor y elimina la clave
        print(f"  🗑️ Eliminado '{nombre}' (era {tel})")


def listar(agenda: dict) -> None:
    """Muestra todos los contactos en orden alfabético."""
    if len(agenda) == 0:
        print("  (agenda vacía)")
    else:
        print(f"  Agenda ({len(agenda)} contactos):")
        for nombre in sorted(agenda):
            print(f"    {nombre:15} → {agenda[nombre]}")


def main():
    agenda = {}

    print("=== Añadir contactos ===")
    anadir(agenda, "Ana",   "600111222")
    anadir(agenda, "Luis",  "600333444")
    anadir(agenda, "Marta", "600555666")
    anadir(agenda, "Ana",   "600999888")   # ya existe → aviso

    print("\n=== Listar ===")
    listar(agenda)

    print("\n=== Buscar ===")
    buscar(agenda, "Luis")
    buscar(agenda, "Fulano")

    print("\n=== Modificar ===")
    modificar(agenda, "Luis", "600777000")
    modificar(agenda, "Fulano", "111")

    print("\n=== Eliminar ===")
    eliminar(agenda, "Marta")
    eliminar(agenda, "Marta")   # ya no está

    print("\n=== Estado final ===")
    listar(agenda)


if __name__ == "__main__":
    main()
