import random

lista = []

def Generar_lista(lista):
    #Genero un diccionario con un "Id" del 1 al 10 con una "Edad" random del 1 al 100.
    for i in range(1, 11):
        dic = dict()
        dic = {"Id": i, "Edad": random.randint(1,100)}
        #Agrego al final de la lista el elemento del diccionario.
        lista.append(dic)
    return lista

print(Generar_lista(lista))
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")

def Ordenar_lista(lista):
    #Ordeno la lista de mayor a menor segun el valor "Edad" del diccionario.
    lista.sort(key=lambda p: p["Edad"], reverse=True)
    return lista

Ordenar_lista(lista)
print("La persona mas grande de edad esta en el Id:", lista[0]["Id"])
print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
print("La persona mas joven de edad esta en el Id:", lista[9]["Id"])
