def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        print(f"\nIteración {i + 1}:")
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(f"Paso {j + 1}: {lista}")  
    return lista

tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = []

for i in range(tamaño):
    Palabra = input(f"Ingrese la palabra {i + 1}: ")
    lista.append(Palabra)

print("\nLista desordenada:", lista)
lista_ordenada = burbuja(lista)
print("\nLista ordenada:", lista_ordenada)
