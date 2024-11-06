def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        print(f"\nIteración {i + 1}:")  

        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
            print(f"Comparando {lista[j]} con {lista[min_index]} (mínimo actual)")


        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
            print(f"Intercambiando {lista[i]} con {lista[min_index]}: {lista}")
        else:
            print(f"No se necesita intercambio, {lista[i]} ya está en la posición correcta.")

    return lista


tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = []

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    lista.append(numero)

print("\nLista desordenada:", lista)
lista_ordenada = seleccion(lista)
print("\nLista ordenada:", lista_ordenada)
