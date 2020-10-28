import openFile
import Ana_Fila

contenido = ""

def menuBasilink():
    salir = False    
    while salir == False:
        print("**************************************")
        print("*              Bienvenido            *")
        print("**************************************")
        print("1. Cargar Script")
        print("2. Manejo AFD")
        print("3. Pila Interactiva")
        print("4. Diagrama de Bloques de Codigo")
        print("5. Salir \n")
        try:
            opcMenu = int(input("---Seleccionar Una opcion---\n"))
        except:
            print("Solamente se permiten numeros")
            
        try:
            if opcMenu == 1:
                archivo = input('Nombre/direccion del archivo: ')
                contenido = openFile.getContenido(archivo)
                
            elif opcMenu == 2:
                #for cont_linea in range(len(contenido)):
                    #Ana_Fila.analisis_linea(contenido[cont_linea],cont_linea+1)
                Ana_Fila.analisis_linea(contenido)

            elif opcMenu == 3:
                print('opcion 3 man')
                
            elif opcMenu == 4:
                print('opcion 4 man')
                
            elif opcMenu == 5:
                salir = True
            else:
                print("Las opciones unicamente son de 1 a 5")
        except:
            print("Entrada invalida")


menuBasilink()
