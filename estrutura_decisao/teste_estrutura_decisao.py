#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from exercicios_estrutura_decisao import *

class testeEstruturaDecisao(unittest.TestCase):

    def test_numero_maior(self):
        self.assertEquals(2, numeroMaior(1,2))

    def test_numero_maior_nan(self):
        try:
            numeroMaior('a', 'b')
        except TypeError:
            pass
        else:
            self.fail('Error test_numero_maior_nan not see TypeError')

    def test_valor_sinal_positivo(self):
        self.assertEquals("positivo", valorSinal(1))

    def test_valor_sinal_negativo(self):
        self.assertEquals("negativo", valorSinal(-2))

    def test_valor_sinal_nan(self):
        try:
            valorSinal('df')
        except TypeError:
            pass
        else:
            self.fail('Error test_valor_sinal_nan not see TypeError')

    def test_sexo_feminino(self):
        self.assertEquals("Feminino", qualSexo("F"))

    def test_sexo_masculino(self):
        self.assertEquals("Masculino", qualSexo("M"))

    def test_sexo_invalido(self):
        self.assertEquals("Sexo Inválido!", qualSexo("GLS"))

    def test_tipoLetra_vogal(self):
        self.assertEquals("vogal", tipoLetra('a'))
    
    def test_tipoLetra_consoante(self):
        self.assertEquals("consoante", tipoLetra('c'))

    def test_tipoLetra_naw(self):
        try:
            tipoLetra(1)
        except TypeError:
            pass
        else:
            self.fail('Error test_tipoLetra_naw')

    def test_situacao_aluno_Aporvado(self):
        self.assertEquals("Aprovado", situacao_aluno(nota1=7, nota2=7))

    def test_situacao_aluno_Reporvado(self):
        self.assertEquals("Reprovado", situacao_aluno(nota1=5, nota2=5))

    def test_situacao_aluno_ApovadoDistincao(self):
        self.assertEquals("Aprovado com Distinção", situacao_aluno(nota1=10, nota2=10))

    def test_situacao_aluno_nan(self):
        try:
            situacao_aluno('a','b')
        except TypeError:
            pass
        else:
            self.fail('Error test_situacao_aluno_nan')

    def test_maiorEntre3(self):
        self.assertEquals(5, maiorEntre3(1,2,5))
        self.assertEquals(5, maiorEntre3(5,1,2))
        self.assertEquals(5, maiorEntre3(1,5,2))

    def test_maiorEntre3_nan(self):
        try:
            maiorEntre3('', 1,2)
        except TypeError:
            pass
        else:
            self.fail('Error test_maiorEntre3_nan')

    def test_maiorMenorEntre3(self):
        self.assertEquals((9,2), maiorMenorEntre3(9,2,5))

    def test_maiorMenorEntre3_nan(self):
        try:
            maiorMenorEntre3('a', 'd', 0)
        except TypeError:
            pass
        else:
            self.fail('Error test_maiorMenorEntre3_nan')

    def test_qualProdutoComprar(self):
        produtos = [Produto("PassaTempo", 3.5), Produto("Bono", 2.9), Produto("Tortinha", 2)]
        self.assertEquals("Tortinha", qualProdutoCamprar(produtos))

    def test_qualProdutoCamprar_Error(self):
        try:
            qualProdutoCamprar([1,'a',None])
        except TypeError:
            pass
        else:
            self.fail("Error test_qualProdutoCamprar")

    def test_ordenarListaNumeroDecrescente(self):
        self.assertEquals([3,2,1], ordenarListaNumeroDecrescente([1,2,3]))

    def test_ordenarListaNumeroDecrescente_nal(self):
        try:
            ordenarListaNumeroDecrescente("a")
        except TypeError:
            pass
        else:
            self.fail('Error test_ordenarListaNumeroDecrescente_nan')

    def test_ordenarListaNumeroDecrescente_nan(self):
        try:
            ordenarListaNumeroDecrescente([1,2,'a'])
        except AttributeError:
            pass
        else:
            self.fail('Error valor nao numerico na lista')

    def test_qualTurno(self):
        self.assertEquals("Boa Noite!", qualTurno('N'))
        self.assertEquals("Bom Dia!", qualTurno('M'))
        self.assertEquals("Boa Tarde!", qualTurno('V'))

    def test_qualTurno_valor_invalido(self):
        self.assertEquals("Valor Inválido!", qualTurno('Iio'))
        self.assertEquals("Valor Inválido!", qualTurno(45))

    def test_reajuste_salario(self):
        self.assertEquals((280, '20%', 56, 336.0), reajuste_salario(280))
        self.assertEquals((300, '15%', 45, 345.0), reajuste_salario(300))
        self.assertEquals((800, '10%', 80, 880.0), reajuste_salario(800))
        self.assertEquals((1600, '5%', 80, 1680.0), reajuste_salario(1600))

    def test_reajuste_salario_nan(self):
        try:
            reajuste_salario("asdf")
        except TypeError:
            pass
        else:
            self.fail('Error desconhecido.')

    def test_folha_pagamento(self):
        self.assertEquals((1100.0, 55.0, 110.0, 121.0, 165.0, 935.0), folha_pagamento(hh = 5, total_h = 220))

    def test_folha_pagamento(self):
        try:
            folha_pagamento('lol', None)
        except TypeError:
            pass
        else:
            self.fail('Error test_folha_pagamento')

    def test_dia_semana(self):
        self.assertEquals("Domingo", dia_semana(1))
        self.assertEquals("Segunda", dia_semana(2))
        self.assertEquals("Terça"  , dia_semana(3))
        self.assertEquals('Quarta' , dia_semana(4))
        self.assertEquals('Quinta' , dia_semana(5))
        self.assertEquals('Sexta'  , dia_semana(6))
        self.assertEquals('Sabado' , dia_semana(7))

    def test_dia_semana_invalido(self):
        self.assertEquals('Valor Inválido!', dia_semana(8))
        self.assertEquals('Valor Inválido!', dia_semana("adsfdsf"))
        self.assertEquals('Valor Inválido!', dia_semana(None))

    def test_valor_conceito(self):
        self.assertEquals((10, 10, 10, 'A', 'Aprovado'), valor_conceito(10,10))
        self.assertEquals((8, 8, 8, 'B', 'Aprovado'), valor_conceito(8,8))
        self.assertEquals((7, 7, 7, 'C', 'Aprovado'), valor_conceito(7,7))
        self.assertEquals((5, 5, 5, 'D', 'Reprovado'), valor_conceito(5,5))
        self.assertEquals((2, 2, 2, 'E', 'Reprovado'), valor_conceito(2,2))

    def test_valor_conceito_nan(self):
        try:
            valor_conceito('a',2)
        except TypeError:
            pass
        else:
            self.fail('Error test_atribuir_conceito_nan')

    def test_valor_conceito_Error(self):
        self.assertEquals('Valor Inválido!', valor_conceito(100, 0))
        self.assertEquals('Valor Inválido!', valor_conceito(0,100))

    def test_tipo_triangulo_equilatero(self):
        self.assertEquals('Equilátero', tipo_triangulo(2,2,2))

    def test_tipo_triangulo_isosceles(self):
        self.assertEquals('Isósceles', tipo_triangulo(2,2,3))

    def test_tipo_triangulo_escaleno(self):
        self.assertEquals('Escaleno', tipo_triangulo(2,3,4))

    def test_tipo_triangulo_nao_triangulo(self):
        self.assertEquals('Os parametros não formam um triângulo',\
        tipo_triangulo(1,4,9))

    def test_tipo_triangulo_nan(self):
        try:
            tipo_triangulo('s', None, 6)
        except TypeError as e:
            self.assertEquals('a float is required', e.message)
        else:
            self.fail('Error inesperado')

    #x' = -b/2a + R[b²-4ac] /2a
    def test_solucao_equacao(self):
        #func = 2x² + 3x + 1
        # x = -3/2*2 - sqr(3² - 4*2*1)/2*2
        # x = -3/4 - sqr(9 - 8)/4
        # x' = -3/4 - 1/4 = - 1
        # x'' = -3/4 + 1/4 = - 1/2
        self.assertEquals('{5, -4}',\
         solucao_equacao(a = 1, b = -1, c = -20))

    def test_solucao_equacao_delta_negativo(self):
        # func = x² +x + 10
        # delta = 1 - 4*1*10 = -
        self.assertEquals('A equação não possui raizes reais.',\
        solucao_equacao(a = 1, b = 1, c = 10))

    def test_solucao_equacao_delta_zero(self):
        #func x² + 2x + 1
        #delta = 4 - 4 *1 *1 = 0
        # x = -2/2 + sqr(4 - 4*1*1)/2
        # x = -1 + sqr(0)/2 = -1
        self.assertEquals('{-1}', solucao_equacao(a = 1, b = 2, c = 1))

    def test_solucao_equacao_nan(self):
        try:
            solucao_equacao("","",2)
        except TypeError:
            pass
        else:
            self.fail('Error test_solucao_equacao_nan.')

    def test_solucao_equacao_a_zero(self):
        self.assertEquals('A equação não é do segundo grau.',\
         solucao_equacao(a = 0, b = 1, c = 1))

    def test_isbissexto(self):
        self.assertTrue(isbissexto(2012))
        self.assertTrue(isbissexto(2008))
        self.assertTrue(isbissexto(2016))

    def test_validar_data(self):
        self.assertTrue(validar_data('11/10/2001'))

    def test_validar_data_data_errada(self):
        self.assertFalse(validar_data('320/13/15'))
        self.assertFalse(validar_data('33/130/150'))
        self.assertFalse(validar_data('32/13//122'))

    def test_qtd_centenas_dezenas_unidades(self):
        self.assertEquals('3c,2d,6u', qtd_centenas_dezenas_unidades(326))
        self.assertEquals('1d,2u', qtd_centenas_dezenas_unidades(12))
        self.assertEquals('3c', qtd_centenas_dezenas_unidades(300))
        self.assertEquals('1c', qtd_centenas_dezenas_unidades(100))
        self.assertEquals('3c,2d', qtd_centenas_dezenas_unidades(320))
        self.assertEquals('3c,1u', qtd_centenas_dezenas_unidades(301))
        self.assertEquals('6u', qtd_centenas_dezenas_unidades(6))

    def test_qtd_centenas_dezenas_unidades_nan(self):
        try:
            qtd_centenas_dezenas_unidades("asdf")
        except TypeError:
            pass
        else:
            self.fail('test_qtd_centenas_dezenas_unidades_nan error')

    def test_saque_caixa(self):
        self.assertEquals('2X$100,1X$50,1X$5,1X$1', saque(256))
        self.assertEquals('2X$100,1X$5', saque(205))
        self.assertEquals('3X$100,1X$50,4X$10,1X$5,4X$1', saque(399))

    def test_saque_fora_range(self):
        self.assertEquals('Informe um valor entre 10 e 600.', saque(1000))
        self.assertEquals('Informe um valor entre 10 e 600.', saque(1))

    def test_saque_nan(self):
        try:
            saque('asdf')
        except TypeError:
            pass
        else:
            self.fail('test_saque_nan error')

    def test_par_ou_impar(self):
        self.assertTrue(isPar(2))
        self.assertTrue(isPar(4))
        self.assertFalse(isPar(1))
        self.assertFalse(isPar(1))

    def test_par_ou_impar_error(self):
        try:
            isPar('asdfaf')
        except TypeError:
            pass
        else:
            self.fail('test_par_ou_impar_error')

    def test_isdecimal(self):
        self.assertTrue(isdecimal(1.2))
        self.assertTrue(isdecimal(1.0000000000001))
        self.assertTrue(isdecimal(2.32))
        self.assertFalse(isdecimal(1))
        self.assertFalse(isdecimal(0))
        self.assertFalse(isdecimal(77665))

    def test_isdecimal_nan(self):
        try:
            isdecimal('adfadf','adsfafd')
        except TypeError:
            pass
        else:
            self.fail('test_isdecimal_nan : numero de parametros Inválido')

    def test_multiFunc(self):
        self.assertEquals('20 : par, 33 : impar', multiFunc(20, 33, 'a'))
        self.assertEquals('11 : impar, 4 : par', multiFunc(11, 4, 'a'))
        self.assertEquals('20 : par, 33 : impar', multiFunc(20, 33, 'a'))
        self.assertEquals('11 : impar, 4 : par', multiFunc(11, 4, 'a'))

        self.assertEquals('7 : positivo, -3 : negativo', multiFunc(7, -3, 'b'))
        self.assertEquals('-1 : negativo, 2 : positivo', multiFunc(-1, 2, 'b'))

        self.assertEquals('7 : inteiro, 0.1 : decimal', multiFunc(7, 0.1, 'c'))
        self.assertEquals('0 : inteiro, -0.22 : decimal', multiFunc(0, -0.22, 'c'))

    def test_classificador(self):
        import random
        suspeito = [True, True, False, False, False]

        for i in range(60):
            params = random.sample(suspeito, 5)
            self.assertEquals('Suspeita', classificador(params[0], params[1],\
                params[2], params[3], params[4]))

        cumplice = [True, True, True, True, False, False]

        for i in range(60):
            params = random.sample(cumplice, 5)
            self.assertEquals('Cúmplice', classificador(params[0], params[1],\
                params[2], params[3], params[4]))

        self.assertEquals('Assassino', classificador(True, True, True, True, True))
        self.assertEquals('Inocente', classificador(False, False, False, False, False))


if __name__ == "__main__":
    unittest.main()

