#!usr/bin/python
# -*- coding: utf-8 -*-
import math
#import pdb

# EstruturaDeDecisao

#Faça um Programa que peça dois números e imprima o maior deles
def numeroMaior(x, y):
    math.isnan(x)
    math.isnan(y)

    if x > y:
        z = x
    elif y >= x:
        z = y
    return z

#Faça um Programa que peça um valor e mostre na tela se o valor
# é positivo ou negativo.
def valorSinal(num):
    math.isnan(num)

    if num < 0:
        result = "negativo"
    elif num >= 0:
        result = "positivo"
    return result

#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def qualSexo(op):
    dic = {'F': "Feminino", 'M': "Masculino"}
    if dic.get(op) != None:
        return dic.get(op)
    return "Sexo Inválido!"

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def tipoLetra(letra):
    if type(letra) is not str:
        raise TypeError('O parametro deve ser um letra.')
    vogais =['a','e','i','o','u']
    if vogais.__contains__(letra):
        result = 'vogal'
    else:
        result = 'consoante'
    return result

"""
Faça um programa para a leitura de duas notas parciais de um aluno.
 O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
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

#Faça um Programa que leia três números e mostre o maior deles.
def maiorEntre3(a,b,c):
    math.isnan(a)
    math.isnan(b)
    math.isnan(c)

    return max(a,b,c)

#Faça um Programa que leia três números e mostre o maior e o menor deles. 
def maiorMenorEntre3(a,b,c):
    math.isnan(a)
    math.isnan(b)
    math.isnan(c)

    return max(a,b,c) , min(a,b,c)

"""
Faça um programa que pergunte o preço de três produtos e informe qual
 produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
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

# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def ordenarListaNumeroDecrescente(lista):
    if type(lista) is not list:
        raise TypeError('Error, parametro nao e uma lista')

    if len( filter(lambda x: type(x) is not int, lista) ) > 0:
        raise AttributeError('A lista possui valor nan')

    lista.sort(reverse=True)
    return lista

"""
Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
 ou "Valor Inválido!", conforme o caso.
"""
def qualTurno(turno):
    if type(turno) == str:
        dic = {'M': 'Bom Dia!', 'N': 'Boa Noite!', 'V': 'Boa Tarde!'}
        if dic.get(turno.upper()) != None:
            return dic.get(turno.upper())
    return "Valor Inválido!"

"""
 As Organizações Tabajara resolveram dar um aumento de salário aos seus
 colaboradores e lhe contraram para desenvolver o programa que calculará
  os reajustes.

 Faça um programa que recebe o salário de um colaborador e o reajuste
 segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
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


"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
 descontos são do Imposto de Renda, que depende do salário bruto (conforme
 tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
 Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário
 Líquido corresponde ao Salário Bruto menos os descontos. O programa
 deverá pedir ao usuário o valor da sua hora e a quantidade de hora trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
    quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""
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

"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
def dia_semana(num):
    try:
        math.isnan(num)
        dic = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sabado'}
        if dic.get(num):
            return dic.get(num)
        return 'Valor Inválido!'
    except TypeError:
        return 'Valor Inválido!'

"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
 disciplina ao longo de um semestre, e calcule a sua média. A atribuição
 de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito
     correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
     ou “REPROVADO” se o conceito for D ou E.
"""
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

"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
 informar se os valores podem ser um triângulo. Indique, caso os lados
 formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados
    for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 
"""
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

#exercicio numero 23
def isdecimal(valor):
    math.isnan(valor)
    return (round(valor) != valor)

#exercicio 24
def ispositivo(valor):
    math.isnan(valor)
    return valor > 0

#exercicio numero 24
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