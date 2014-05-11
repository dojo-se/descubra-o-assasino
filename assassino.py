# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest
import random
from testemunha import Testemunha
from detetive import Detetive


suspeitos = ['Charles B. Abbage', 'Donald Duck Knuth', 'Ada L. Ovelace', 'Alan T. Uring', 'Ivar J. Acobson', 'Ras Mus Ler Dorf']
locais = ['Redmond', 'Palo Alto', 'San Francisco', 'Tokio', 'Restaurante no Fim do Universo', 'São Paulo', 'Cupertino', 'Helsinki', 'Maida Vale', 'Toronto']
armas =['Peixeira', 'DynaTAC 8000X (o primeiro aparelho celular do mundo)', 'Trezoitão', 'Trebuchet', 'Maça', 'Gládio']

class TestemunhaTest(unittest.TestCase):
    def setUp(self):
        self.crime = [1, 2, 1]
        self.testemunha = Testemunha(self.crime[0], self.crime[1], self.crime[2])

    def selecionarSuspeitoErrado(self):
        suspeito_errado = self.crime[0]
        while suspeito_errado == self.crime[0]:
            suspeito_errado = random.choice(range(0,len(suspeitos)))
        return suspeito_errado

    def selecionarLocalErrado(self ):
        local_errado = self.crime[1]
        while local_errado == self.crime[1]:
            local_errado = random.choice(range(0,len(locais)))
        return local_errado

    def selecionarArmaErrada(self):
        arma_errada = self.crime[2]
        while arma_errada == self.crime[2]:
            arma_erraada = random.choice(range(0,len(armas)))
        return arma_errada
    
    def test_hipoteseTodaErrada(self):
        for i in range(0,100):
            suspeito_errado = self.selecionarSuspeitoErrado
            local_errado = self.selecionarLocalErrado
            arma_errada = self.selecionarArmaErrada
            self.assertIn(self.testemunha.foi(suspeito_errado, local_errado, arma_errada), [1,2,3])
        
    def test_hipoteseSuspeitoCerto(self):
        suspeito = self.crime[0]
        for i in range(0,100):
            local_errado = self.selecionarLocalErrado
            arma_errada = self.selecionarArmaErrada
            testemunho = self.testemunha.foi(suspeito, local_errado, arma_errada)
            self.assertIn(testemunho, [2,3])
            self.assertNotEqual(1, testemunho)

    def test_hipoteseLocalCerto(self):
        local = self.crime[1]
        for i in range(0,100):
            suspeito_errado = self.selecionarSuspeitoErrado
            arma_errada = self.selecionarArmaErrada
            testemunho = self.testemunha.foi(suspeito_errado, local, arma_errada)
            self.assertIn(testemunho, [1,3])
            self.assertNotEqual(2, testemunho)

    def test_hipoteseArmaCerta(self):
        arma = self.crime[2]
        for i in range(0,100):
            suspeito_errado = self.selecionarSuspeitoErrado
            local_errado = self.selecionarLocalErrado
            testemunho = self.testemunha.foi(suspeito_errado, local_errado, arma)
            self.assertIn(testemunho, [1,2])
            self.assertNotEqual(3, testemunho) 

    def test_hipoteseSuspeitoELocalCertos(self):
        suspeito = self.crime[0]
        local = self.crime[1]
        for i in range(0,100):
            arma_errada = self.selecionarArmaErrada
            testemunho = self.testemunha.foi(suspeito, local, arma_errada)
            self.assertEqual(3, testemunho) 
    
    def test_hipoteseSuspeitoEArmaCertos(self):
        suspeito = self.crime[0]
        arma = self.crime[2]
        for i in range(0,100):
            local_errado = self.selecionarLocalErrado
            testemunho = self.testemunha.foi(suspeito, local_errado, arma)
            self.assertEqual(2, testemunho)

    def test_hipoteseLocalEArmaCertos(self):
        local = self.crime[1]
        arma = self.crime[2]
        for i in range(0,100):
            suspeito_errado = self.selecionarSuspeitoErrado
            testemunho = self.testemunha.foi(suspeito_errado, local, arma)
            self.assertEqual(1, testemunho)

    def test_hipoteseCerta(self):
        suspeito = self.crime[0]
        local = self.crime[1]
        arma = self.crime[2]
        self.assertEqual(0, self.testemunha.foi(suspeito, local, arma))


class DetetiveTest(unittest.TestCase):
    def setUp(self):
        self.crime = [1, 2, 1]
        self.testemunha = Testemunha(self.crime[0], self.crime[1], self.crime[2])
        self.detetive = Detetive(self.testemunha, suspeitos, locais, armas)

    def test_investigacao(self):
        self.assertEqual(self.crime, self.detetive.Investigar())

    def test_testemunhaMentirosa(self):
        crime = [ -1, -1, -1]
        testemunha = Testemunha(crime[0], crime[1], crime[2])
        detetive = Detetive(testemunha, suspeitos, locais, armas)
        self.assertEqual(False, detetive.Investigar())

if __name__ == '__main__':
    unittest.main()