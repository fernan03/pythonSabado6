lista = []
contador = 0

while(contador<10):
    diccionario = {}
    diccionario["NOMBRE"] = input("Digite nombre: ")
    diccionario["COLOR"] = input("Digite color: ")
    diccionario["PRECIO"] = input("Digite precio: ")
    lista.append(diccionario)
    contador+=1
lista.reverse()
print(f'{lista}')