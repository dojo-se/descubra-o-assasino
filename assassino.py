# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest


suspeitos = ['Charles B. Abbage', 'Donald Duck Knuth', 'Ada L. Ovelace', 'Alan T. Uring', 'Ivar J. Acobson', 'Ras Mus Ler Dorf']
locais = ['Redmond', 'Palo Alto', 'San Francisco', 'Tokio', 'Restaurante no Fim do Universo', 'São Paulo', 'Cupertino', 'Helsinki', 'Maida Vale', 'Toronto']
arma =['Peixeira', 'DynaTAC 8000X (o primeiro aparelho celular do mundo)', 'Trezoitão', 'Trebuchet', 'Maça', 'Gládio']

def testemunha(assassino, local, arma):
    return True

class TestemunhaTest(unittest.TestCase):
    def test_simples(self):
        self.assertEqual(True, problema_para_resolver())

if __name__ == '__main__':
    unittest.main()