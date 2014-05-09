import testemunha

class Detetive(object):
   """Classe detetive que vai investigar quem foi o assassino"""
   def __init__(self, testemunha, suspeitos, locais, armas):
      self.testemunha = testemunha
      self.suspeitos = suspeitos
      self.locais = locais
      self.armas = armas
      
   def Investigar(self):
      hipotese =  -1
      suspeito_corrente = 0
      local_corrente       = 0
      arma_corrente      = 0

      while(hipotese != 0 and len(self.suspeitos) > suspeito_corrente and len(self.locais) > local_corrente and len(self.armas) > arma_corrente):
         hipotese = self.Hipotese(suspeito_corrente, local_corrente, arma_corrente)
         if hipotese == 1:
            suspeito_corrente += 1
         elif  hipotese == 2:
            local_corrente += 1
         elif hipotese == 3:
            arma_corrente +=1

      if hipotese == 0:   
         print "Crime resolvido: {0} assassinou a vitima usando {1} em {2}".format( \
            self.suspeitos[suspeito_corrente], \
            self.armas[arma_corrente], \
            self.locais[local_corrente])
         return [suspeito_corrente, local_corrente, arma_corrente]
      else:
         print "Prendam a testemunha por falso testemunho!"
         return False

   def Hipotese(self, suspeito, local, arma):
      print "Testemunha, Foi {0} usando {1} em {2}?".format( \
         self.suspeitos[suspeito], \
         self.armas[arma], \
         self.locais[local])
      return self.testemunha.foi(suspeito, local, arma)