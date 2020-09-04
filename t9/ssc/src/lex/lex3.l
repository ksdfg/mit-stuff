letter	[a-zA-Z]
digit	[0-9]
id		{letter}({letter}|{digit})

%%
{id}	{ printf("ID: %s\n", yytext); }
%%

int yywrap() {
	return 0;
}

int main() {
	yylex();
	return 0;
}
