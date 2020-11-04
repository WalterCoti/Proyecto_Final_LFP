import tokens
import varGlobal
import transisiones
from colorama import Fore, Back, Style
#prueba=[]

#prueba = ['tk_let', 'tk_iden', 'tk_=', 'tk_"', 'tk_txt', 'tk_"', 'tk_;']
prueba=['tk_if','tk_(','tk_iden','tk_)','tk_{','tk_}']

def iniciarAP():
    Auto_Pila(dameTokens())
   # Auto_Pila(prueba)

def dameTokens():
    listaTokens=[]
    for obj_token in varGlobal.lst_Token_encontrados:
        listaTokens.append(obj_token.getToken())
    return listaTokens



#(estado, lo que leo, desapilar, estado, apilar)
def Auto_Pila(entrada):
    ent_ana = entrada
    salir = True
    estado = "i"
    pilaActual = []
    pila = []

    while salir== True:
        pilaActual= pila.copy()
        try:
            if estado == "i":#---------------------------------estado i--------------
                print(Fore.RED, 'PILA'+ "  |  " +Fore.YELLOW,'CADENA ENTRADA' + "  |  " +Fore.GREEN,'TRANSISION')
                #print('PILA' + "  |  " +'CADENA ENTRADA'+ "  |  " + 'TRANSISION')
                pila.append("#")
                printFormato(pilaActual,entrada,transisiones.tran[0])
               # print("|"+ pila + "  |  " + entrada[0] + "  |  " + transisiones.tran[0])
                estado = "p"

            elif estado == "p":#---------------------------------estado p--------------
                
                pila.append("SENT")
                printFormato(pilaActual,entrada,transisiones.tran[1])
                estado = "q"

            elif estado == "q":#---------------------------------estado q--------------

                cimaPila = pila[-1]
                if len(ent_ana)==0:
                    TuplaTR= dameTuplaNoTerm(cimaPila,"E")
                    printFormato(pilaActual,entrada,TuplaTR)
                    
                    if cimaPila == "#":
                        printFormato(pilaActual,["----"],transisiones.tran[-1])
                        pila.pop()
                        estado = "r"

                else:
                    tokenAct = entrada[0]
                    if cimaPila in tokenAct:
                        tplaTerminal = tupla_Terminal(cimaPila)
                        printFormato(pilaActual,entrada,tplaTerminal)     
                        pila.pop()
                        entrada.pop(0)
                    else:
                        try:
                            TuplaTRansision = dameTuplaNoTerm(cimaPila,tokenAct)
                            if type(TuplaTRansision) == None:
                                TuplaTRansisionconE = dameTuplaNoTerm(cimaPila,"E")
                                pila.pop()
                                printFormato(pilaActual,entrada,TuplaTRansisionconE)
                            else:
                                pila.pop()
                                for tken in reversed(TuplaTRansision[4]):
                                    pila.append(tken)
                                printFormato(pilaActual,entrada,TuplaTRansision)
                            #print(pilaActual,entrada,TuplaTRansision)
                        except:
                            print("transicion con Epsilon prro")

            elif estado == "r":
                print(Fore.BLUE,"Sintaxis Correcta")
                print(Fore.RESET)
                pass# estado de aceptacion
            
        except:
            print(Fore.RED,"Sintaxis Incorrecta")        
            print(Fore.RESET)
            break
        #x=input()



def tplaNoTerminal(No_terminal):
    for nterm in transisiones.tran:
        tmplist = nterm[4]
        if tmplist.__class__== list:
            if tmplist[0] == No_terminal:
                return nterm
        else:
            if tmplist == No_terminal:
                return nterm

def dameTuplaNoTerm(cimaPila, NTBuscar):
    bucle = True
    NTerm= tplaNoTerminal(NTBuscar)
    while bucle == True:                
        if NTerm[2] == cimaPila:
            return NTerm
        else:
            NTerm = tplaNoTerminal(NTerm[2])

def tupla_Terminal(tkDesapilar):
    for nterm in transisiones.tran:
        tmplist = nterm[1]
        if tmplist == tkDesapilar:
            return nterm
        
def printFormato(Pilaentrada, cadenaentrada, tran_entrada):
    txtPila =""
    txt_ent = ""
    txt_tran = ""
    produc = ""
    for itm in Pilaentrada:
        txtPila += itm+" "
    for tkns in cadenaentrada:
        txt_ent += tkns + " "
    for prod in tran_entrada[4]:
        produc += prod +" "
    txt_tran =  "(" + tran_entrada[0] + ", "+tran_entrada[1] + ", "+tran_entrada[2] + "; "+ tran_entrada[3] + ", "+ produc + ")"
    print(Fore.RED, txtPila + Fore.YELLOW,txt_ent + Fore.GREEN,txt_tran)

#print(dameTupla("SENT","tk_let"))
iniciarAP()


