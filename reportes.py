import varGlobal
import webbrowser
import os
import base_html


def reportTokens():
    lst_head = ['No.','Lexema','Token','Fila','Columna','Descripción']
    try: 
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "R_Token.html")
        with  open(path, 'w+') as file_reporte:
            file_reporte.write(base_html.html_head("Report Tokens","Lista de Tokens"))
            file_reporte.write("<thead class=\"thead-dark\">")
            file_reporte.write("<tr>")
            for columna in lst_head:
                file_reporte.write("<th>"+ columna+ "</th>")
            file_reporte.write("</tr>")
            file_reporte.write("</thead")
            file_reporte.write("<tbody>")
            for cont in range(len(varGlobal.lst_Token_encontrados)):
                elem_Token = varGlobal.lst_Token_encontrados[cont]
                file_reporte.write("<tr>")
                file_reporte.write("<th>"+ str(cont+1) + "</th>")
                file_reporte.write("<td>"+ elem_Token.getLexema() + "</td>")
                file_reporte.write("<td>"+ elem_Token.getToken() + "</td>")
                file_reporte.write("<td>"+ str(elem_Token.getFila())+ "</td>")
                file_reporte.write("<td>"+ str(elem_Token.getCol()) + "</td>")
                file_reporte.write("<td>"+ elem_Token.getDescript() + "</td>")
                file_reporte.write("</tr>")
            file_reporte.write("</tbody>")
            file_reporte.write(base_html.final_hmtl)
        webbrowser.open_new_tab(path)
        print("Reporte de Tokens creado con Exito")
    except:
        print("Error al buscar algun dato")


def ReportError():
    lst_head = ['No.','Error','Fila','Columna']
    try: 
        if len(varGlobal.lst_Errores) == 0:
            print("No se Encontraron Errores")
        else:
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "R_Errores.html")
            with  open(path, 'w+') as file_reporte:
                file_reporte.write(base_html.html_head("Report Errores","Lista de Errores"))
                file_reporte.write("<thead class=\"thead-dark\">")
                file_reporte.write("<tr>")
                for columna in lst_head:
                    file_reporte.write("<th>"+ columna+ "</th>")
                file_reporte.write("</tr>")
                file_reporte.write("</thead")
                file_reporte.write("<tbody>")
                aver = range(len(varGlobal.lst_Token_encontrados)-1)
                for cont in range(len(varGlobal.lst_Errores)):
                    error = varGlobal.lst_Errores[cont]
                    file_reporte.write("<tr>")
                    file_reporte.write("<th>"+ str(cont+1) + "</th>")
                    file_reporte.write("<td>"+ str(error.getTexto()) + "</td>")
                    file_reporte.write("<td>"+ str(error.getFila())+ "</td>")
                    file_reporte.write("<td>"+ str(error.getColumna()) + "</td>")
                    file_reporte.write("</tr>")
                file_reporte.write("</tbody>")
                file_reporte.write(base_html.final_hmtl)
            webbrowser.open_new_tab(path)
            print("Reporte de Errores creado con Exito")
    except:
        print("Error al buscar algun dato")