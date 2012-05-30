#!usr/bin/python
# -*- coding: utf-8 -*-
import math
#import pdb

# EstruturaDeDecisao

# exercicio numero 1
def numeroMaior(x, y):
    math.isnan(x)
    math.isnan(y)

    if x > y:
        z = x
    elif y >= x:
        z = y
    return z

# exercicio numero 2
def valorSinal(num):
    math.isnan(num)

    if num < 0:
        result = "negativo"
    elif num >= 0:
        result = "positivo"
    return result

# exercicio numero 3
def qualSexo(op):
    dic = {'F': "Feminino", 'M': "Masculino"}
    if dic.get(op) != None:
        return dic.get(op)
    return "Sexo Inválido!"

# exercicio numero 4
def tipoLetra(letra):
    if type(letra) is not str:
        raise TypeError('O parametro deve ser um letra.')
    vogais =['a','e','i','o','u']
    if vogais.__contains__(letra):
        result = 'vogal'
    else:
        result = 'consoante'
    return result

# exercicio numero 5
def situacao_aluno(nota1, nota2):
    math.isnan(nota1)
    math.isnan(nota2)

    media = (nota1+nota2) / 2
    if media >=7 and media < 10:
        result = 'Aprovado'
    elif media < 7:
        result = 'Reprovado'
    else:
        result = 'Aprovado com Distinção'
    return result

# exercicio numero 6
def maiorEntre3(a,b,c):
    math.isnan(a)
    math.isnan(b)
    math.isnan(c)

    return max(a,b,c)

# exercicio numero 7 
def maiorMenorEntre3(a,b,c):
    math.isnan(a)
    math.isnan(b)
    math.isnan(c)

    return max(a,b,c) , min(a,b,c)

# exercicio numero 8
def qualProdutoCamprar(produtos):
    if len( filter(lambda x: x.__class__ is not Produto, produtos) ) > 0:
        raise TypeError('Error, lista de Produtos possui algum item diferente de Produto')

    menor_prod = reduce(lambda x, y: x.valor < y.valor and x or y, produtos)
    return menor_prod.nome

class Produto:
    def __init__(self, nome, valor):
        math.isnan(valor)
        self.nome = nome
        self.valor = valor

# exercicio numero 9
def ordenarListaNumeroDecrescente(lista):
    if type(lista) is not list:
        raise TypeError('Error, parametro nao e uma lista')

    if len( filter(lambda x: type(x) is not int, lista) ) > 0:
        raise AttributeError('A lista possui valor nan')

    lista.sort(reverse=True)
    return lista

# exercicio numero 10
def qualTurno(turno):
    if type(turno) == str:
        dic = {'M': 'Bom Dia!', 'N': 'Boa Noite!', 'V': 'Boa Tarde!'}
        if dic.get(turno.upper()) != None:
            return dic.get(turno.upper())
    return "Valor Inválido!"

# exercicio numero 11
def reajuste_salario(salario):
    math.isnan(salario)

    if salario <= 280.0:
        result = (salario, '20%', salario * 0.2, round(salario * 1.2, 2))
    elif salario > 280 and salario <= 700:
        result = (salario, '15%', salario * 0.15, round(salario * 1.15, 2))
    elif salario > 700 and salario <= 1500:
        result = (salario, '10%', salario * 0.1, round(salario * 1.1, 2))
    else:
        result = (salario, '5%', salario * 0.05, round(salario * 1.05, 2))

    return result


# exercicio numero 12
def folha_pagamento(hh, total_h):
    math.isnan(hh)
    math.isnan(total_h)
    bruto = hh * total_h
    if bruto <= 900:
        ir = 0.000000001
    elif bruto > 900 and bruto <= 1500:
        ir = 0.05
    elif bruto > 1500 and salario <= 2500:
        ir = 0.1
    elif bruto > 2500:
        ir = 0.2
    valorIR = round(ir * bruto, 2)
    inss = round(bruto * 0.1, 2)
    fgts = round(bruto * 0.11, 2)
    total_descontado = round(valorIR+inss, 2)
    liquido = round(bruto - (valorIR+inss), 2)
    porc = round(ir*100, 2)
    result = (bruto, valorIR, inss, fgts, total_descontado, liquido)
    return result

# exercicio numero 13
def dia_semana(num):
    try:
        math.isnan(num)
        dic = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sabado'}
        if dic.get(num):
            return dic.get(num)
        return 'Valor Inválido!'
    except TypeError:
        return 'Valor Inválido!'

# exercicio numero 14
def valor_conceito(nota1, nota2):
    math.isnan(nota1)
    math.isnan(nota2)
    if (0 <= nota1 <= 10) and ( 0 <= nota2 <= 10):
        media = (nota1+nota2)/2
        if media <= 4:
            conceito = 'E'
        elif media > 4 and media <= 6:
            conceito = 'D'
        elif media > 6 and media <= 7.5:
            conceito = 'C'
        elif media > 7.5 and media <= 9:
            conceito = 'B'
        elif media > 9:
            conceito = 'A'
        result_final = (media > 6 and 'Aprovado' or 'Reprovado')
    else:
        return 'Valor Inválido!'
    return nota1, nota2,media, conceito, result_final

# exercicio numero 15
def tipo_triangulo(lado1, lado2, lado3):
    math.isnan(lado1)
    math.isnan(lado2)
    math.isnan(lado3)
    if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
        if lado1 == lado2 == lado3:
            return 'Equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        elif lado1 != lado2 != lado3:
            return 'Escaleno'
    else:
        return 'Os parametros não formam um triângulo'

# exercico numero 16
#x' = -b/2a + R[b²-4ac] /2a
def solucao_equacao(a,b,c):
    math.isnan(a)
    math.isnan(b)
    math.isnan(c)
    if a == 0:
        return 'A equação não é do segundo grau.'

    delta = b**2 - 4*a*c
    if delta < 0:
        return 'A equação não possui raizes reais.'

    x1 = round(((-b) + math.sqrt(delta)) / 2*a)
    if delta > 0:
        x2 = round(((-b) - math.sqrt(delta)) / 2*a)
        return '{%i, %i}' % (x1,x2)

    return '{%i}' % x1

# exercico numero 17
def isbissexto(ano):
    math.isnan(ano)
    if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
            return True
    return False

import datetime

def validar_data(data):
    if type(data) is str:
        dmy = data.split('/')
        if  1 <= int(dmy[1]) <= 12 and 1 <= int(dmy[0]) <= 31:
            d = datetime.date(int(dmy[2]), int(dmy[1]), int(dmy[0]))
            if d:
                return True
    return False

def qtd_centenas_dezenas_unidades(num):
    math.isnan(num)
    max = 1000
    if num > max:
        raise ValueError('Valor maior que o permitido %i' % max)
    c = num / 100
    d = (num % 100) / 10
    u = (num % 100) % 10
    result = ''
    if c != 0:
        result = str(c) + 'c'
    if d != 0:
        result += (c != 0 and ',' or '') + str(d) + 'd'
    if u != 0:
        result += ((d != 0 or c != 0) and ',' or '') + str(u) + 'u'

    return result

# exercico numero 21
def saque(valor):
    math.isnan(valor)

    if 10 <= valor <= 600:

        def concat(a,b):
            return a + ',' + b

        isDiv = lambda x,y: x % y != x

        n = lambda x,y: str(x / y) + 'X$' + str(y)

        result = []
        for i in [100,50,10,5,1]:
            if isDiv(valor, i):
                result.append(n(valor, i))
                valor = valor % i

        return reduce(concat, result)
    return 'Informe um valor entre 10 e 600.'

# exercicio numero 22
def isPar(valor):
    math.isnan(valor)
    return valor % 2 == 0

# exercicio numero 23
def isdecimal(valor):
    math.isnan(valor)
    return (round(valor) != valor)

# exercicio 24
def ispositivo(valor):
    math.isnan(valor)
    return valor > 0

# exercicio numero 24
def multiFunc(x, y, opt):
    math.isnan(x)
    math.isnan(y)

    if type(opt) != str :
        raise TypeError('opt invalido!')

    result = ''

    if opt.lower() == 'a':
        result = str(x) +  (isPar(x) and ' : par, ' or ' : impar, ')
        result += str(y) +  (isPar(y) and ' : par' or ' : impar')

    elif opt.lower() == 'b':
        result = str(x) +  (ispositivo(x) and ' : positivo, ' or ' : negativo, ')
        result += str(y) +  (ispositivo(y) and ' : positivo' or ' : negativo')

    elif opt.lower() == 'c':
        result = str(x) +  (isdecimal(x) and ' : decimal, ' or ' : inteiro, ')
        result += str(y) +  (isdecimal(y) and ' : decimal' or ' : inteiro')

    return result

# exercicio numero 25
def classificador(istel, islocal, ismora, isdivida, istrab):
    respostas = filter(lambda x: x,[istel, islocal, ismora, isdivida, istrab])
    if len(respostas) == 2:
        return 'Suspeita'
    elif 3 <= len(respostas) <= 4:
        return 'Cúmplice'
    elif len(respostas) == 5:
        return 'Assassino'
    return 'Inocente'
