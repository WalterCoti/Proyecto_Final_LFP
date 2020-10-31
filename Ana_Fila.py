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
        carcActual = contenido[pos]
        if contenido[pos] =="\n":
            numFila += 1
            numCol = 0
        else:
            numCol +=1
            if estado == 0:
                if contenido[pos].isalpha() or contenido[pos]== "_":
                    texto = texto + contenido[pos]
                elif contenido[pos].isdigit():
                    texto = texto + contenido[pos]
                else:
                    if contenido[pos] in tokens.lstTokens:
                       # estado = 2   #----ir a estado en identificador entre parentesis
                        if texto:
                            if contenido[pos] == "(":
                                
                                if texto.lower() in tokens.lstTokens:
                                    addToken(numFila,numCol-len(texto), texto,texto)    
                                    texto=""
                                    estado = 3
                                else:
                                    addToken(numFila,numCol-len(texto),"identificador",texto)
                                    texto=""
                                    estado=3

                        if contenido[pos]=="=" and contenido[pos+1]==">":
                            addToken(numFila,numCol, "=>","=>")
                        else:
                            addToken(numFila,numCol, contenido[pos],contenido[pos])
                    elif contenido[pos]=="*" and contenido[pos-1]=="/":
                        addToken(numFila,numCol-1, "/*","/*")
                        estado = 6
                    elif contenido[pos] == ">" or contenido[pos] == "/":
                        continue
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
                        if contenido[pos].isspace():
                            continue
                        else:
                            addErrores(numFila,numCol,contenido[pos])
          
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
                elif contenido[pos] in tokens.lstTokens:
                    addToken(numFila,numCol,contenido[pos],contenido[pos]) 
                    estado = 2
                else:
                    if contenido[pos].isspace():
                        continue
                    else:
                        addErrores(numFila,numCol,contenido[pos])
          
            elif estado == 2:#----------------------------------------------------------------
                if contenido[pos].isdigit() or contenido[pos].isalpha():
                    texto = texto + contenido[pos] 
# 
                elif contenido[pos]== "_":
                    texto = texto + contenido[pos] 
                else:
                    if contenido[pos] in tokens.lstTokens:
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto)   
                            else:
                                addToken(numFila,numCol-len(texto), "identificador",texto)
                        else:
                            estado = 3
                        if contenido[pos] == ":" or contenido[pos] == ";":
                            estado = 0
                        if contenido[pos] == ")":
                            estado = 0          
                        if contenido[pos] == "(":
                            estado = 3 
                        if contenido[pos] == "\"":
                            estado = 4
                        addToken(numFila,numCol,contenido[pos],contenido[pos])
                        texto =""
                    else:
                        if contenido[pos].isspace():
                            continue
                        else:
                            addErrores(numFila,numCol,contenido[pos])


            elif estado == 3:#------------------------------------------------------------------------
                if contenido[pos] in tokens.lstTokens:
                    if contenido[pos] == "\"":
                        addToken(numFila,numCol,contenido[pos] ,contenido[pos])
                        estado = 4
                    elif contenido[pos] == ",":
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto)   
                            else:
                                addToken(numFila,numCol-len(texto), "texto",texto)      
                            texto =""
                        addToken(numFila,numCol,contenido[pos],contenido[pos])
                    elif contenido[pos] == "(":
                        addToken(numFila,numCol,contenido[pos],contenido[pos])
                        estado = 5
                    elif contenido[pos] == ")" or contenido[pos] =="}":
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto)   
                            else:
                                addToken(numFila,numCol-len(texto), "identificador",texto)      
                            texto =""
                        addToken(numFila,numCol,contenido[pos],contenido[pos])
                        estado = 0
                    elif contenido[pos] == ";" or contenido[pos] =="{" :
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto)   
                            else:
                                addToken(numFila,numCol-len(texto), "identificador",texto)      
                            texto =""
                        else:
                            addToken(numFila,numCol,contenido[pos],contenido[pos])
                        texto =""
                        estado=0
                elif contenido[pos].isalpha() or contenido[pos].isdigit():
                        texto = texto + contenido[pos]
                elif contenido[pos] == "_":
                    texto = texto + contenido[pos]
                else:
                    if contenido[pos].isspace():
                        continue
                    else:
                        addErrores(numFila,numCol,contenido[pos])
            elif estado == 4:#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
                if contenido[pos] == "\"":
                    if texto:
                        addToken(numFila,numCol-len(texto),"texto",texto)
                    addToken(numFila,numCol,"\"","\"")
                    texto = ""
                    estado = 5
                else:
                    texto = texto + contenido[pos]
            elif estado == 5: #_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
                if contenido[pos] in tokens.lstTokens:
                    if contenido[pos] == ",":
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                                texto =""
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto) 
                                texto =""
                            else:
                                addToken(numFila,numCol-len(texto), "identificador",texto) 
                                texto =""
                        addToken(numFila,numCol,",",",")
                        texto = ""
                        estado = 3
                    elif contenido[pos] == ")":
                        if texto:
                            if texto.lower() in tokens.lstTokens:
                                addToken(numFila,numCol-len(texto), texto,texto) 
                                texto =""
                            elif texto.isnumeric():
                                addToken(numFila,numCol-len(texto), "numero",texto) 
                                texto =""
                            else:
                                addToken(numFila,numCol-len(texto), "identificador",texto) 
                                texto =""

                        addToken(numFila,numCol,")",")")
                        texto = ""
                    elif contenido[pos] == ";":
                        addToken(numFila,numCol,";",";")
                        estado = 0
                    elif contenido[pos] == "\"":
                        addToken(numFila,numCol,contenido[pos],contenido[pos])
                        estado = 4
                else:
                    if contenido[pos].isspace():
                        continue
                    else:
                        addErrores(numFila,numCol,contenido[pos])
            elif estado == 6:
                if contenido[pos]=="*" and contenido[pos+1]=="/":
                    if texto:
                        addToken(numFila,numCol- len(texto),"texto",texto)
                    addToken(numFila,numCol, "*/","*/")
                    texto = ""
                    estado = 0
                else:
                    texto = texto + contenido[pos]
         



def addToken(fila, columna, preserv, valor):
    ntoken = obj_Token.obToken(tokens.lstTokens.get(preserv),valor)
    ntoken.setColum(columna)
    ntoken.setFila(fila)
    ntoken.setDescript(tokens.desc_Tokens.get(preserv))
    varGlobal.lst_Token_encontrados.append(ntoken)

def addErrores(fila, columna, texto):
    nError = obj_error.errorTo(fila,columna,texto)
    varGlobal.lst_Errores.append(nError)