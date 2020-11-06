# Proyecto_Final_LFP

Gramática:


```
SENT -> tk_var  tk_iden  tk_=  tip_valor  
		|tk_let  tk_iden  tk_=  tip_valor  
		|tk_const  tk_iden  tk_=  tip_valor  
		|tk_if  tk_(  tip_valor  tk_)  tk_{  SENT  tk_}  SENT  
		|tk_whilE, tk_(  tip_valor  tk_)  tk_{  SENT  tk_}  SENT  
		|tk_for  tk_(  tk_iden  tk_in  tk_iden  tk_)  tk_{  SENT  tk_}  SENT  
		|tk_switch  tk_(  tip_valor  tk_)  tk_{  tipo_casE, tk_}  SENT  
		|tk_iden  tk_(  tip_valor  tk_)  tk_;  SENT  
		|E  
```
```
tipo_case -> tk_caso  VALOR  tk_:  SENT  op_brE, tipo_case  
			| tk_def  tk_:  SENT  op_brE, tipo_case  
			| E  
```
```
op_brE -> tk_break  tk_;  
		 |E  
```
```
VALOR -> tk_"  tk_txt  tk_"  
		|tk_true  
		|tk_false  
		|tk_num  
		|tk_iden  
		|tk_(  tip_valor  tk_)  tk_=>  tk_{  SENT  tk_}  SENT  
```
```
tip_valor -> VALOR  M_Valor  
			|E  
```
```
M_Valor -> tk_,  tip_valor  
		| tk_; SENT  
		| E 
```
