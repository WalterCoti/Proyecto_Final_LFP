lstTokens = {'/*':'tk_iCom',
            'texto':'tk_txt',
            'comentario':'tk_Com',
            '*/':'tk_fCom',
            'identificador':'tk_iden',
            'let':'tk_let',
            '=':'tk_=',
            'true':'tk_true',
            'false':'tk_false',
            'var':'tk_var',
            'const':'tk_const',
            ';':'tk_;',
            '"':'tk_"',
            'if':'tk_if',
            '(':'tk_(',
            ')':'tk_)',
            '{':'tk_{',
            '}':'tk_}',
            'while':'tk_while',
            'foreach':'tk_for',
            'switch':'tk_switch',
            'case':'tk_caso',
            'numero':'tk_num',
            'break':'tk_break',
            'default':'tk_def',
            ':':'tk_:',
            ',':'tk_,',
            '=>':'tk_=>',
            'in':'tk_in'
}

desc_Tokens = {'/*':'apertura de comentario en bloque',
            'texto':'texto plano',
            'comentario':'es una cadena de texto de tipo comentario',
            '*/':'cierre de comentario',
            'identificador':'texto que representa un identificador',
            'let':'declara el tipo de variable',
            '=':'signo igual, describe que el valor es igual a',
            'true':'Booleano Verdadero',
            'false':'Booleano Falso',
            'var':'Define un tipo de variable no especifico',
            'const':'Define una variable constante',
            ';':'Determina el final de una linea o funcion',
            '"':'Se utiliza para delimitar texto',
            'if':'operador if, valua un booleano para seguir con la ejecucion',
            '(':'inicia un conjunto de valores',
            ')':'finaliza el conjunto de volores',
            '{':'inicia la agrupacion de codigo a ejecutarse',
            '}':'finaliza la agrupacion de codigo a ejecutarse',
            'while':'ciclo que necesita de una validacion',
            'foreach':'ciclo que itera sobre una agrupacion de elementos',
            'switch':'operador en caso de, hace a referencia a un segmento en especifico',
            'case':'se refiere a una condicion en especifico',
            'numero':'es un numero',
            'break':'finaliza la ejecucion de una bucle.',
            'default':'por defecto, usado para referirse a la opcion inicial',
            ':':'inicio de un caso',
            ',':'separacion de valores',
            '=>':'utilizado para asignar ',
            'in':'utilizado en el ciclo foreach, esta contenido en'
}
Terminales = ['tk_iCom',
            'tk_txt',
            'tk_Com',
            'tk_fCom', 
            'tk_iden',
            'tk_let',
            'tk_=',
            'tk_true',
            'tk_false',
            'tk_var',
            'tk_const',
            'tk_;',
            'tk_"',
            'tk_if',
            'tk_(',
            'tk_)',
            'tk_{',
            'tk_}',
            'tk_while',
            'tk_for',
            'tk_switch',
            'tk_caso',
            'tk_num',
            'tk_break',
            'tk_def',
            'tk_:',
            'tk_,',
            'tk_=>',
            'tk_in']


#print(listaoficial)