from ListaDoble import ListaDoble
listapedido = ListaDoble()

#METODOS PARA LA COLA

def menu():

    print("---------------------------------------")
    print("             MENU")
    print("1.Ingresar Orden")
    print("2.Entregar Orden")
    print("3.Mostar Ordenes")
    print("4.Datos Personales")
    print("5.Salir")
    print("---------------------------------------")



    
while True:
    menu()

    Eleccion= input("Ingrese la opcion que desea realizar: ")

    

    if Eleccion =="1":

        print("----------------------------------------------------------------")
        ingrediente = input("Ingrese el ingrediente a utilizar en la Pizza: ")
        listapedido.insertarIncio(ingrediente)
        print("pedido realizado")


    
    elif Eleccion == "2":
        print("Entregar ordenes...")
        
        listapedido.eliminarFinal()
      

        

    elif Eleccion == "3":
        print("Se muestra Los pedidos por orden de prioridad...")
        print("El primero en entrar es el primero en salir ")
        listapedido.recorrerCola()

    elif Eleccion == "4":
        print("---------------------------------------------------")
        print("Introduccion a la Programacion y Computacion 2...")
        print("Ingenieria en Ciencias y Sistemas")
        print("Cuarto Semestre")
        print("Daniel Alejandro Orozco Melgar")
        print("201513677")
        print("---------------------------------------------------")
        
      

    elif Eleccion == "5":
             
        print("Saliendo...")
        print("Saliendo..")
        print("Saliendo.")
        break
                           
    else:
        print("Opcion Incorrecta elige una entre el rango de 1-6")