def insercion(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        print(f"\nIteración {i}: numero = {clave}")  
        
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            print(f"Desplazando {lista[j]} a la posición {j + 1}: {lista}")  
            j -= 1
            
        
        lista[j + 1] = clave
        print(f"Insertado {clave} en la posición {j + 1}: {lista}")  
    return lista


tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = []

for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    lista.append(numero)


print("\nLista desordenada:", lista)
lista_ordenada = insercion(lista)
print("\nLista ordenada:", lista_ordenada)
