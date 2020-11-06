import tokens
import varGlobal
import transisiones
from colorama import Fore, Back, Style



def iniciarAP():
    Auto_Pila(dameTokens())


def dameTokens():
    listaTokens=[]
    for obj_token in varGlobal.lst_Token_encontrados:
        if obj_token.getToken()=="tk_iCom" :
            continue
        elif obj_token.getToken()=="tk_Com":
            continue
        elif  obj_token.getToken() =="tk_fCom" :
            continue
        else:
            listaTokens.append(obj_token.getToken())
    return listaTokens



#(estado, lo que leo, desapilar; estado, apilar)
def Auto_Pila(entrada):
    ent_ana = entrada
    salir = False
    estado = "i"
    pilaActual = []
    pila = []

    while not salir:
        pilaActual= pila.copy()
        try:
            if estado == "i":#---------------------------------estado i--------------
                print(Fore.RED, 'PILA'+ "  |  " +Fore.YELLOW,'CADENA ENTRADA' + "  |  " +Fore.GREEN,'TRANSISION')
                pila.append("#")
                printFormato(pilaActual,entrada,transisiones.tran[0])
                estado = "p"

            elif estado == "p":#---------------------------------estado p--------------
                
                pila.append("SENT")
                printFormato(pilaActual,entrada,transisiones.tran[1])
                estado = "q"

            elif estado == "q":#---------------------------------estado q--------------

                cimaPila = pila[-1]
                if len(entrada)==0:
                    if cimaPila == "#":
                        printFormato(pilaActual,["----"],transisiones.tran[-1])
                        pila.pop()
                        estado = "r"
                    else:
                        TuplaTR= tuplaconEpsilon(cimaPila,"E")
                        pila.pop()
                        printFormato(pilaActual,entrada,TuplaTR)
                else:
                    tokenAct = entrada[0]
                    if cimaPila in tokenAct:
                            tplaTerminal = tupla_Terminal(cimaPila)
                            printFormato(pilaActual,entrada,tplaTerminal)     
                            pila.pop()
                            entrada.pop(0)
                    
                    elif tokenAct=="tk_iden" and cimaPila=="SENT":
                        tran_Apilar=('q','E','SENT','q',['tk_iden','tk_(','tip_valor','tk_)','tk_;','SENT'])
                        printFormato(pilaActual,entrada,tran_Apilar)
                        pila.pop()
                        for tken in reversed(tran_Apilar[4]):
                            pila.append(tken)
                    else:
                        try:
                            TuplaTRansision = dameTuplaNoTerm(cimaPila,tokenAct)
                            if type(TuplaTRansision) == None:
                                pass
                            else:
                                pila.pop()
                                for tken in reversed(TuplaTRansision[4]):
                                    pila.append(tken)
                                printFormato(pilaActual,entrada,TuplaTRansision)
                            #print(pilaActual,entrada,TuplaTRansision)
                        except:
                            TuplaTRansisionconE = tuplaconEpsilon(cimaPila,"E")
                            if type(TuplaTRansisionconE)==None:
                                 print(Fore.RED, "Sintaxis Incorrecta de aqui")
                                 print(Fore.RESET)
                            else:
                                pila.pop()
                                printFormato(pilaActual,entrada,TuplaTRansisionconE)
                            

            elif estado == "r":
                print(Fore.BLUE,"Sintaxis Correcta")
                print(Fore.RESET)
                salir == True
                break
            
        except:
            print(Fore.RED,"Sintaxis Incorrecta")        
            print(Fore.RESET)
            break
        x=input()

def tuplaconEpsilon(cimaPila,val_buscar):
    for tpls in transisiones.tran:
        if tpls[2]==cimaPila:
            if tpls[4][0] == val_buscar:    
                return tpls

def tplaNoTerminal(No_terminal):
    for nterm in transisiones.tran:
        tmplist = nterm[4]
        if tmplist[0] == No_terminal:
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



