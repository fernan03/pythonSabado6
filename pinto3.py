print("***MENU***")
print("1. Agregar 1 producto")
print("2. Mostrar producto")
print("3. Buscar producto y editarlo")
print("4. Buscar producto y eliminarlo")
print("5. Salir")

opcion=100

productos=[]
while(opcion !=0):
    producto={}
    opcion=int(input("Digite una opcion: "))
    if(opcion==1):
        producto['codigo']=int(input("digite codigo del producto: "))
        producto['nombre']=input("Digite nombre del producto: ")
        producto['precio']=int(input("Digite precio del producto: "))
        productos.append(producto)
        print(f'Producto agregado...')

    elif(opcion==2): 
        print(productos)

    elif(opcion==3):
            print("hola")
    elif(opcion==4):
        print("hola")

    elif(opcion==5):
        print(f'FIN')
        break;
    else:
        print(f'Digite opcion valida')

    
