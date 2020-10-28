import tokens
import obj_Token
import varGlobal
import obj_error


def analisis_linea(contenido):
    estado = 0
    texto = ""
    numFila = 1
    numCol = 0
    lencontrr = len(contenido)

    for pos in range(len(contenido)):
        if contenido[pos] =="\n":
            numFila += 1
            numCol = 0
        else:
            carcActual = contenido[pos]
            numCol +=1
            if estado == 0:
                if contenido[pos].isalpha():
                    texto = texto + contenido[pos]
                else:
                    if contenido[pos] in tokens.lstTokens:
                       # estado = 2   #----ir a estado en identificador entre parentesis
                        if texto.lower() in tokens.lstTokens:
                            addToken(numFila,numCol-len(texto), texto,texto)    
                            texto=""
                            estado = 2
                        else:
                            addToken(numFila,numCol-len(texto),"identificador",texto)
                            texto=""
                            estado=1
                        addToken(numFila,numCol, contenido[pos],contenido[pos])

                    elif contenido[pos].isspace():
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto)    
                                texto=""
                                estado = 1
                            else:
                                addToken(numFila,numCol-len(texto),"identificador",texto)
                                texto=""
                                estado = 1
                        if contenido[pos+1].isalpha() or contenido[pos + 1] == "_":
                            estado=2
                    else:
                        addErrores(numFila,numCol,contenido[pos])
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto)    
                                texto=""
                                estado = 1
                            else:
                                addToken(numFila,numCol-len(texto),"identificador",texto)
                                texto=""
            
            elif estado == 1:#--------------------------------------IDENTIFICADOR---------------------------------------
                if contenido[pos].isdigit() :
                    prueba = contenido[pos + 1]
                    if contenido[pos + 1].isalpha() or contenido[pos + 1] == "_" :
                        estado = 2
                        texto = texto + contenido[pos]
                        addToken(numFila,(numCol - len(texto)),"numero",texto) 
                        texto=""
                    else:
                        texto = texto + contenido[pos]
                elif contenido[pos].isspace():
                    if texto:
                        addToken(numFila,(numCol - len(texto)),"identificador",texto) 
                        texto=""  
                    if contenido[pos+1].isalpha() or contenido[pos + 1] == "_":
                            estado=2
                else:
                    addErrores(numFila,numCol,contenido[pos])
                    if texto:
                        if texto.lower() in tokens.lstTokens:
                            addToken(numFila,numCol-len(texto), texto,texto)    
                            texto=""
                            estado = 1
                        else:
                            addToken(numFila,numCol-len(texto),"identificador",texto)
                            texto=""
          
            elif estado == 2:#----------------------------------------------------------------
                if contenido[pos].isdigit() or contenido[pos].isalpha():
                    texto = texto + contenido[pos] 
                elif contenido[pos]== "_":
                    texto = texto + contenido[pos] 
                elif contenido[pos].isspace():
                    addToken(numFila,numCol-len(texto),"identificador",texto)
                    texto=""
                else:
                    if contenido[pos] in tokens.lstTokens:
                        addToken(numFila,numCol-len(texto),"identificador",texto)
                        addToken(numFila,numCol-len(texto),contenido[pos],contenido[pos])
                        texto=""
                    else:
                        if texto:
                            addToken(numFila,numCol-len(texto),"identificador",texto)
                            texto=""
                            addErrores(numFila,numCol,contenido[pos])


            elif estado == 3:
                pass
            elif estado == 4:
                pass
            elif estado == 5:
                pass
            elif estado == 6:
                pass
            elif estado == 7:
                pass
            elif estado == 8:
                pass
            elif estado == 9:
                pass



def addToken(fila, columna, preserv, valor):
    ntoken = obj_Token.obToken(tokens.lstTokens.get(preserv),valor)
    ntoken.setColum(columna)
    ntoken.setFila(fila)
    ntoken.setDescript(tokens.desc_Tokens.get(preserv))
    varGlobal.lst_Token_encontrados.append(ntoken)

def addErrores(fila, columna, texto):
    nError = obj_error.errorTo(fila,columna,texto)
    varGlobal.lst_Errores.append(nError)