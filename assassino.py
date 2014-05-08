# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

corretos = [1,1,1]
suspeitos = ['Charles B. Abbage', 'Donald Duck Knuth', 'Ada L. Ovelace', 'Alan T. Uring', 'Ivar J. Acobson', 'Ras Mus Ler Dorf']
locais = ['Redmond', 'Palo Alto', 'San Francisco', 'Tokio', 'Restaurante no Fim do Universo', 'São Paulo', 'Cupertino', 'Helsinki', 'Maida Vale', 'Toronto']
arma =['Peixeira', 'DynaTAC 8000X (o primeiro aparelho celular do mundo)', 'Trezoitão', 'Trebuchet', 'Maça', 'Gládio']

def testemunha(assassino, local, arma):
    if assassino == 1 and local == 1 and arma == 1:
        return 0
        
    return True

class TestemunhaTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(True, testemunha(1,1,1))
        
    def test_corretos(self):
        self.assertEqual(0, testemunha(1,1,1))        

if __name__ == '__main__':
    unittest.main()