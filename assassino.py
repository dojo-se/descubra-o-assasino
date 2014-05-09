# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest
import random

corretos = [0,1,0]
suspeitos = ['Charles B. Abbage', 'Donald Duck Knuth', 'Ada L. Ovelace', 'Alan T. Uring', 'Ivar J. Acobson', 'Ras Mus Ler Dorf']
locais = ['Redmond', 'Palo Alto', 'San Francisco', 'Tokio', 'Restaurante no Fim do Universo', 'São Paulo', 'Cupertino', 'Helsinki', 'Maida Vale', 'Toronto']
armas =['Peixeira', 'DynaTAC 8000X (o primeiro aparelho celular do mundo)', 'Trezoitão', 'Trebuchet', 'Maça', 'Gládio']

def informacaoDaTestemunha(assassino, local, arma):
    returnArray = []
    if assassino != corretos[0]:
        returnArray.append(1)
    if local != corretos[1]:
        returnArray.append(2)
    if arma != corretos[2]:
        returnArray.append(3)
    if assassino == corretos[0] and local == corretos[1] and arma == corretos[2]:
        returnArray.append(0)
    return returnArray

def testemunha(assassino, local, arma):
    infos=informacaoDaTestemunha(assassino, local, arma)
    return random.choice(infos)
    
def detetive():
    chutes = [random.choice(range(1,len(suspeitos))), 
                    random.choice(range(1,len(locais))),
                    random.choice(range(1,len(armas)))]
    resposta = testemunha(chutes[0], chutes[1], chutes[2])                
    cont = 0
    while (resposta != 0):
        cont += 1
        if resposta == 1:
            chutes = [random.choice(range(1,len(suspeitos))), chutes[1], chutes[2]]
            resposta = testemunha(chutes[0], chutes[1], chutes[2])
        if resposta == 2:
            chutes = [chutes[0], random.choice(range(1,len(locais))), chutes[2]]
            resposta = testemunha(chutes[0], chutes[1], chutes[2])
        if resposta == 3:
            chutes = [chutes[0], chutes[1], random.choice(range(1,len(armas)))]
            resposta = testemunha(chutes[0], chutes[1], chutes[2])
    print "Foram dados %d chutes" %(cont)
    print "Assasino: %s" %(suspeitos[chutes[0]])
    print "Onde: %s" %(locais[chutes[1]])
    print "Arma: %s" %(armas[chutes[2]])
    return chutes
        
        

class TestemunhaTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(0, testemunha(1,2,1))
        
    def test_corretos(self):
        self.assertEqual(2, testemunha(1,1,1))   
        self.assertEqual(1, testemunha(2,2,1))
        self.assertEqual(3, testemunha(1,2,2))
    
    def test_info_testemunha(self):
        self.assertEqual([0], informacaoDaTestemunha(1,2,1))   
        self.assertEqual([1], informacaoDaTestemunha(2,2,1))
        self.assertEqual([2], informacaoDaTestemunha(1,1,1))
        self.assertEqual([3], informacaoDaTestemunha(1,2,2))
        
    def test_info_testemunha_dois_errados(self):
        self.assertEqual([1,2], informacaoDaTestemunha(2,1,1))
        self.assertEqual([2,3], informacaoDaTestemunha(1,1,2))
        self.assertEqual([1,3], informacaoDaTestemunha(2,2,2))
        
    def test_info_testemunha_tres_errados(self):
        self.assertEqual([1,2,3], informacaoDaTestemunha(0,0,0))
    
    
    def test_resposta_detetive(self):
        self.assertEquals(corretos, detetive())
        

if __name__ == '__main__':
    unittest.main()