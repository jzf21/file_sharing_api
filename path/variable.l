% {
#include "y.tab.h" // Include Yacc-generated token definitions
      % }

    % %

    [a - zA -
        Z][a - zA - Z0 - 9] *
    return identifier; // Match an identifier: starting letter, followed by letters/digits

.return yytext[0]; // Match and return any other character
\n return 0;       // End of input

% %

    int yywrap()
{
    return 1;
}
------------
%{
    #include <stdio.h>

    // Declare yylex, which is provided by the Lex file
    int yylex();

    // Declare yyerror, which handles errors
    void yyerror(const char *s);

    int valid = 1;  // To check if the identifier is valid or not
%}

%token identifier  // Token for valid identifiers

%%

start : identifier    // The rule expects an identifier
      ;

%%

void yyerror(const char *s) {
    printf("\n%s\n", s);  // Print the error message passed from Yacc
    valid = 0;  // Mark as invalid if an error occurs
}

int main() {
    printf("\nEnter a name to be tested for identifier: ");
    yyparse();  // Start parsing the input
    if (valid) {
        printf("\nIt is a valid identifier!\n");
    }
    return 0;
}

