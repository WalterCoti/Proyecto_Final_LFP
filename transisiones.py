tran = [
('i','E','E','p',['#']),
('p','E','E','q',['SENT']),
('q','E','SENT','q',['declar','SENT']),
('q','E','SENT','q',['s_if','SENT']),
('q','E','SENT','q',['s_while','SENT']),
('q','E','SENT','q',['s_for','SENT']),
('q','E','SENT','q',['s_switch','SENT']),
('q','E','SENT','q',['call_func','SENT']),
('q','E','SENT','q',['E']),
('q','E','declar','q',['tipo_var','tk_iden','tk_=','tipo_decla']),
('q','E','s_if','q',['tk_if','tk_(','tip_valor','tk_)','tk_{','SENT','tk_}']),
('q','E','s_while','q',['tk_while','tk_(','tip_valor','tk_)','tk_{','SENT','tk_}','SENT']),
('q','E','s_for','q',['tk_for','tk_(','tk_iden','tk_in','tk_iden','tk_)','tk_{','SENT','tk_}']),
('q','E','s_switch','q',['tk_switch','tk_(','tip_valor','tk_)','tk_{','tipo_case','tk_}']),
('q','E','tipo_decla','q',['tk_(','tip_valor','tk_)','tk_=>','tk_{','SENT','tk_}']),
('q','E','tipo_case','q',['tk_caso','VALOR','tk_:','SENT','op_bre']),
('q','E','tipo_case','q',['tk_def','tk_:','SENT','op_bre']),
('q','E','op_bre','q',['tk_break','tk_:']),
('q','E','op_bre','q',['E']),
('q','E','call_func','q',['tk_iden','tk_(','tip_valor','tk_)','tk_;']),
('q','E','tipo_var','q',['tk_var']),
('q','E','tipo_var','q',['tk_let']),
('q','E','tipo_var','q',['tk_const']),
('q','E','tipo_decla','q',['tip_valor']),
('q','E','VALOR','q',['tk_"','tk_txt','tk_"']),
('q','E','VALOR','q',['tk_true']),
('q','E','VALOR','q',['tk_false']),
('q','E','VALOR','q',['tk_num']),
('q','E','VALOR','q',['tk_iden']),
('q','E','tip_valor','q',['VALOR','M_Valor']),
('q','E','M_Valor','q',['tk_,','tip_valor']),
('q','E','M_Valor','q',['tk_;']),
('q','E','M_Valor','q',['E']),
('q','tk_iCom','E','q',['E']),
('q','tk_Com','E','q',['E']),
('q','tk_fCom','E','q',['E']),
('q','tk_let','tk_let','q',['E']),
('q','tk_igual','tk_igual','q',['E']),
('q','tk_true','tk_true','q',['E']),
('q','tk_false','tk_false','q',['E']),
('q','tk_var','tk_var','q',['E']),
('q','tk_const','tk_const','q',['E']),
('q','tk_;','tk_;','q',['E']),
('q','tk_"','tk_"','q',['E']),
('q','tk_txt','tk_txt','q',['E']),
('q','tk_iden','tk_iden','q',['E']),
('q','tk_=','tk_=','q',['E']),
('q','tk_if','tk_if','q',['E']),
('q','tk_(','tk_(','q',['E']),
('q','tk_)','tk_)','q',['E']),
('q','tk_{','tk_{','q',['E']),
('q','tk_}','tk_}','q',['E']),
('q','tk_while','tk_while','q',['E']),
('q','tk_for','tk_for','q',['E']),
('q','tk_switch','tk_switch','q',['E']),
('q','tk_caso','tk_caso','q',['E']),
('q','tk_num','tk_num','q',['E']),
('q','tk_break','tk_break','q',['E']),
('q','tk_def','tk_def','q',['E']),
('q','tk_:','tk_:','q',['E']),
('q','tk_,','tk_,','q',['E']),
('q','tk_=>','tk_=>','q',['E']),
('q','tk_in','tk_in','q',['E']),
('q','#','#','q',['E'])
]

def tplaNoTerminal(No_terminal):
    for nterm in tran:
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
    for nterm in tran:
        tmplist = nterm[1]
        if tmplist == tkDesapilar:
            return nterm
        


print(dameTuplaNoTerm("SENT","E"))