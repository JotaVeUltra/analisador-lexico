from collections import namedtuple

Simbolo = namedtuple('Simbolo', ['label', 'descricao', 'codigo'])

VAZIO = Simbolo('', 'Cadeia vazia', '0')
EOF = Simbolo('$', 'Fim do arquivo', '1')
OPERADOR_SOMA = Simbolo('+', 'Soma', '2')
OPERADOR_SUBTRACAO = Simbolo('-', 'Subtração', '3')
OPERADOR_MULTIPLICACAO = Simbolo('*', 'Multiplicação', '4')
OPERADOR_DIVISAO = Simbolo('/', 'Divisão', '5')
OPERADOR_IGUALDADE = Simbolo('=', 'Igualdade', '6')
MAIOR_QUE = Simbolo('>', 'Maior que', '7')
MAIOR_IGUAL = Simbolo('>=', 'Maior igual que', '8')
MENOR_QUE = Simbolo('<', 'Menor que', '9')
MENOR_IGUAL = Simbolo('<=', 'Menor igual que', '10')
DIFERENTE = Simbolo('<>', 'Diferente', '11')
ATRIBUICAO = Simbolo(':=', 'Atribuição', '12')
DOIS_PONTOS = Simbolo(':', 'Dois pontos', '13')
PONTO_VIRGULA = Simbolo(';', 'Ponto e vírgula', '14')
VIRGULA = Simbolo(',', 'Vírgula', '15')
PONTO = Simbolo('.', 'Ponto', '16')
ABRE_PARENTESE = Simbolo('(', 'Abre parentese', '17')
FECHA_PARENTESE = Simbolo(')', 'Fecha parentese', '18')
IDENTIFICADOR = Simbolo('', 'Identificador', '19')
INTEIRO = Simbolo('[0-9]', 'Inteiro', '20')
LITERAL = Simbolo('[a-zA-Z]', 'Literal', '21')
PROGRAM = Simbolo('PROGRAM', 'Program', '22')
CONST = Simbolo('CONST', 'Const', '23')
VAR = Simbolo('VAR', 'Var', '24')
PROCEDURE = Simbolo('PROCEDURE', 'Procedure', '25')
BEGIN = Simbolo('BEGIN', 'Begin', '26')
END = Simbolo('END', 'End', '27')
INTEGER = Simbolo('INTEGER', 'Integer', '28')
OF = Simbolo('OF', 'Of', '29')
CALL = Simbolo('CALL', 'Call', '30')
IF = Simbolo('IF', 'If', '31')
THEN = Simbolo('THEN', 'Then', '32')
ELSE = Simbolo('ELSE', 'Else', '33')
WHILE = Simbolo('WHILE', 'While', '34')
DO = Simbolo('DO', 'Do', '35')
REPEAT = Simbolo('REPEAT', 'Repeat', '36')
UNTIL = Simbolo('UNTIL', 'Until', '37')
READLN = Simbolo('READLN', 'Readln', '38')
WRITELN = Simbolo('WRITELN', 'Writeln', '39')
OR = Simbolo('OR', 'Or', '40')
AND = Simbolo('AND', 'And', '41')
NOT = Simbolo('NOT', 'Not', '42')
FOR = Simbolo('FOR', 'For', '43')
TO = Simbolo('TO', 'To', '44')
CASE = Simbolo('CASE', 'Case', '45')
COMENTARIO = Simbolo('Comentario', 'Comentario', '-1')
ERROR = Simbolo('Caracter não identificado', 'Erro', '-2')

simbolos = [
    VAZIO,
    EOF,
    OPERADOR_SOMA,
    OPERADOR_SUBTRACAO,
    OPERADOR_MULTIPLICACAO,
    OPERADOR_DIVISAO,
    OPERADOR_IGUALDADE,
    MAIOR_QUE,
    MAIOR_IGUAL,
    MENOR_QUE,
    MENOR_IGUAL,
    DIFERENTE,
    ATRIBUICAO,
    DOIS_PONTOS,
    PONTO_VIRGULA,
    VIRGULA,
    PONTO,
    ABRE_PARENTESE,
    FECHA_PARENTESE,
    PROGRAM,
    CONST,
    VAR,
    PROCEDURE,
    BEGIN,
    END,
    INTEGER,
    OF,
    CALL,
    IF,
    THEN,
    ELSE,
    WHILE,
    DO,
    REPEAT,
    UNTIL,
    READLN,
    WRITELN,
    OR,
    AND,
    NOT,
    FOR,
    TO,
    CASE,
]
