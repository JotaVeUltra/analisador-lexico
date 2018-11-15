from collections import namedtuple
from typing import Callable

from constantes import PALAVRAS_RESERVADAS

Token = namedtuple("Token", ["codigo", "caracteres", "tipo"])
Token.__repr__ = (
    lambda self: f"< {str(self.codigo).rjust(2)} {str(self.tipo).rjust(19)}: {self.caracteres} >"
)


def analisar(texto: str) -> list:
    tokens = []
    linha = 0
    estado = 0
    sequencia = ""
    for caractere in texto:
        if caractere == "\n":
            linha += 1
        estado, sequencia, token = processa_estado(estado)(sequencia, caractere, linha)
        if token:
            tokens.append(token)
        if estado >= 0:
            sequencia += caractere
        else:
            tokens.append(
                Token(0, caractere, f"[WARNING] Ignorou Token Invalido! Linha: {linha}")
            )
            estado = 0

    return tokens


def processa_estado(estado: int) -> Callable:
    return {
        0: processa_estado_0,
        1: processa_estado_1,
        2: processa_estado_2,
        3: processa_estado_3,
        4: processa_estado_4,
        5: processa_estado_5,
        6: processa_estado_6,
        7: processa_estado_7,
        8: processa_estado_8,
        9: processa_estado_9,
        10: processa_estado_10,
        11: processa_estado_11,
        12: processa_estado_12,
        13: processa_estado_13,
        14: processa_estado_14,
        15: processa_estado_15,
    }[estado]


def processa_estado_0(sequencia: str, caractere: str, linha: int) -> tuple:
    sequencia = ""
    token = None
    if caractere.isalpha():
        return 1, sequencia, token
    if caractere.isdigit():
        return 14, sequencia, token
    if caractere in "-=+*)[],;$":
        return 7, sequencia, token
    return (
        {
            " ": 0,
            "\n": 0,
            "_": 2,
            '"': 3,
            "<": 5,
            ">": 6,
            ".": 8,
            ":": 9,
            "/": 10,
            "(": 15,
        }.get(caractere, -1),
        sequencia,
        token,
    )


def processa_estado_1(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere.isalpha() or caractere.isdigit():
        estado = 1
        token = None
    else:
        estado = 0
        if sequencia.upper() in PALAVRAS_RESERVADAS.keys():
            token = Token(
                PALAVRAS_RESERVADAS[sequencia.upper()],
                sequencia,
                "Palavra-reservada",
            )
        else:
            if len(sequencia) <= 30:
                token = Token(25, sequencia, "IDENT")
            else:
                token = Token(
                    0,
                    sequencia,
                    f"Um Identificador não pode conter mais de 30 caracteres! Linha: {linha}",
                )

    return estado, sequencia, token


def processa_estado_2(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere.isalpha() or caractere.isdigit():
        return 1, sequencia, None
    token = Token(
        0,
        sequencia,
        f"Um identificador deve terminar com letra ou numero! Linha: {linha}",
    )

    return -1, sequencia, token


def processa_estado_3(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == '"':
        return 4, sequencia, None
    return 3, sequencia, None


def processa_estado_4(sequencia: str, caractere: str, linha: int) -> tuple:
    if len(sequencia) < 257:
        token = Token(48, sequencia, "LITERAL")
    else:
        token = Token(
            0,
            sequencia,
            f"ILEGAL, valor fora da escala! Linha: {linha}",
        )

    return 0, sequencia, token


def processa_estado_5(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "=" or caractere == ">":
        return 7, sequencia, None
    token = Token(43, sequencia, "Sinal-de-Menor")
    return 0, sequencia, token


def processa_estado_6(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "=":
        return 7, sequencia, None
    token = Token(41, sequencia, "Sinal-de-Maior")
    return 0, sequencia, token


def processa_estado_7(sequencia: str, caractere: str, linha: int) -> tuple:
    if sequencia == "-":
        token = Token(31, sequencia, "Sinal-de-Subtracao")
    elif sequencia == "=":
        token = Token(40, sequencia, "Sinal-de-Igualdade")
    elif sequencia == "<>":
        token = Token(45, sequencia, "Sinal-de-Diferente")
    elif sequencia == ">=":
        token = Token(42, sequencia, "Sinal-de-Maior-igual")
    elif sequencia == "<=":
        token = Token(44, sequencia, "Sinal-de-Menor-igual")
    elif sequencia == "+":
        token = Token(30, sequencia, "Sinal-de-Adicao")
    elif sequencia == "*":
        token = Token(32, sequencia, "Sinal-de-Multiplicacao")
    elif sequencia == ")":
        token = Token(37, sequencia, "Fechamento-de-parenteses")
    elif sequencia == "[":
        token = Token(34, sequencia, "Abertura-de-colchetes")
    elif sequencia == "]":
        token = Token(35, sequencia, "Fechamento-de-colchetes")
    elif sequencia == ",":
        token = Token(46, sequencia, "Virgula")
    elif sequencia == ";":
        token = Token(47, sequencia, "Ponto-e-virgula")
    elif sequencia == "..":
        token = Token(50, sequencia, "Ponto-ponto")
    elif sequencia == ":=":
        token = Token(38, sequencia, "Sinal-de-atribuicao")
    elif sequencia == "$":
        token = Token(51, sequencia, "Fim-de-Arquivo")
    return 0, sequencia, token


def processa_estado_8(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == ".":
        return 7, sequencia, None
    token = Token(49, sequencia, "Ponto-final")
    return 0, sequencia, token


def processa_estado_9(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "=":
        return 7, sequencia, None
    token = Token(39, sequencia, "Dois-pontos")
    return 0, sequencia, token


def processa_estado_10(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "*":
        return 11, sequencia, None
    token = Token(33, sequencia, "Sinal-de-divisao")
    return 0, sequencia, token


def processa_estado_11(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "*":
        return 12, sequencia, None
    return 11, sequencia, None


def processa_estado_12(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere == "*":
        return 12, sequencia, None
    if caractere == ")":
        return 13, sequencia, None
    if caractere == "$":
        return -1, sequencia, None
    return 11, sequencia, None


def processa_estado_13(sequencia: str, caractere: str, linha: int) -> tuple:
    return 0, sequencia, None


def processa_estado_14(sequencia: str, caractere: str, linha: int) -> tuple:
    if caractere.isdigit():
        return 14, sequencia, None
    elif processa_estado_0(sequencia, caractere, linha)[0] < 0:
        estado = -1
    else:
        estado = 0
    num_inteiro = int(sequencia)
    if abs(num_inteiro) > 32767:
        token = Token(
            0,
            sequencia,
            f"ILEGAL, valor fora da escala! Linha: {linha}",
        )
    else:
        token = Token(26, str(num_inteiro), "INTEIRO")

    return estado, sequencia, token


def processa_estado_15(sequencia: str, caractere: str, linha: int) -> tuple:
    estado = processa_estado_10(sequencia, caractere, linha)[0]
    token = None
    if estado == 0:
        token = Token(36, sequencia, "Abertura-de-Parenteses")
    return estado, sequencia, token


def main(args: list = None) -> None:
    from pprint import pprint

    with open("teste.txt", "r") as file:
        text = file.read()

    tokens = analisar(text)
    pprint(tokens)


if __name__ == "__main__":
    main()
