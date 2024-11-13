%{
#include "y.tab.h"
%}

%%
for					return FOR;
[\(\)]					return PARANTHESIS;
[a-zA-Z0-9]*				return OPERAND;
"="|"<"|">"|">="|"<="|"=="|"++"|"--"	return OPERATOR;
\;					return SEMICOLON;
,					return COMMA;
\n					return NEWLINE;
.					;
%%


int yywrap()
{
	return 1;
}



--------------------------------------------------
//for.y

%{
	#include <stdio.h>
	int valid = 1;
%}

%token FOR PARANTHESIS OPERAND OPERATOR COMMA SEMICOLON NEWLINE

%%
start: FOR PARANTHESIS A A B PARANTHESIS NEWLINE;
A: OPERAND OPERATOR OPERAND SEMICOLON | OPERAND OPERATOR OPERAND COMMA A | SEMICOLON;
B: OPERAND OPERATOR | OPERAND OPERATOR COMMA B |;
%%

int yyerror()
{
	valid = 0;
	printf("Invalid.\n");
	return 1;
}

void main()
{
	printf("Enter string:\n");
	yyparse();

	if (valid)
		printf("Valid.\n");
}