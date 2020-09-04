%{
	/*Demo program for recognition of letters
%}

letter	[a-zA-z]

%%
{letter}	{ printf("letter: %s\n", yytext); }
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
