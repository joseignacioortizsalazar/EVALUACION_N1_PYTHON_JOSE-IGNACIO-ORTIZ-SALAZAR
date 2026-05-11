print("====Registro y clasificación de deportistas por disciplina====")
deportistas = {}

n = int(input("====Ingrese la cantidad de deportistas: "))

for i in range(n):
    print(f"\nDeportista {i+1}")
    
    nombre = input("Nombre: ")
    disciplina = input("Disciplina: ")
    tiempo = float(input("Tiempo en la prueba: "))

    """si la disiplna no esxiste se crea"""""
    if disciplina not in deportistas:
        deportistas[disciplina] = []

    
    deportistas[disciplina].append({
        "nombre": nombre,
        "tiempo": tiempo
    })

print("\n=== Deportistas por disciplina ===")

for disciplina, lista in deportistas.items():
    print(f"\n{disciplina}:")
    
    for deportista in lista:
        print(f" - {deportista['nombre']} | Tiempo: {deportista['tiempo']}")

  
"""Mostrar el mejor tiempo por disciplina"""
print("\n=== Mejor deportista por disciplina ===")

for disciplina, lista in deportistas.items():
    
    """ Buscar el mejor tiempo"""
    mejor = min(lista, key=lambda x: x["tiempo"])

    print(f"{disciplina}:")
    print(f" Mejor deportista: {mejor['nombre']}")
    print(f" Tiempo: {mejor['tiempo']}")