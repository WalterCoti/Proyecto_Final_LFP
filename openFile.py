def getContenido(nameFile):
    try:
        with open (nameFile, 'r+') as data: 
            contenido = data.read();
            return contenido
    except:
        print("no se encontro el archivo ->  " + nameFile)

def createFile(nameFile):
    pass