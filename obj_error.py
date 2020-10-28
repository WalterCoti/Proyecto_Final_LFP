class errorTo():
    def __init__(self,fila, col, texto):
        self.fila = fila
        self.columna = col
        self.text = texto

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTexto(self):
        return self.text