import random

class Testemunha(object):
   """Classe que testemunhou o assassinato, vai informar se a hipotese do detetive esta certa"""
   def __init__(self, assassino, local, arma):
      self.assassino = assassino
      self.local = local
      self.arma = arma
   
   def foi(self, assassino, local, arma):
    acertos = []
    if assassino != self.assassino:
        acertos.append(1)
    if local != self.local:
        acertos.append(2)
    if arma != self.arma:
        acertos.append(3)
    if assassino == self.assassino and local == self.local and arma == self.arma:
        acertos.append(0)

    return random.choice(acertos)