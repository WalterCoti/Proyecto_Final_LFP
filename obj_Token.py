class obToken():
    def __init__(self,token,txtValor):
        self.fila = ""
        self.columna = ""
        self.descript = ""
        self.ntoken = token
        self.valor = txtValor
    
    def setFila(self,fila):
        self.fila = fila
    
    def setColum(self, col):
        self.columna = col
    
    def setDescript(self, descripcion):
        self.descript = descripcion

    def getFila(self):
        return self.fila 
    
    def getCol(self):
        return self.columna

    def getDescript(self):
        return self.descript
        
    def getToken(self):
        return self.ntoken
    
    def getLexema(self):
        return self.valor
    
    