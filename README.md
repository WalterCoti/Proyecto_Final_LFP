# Proyecto_Final_LFP

Gramática:
SENT -> declar SENT

		| s_if SENT
		| s_while SENT
		| s_for SENT
		| s_switch SENT
		| call_func SENT
		| E
	

declar -> tipo_var tk_iden tk_= tipo_decla

s_if ->  tk_if tk_( tip_valor tk_) tk_{ SENT tk_}

s_while ->  tk_while tk_( tip_valor tk_) tk_{ SENT tk_} SENT

s_for ->  tk_for tk_( tk_iden tk_in tk_iden tk_) tk_{ SENT tk_}

s_switch ->  tk_switch tk_( tip_valor tk_) tk_{ tipo_case tk_}

tipo_decla -> tk_( tip_valor tk_) tk_=> tk_{ SENT tk_}

tipo_case ->  tk_caso VALOR tk_: SENT op_bre
		| tk_def tk_: SENT op_bre
		
op_bre -> tk_break tk_:
		|	E
	
call_func -> tk_iden tk_( tip_valor tk_) tk_;

tipo_var ->  tk_var

		| tk_let
		| tk_const
		| tip_valor
		
VALOR -> tk_" tk_txt tk_"

		| tk_true
		| tk_false
		| tk_num
		| tk_iden
		
tip_valor -> VALOR M_Valor

M_Valor ->  tk_, tip_valor

		| tk_;
		| E
