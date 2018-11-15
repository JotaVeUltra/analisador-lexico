from collections import namedtuple

from simbolos import simbolos, ERROR, IDENTIFICADOR, INTEIRO, COMENTARIO, LITERAL


Token = namedtuple('Token', ['string', 'identificacao', 'ordem', 'codigo'])

def analisar(texto_input):
    condicao = texto_input

    comentarios = []
    literais = []
    tokens = []

    while '(*' in condicao and '*)' in condicao:
        inicio_comentario = condicao.find('(*')
        fim_comentario = condicao.find('*)') + 2
        comentario = condicao[inicio_comentario:fim_comentario]

        comentarios.append(comentario)
        condicao = condicao.replace(comentario, ' # ')

    while '"' in condicao:
        inicio_literal = condicao.find('"')
        fim_literal = find_nth(condicao, '"', 2) + 1
        literal = condicao[inicio_literal: fim_literal]

        literais.append(literal)
        condicao = condicao.replace(literal, ' @ ')

    texto = condicao.replace('\n', ' ')
    texto = texto.replace('\t', ' ')
    while '  ' in texto:
        texto = texto.replace('  ', ' ')

    texto_quebrado = texto.split(' ')

    for ordem, txt in enumerate(texto_quebrado):
        if txt == '#':
            try:
                token = Token(comentarios.pop(0), COMENTARIO.descricao, ordem, COMENTARIO.codigo)
            except:
                token = identificar_token(ordem, txt)
        elif txt == '@':
            try:
                token = Token(literais.pop(0), LITERAL.descricao, ordem, LITERAL.codigo)
            except:
                token = identificar_token(ordem, txt)

        else:
            token = identificar_token(ordem, txt)

        tokens.append(token)

    msg = ''
    for token in tokens:
        if token.codigo == '-1':
            continue
        elif token.codigo == '-2':
            msg = str(token.codigo).ljust(5) +  token.identificacao.ljust(20) +  ' - ' + token.string.ljust(20)
            print(msg)
            return
        else:
            msg += str(token.codigo).ljust(5) +  token.identificacao.ljust(20) +  ' - ' + token.string.ljust(20) + '\n'
    print(msg)

def identificar_token(ordem, string):
    for simbolo in simbolos:
        if string.upper() == simbolo.label:
            return Token(string, simbolo.descricao, ordem, simbolo.codigo)
    if string.isalpha():
        return Token(string, IDENTIFICADOR.descricao, ordem, IDENTIFICADOR.codigo)
    if string.isdigit():
        if abs(int(string) <= 32767):
            return Token(string, INTEIRO.descricao, ordem, INTEIRO.codigo)

    return Token(string, ERROR.descricao, ordem, ERROR.codigo)


def find_nth(string, substring, n):
    if n == 1:
        return string.find(substring)
    return string.find(substring, find_nth(string, substring, n - 1) + 1)


if __name__ == '__main__':
    with open('teste', 'r') as file:
        text = file.read()

    analisar(text)
