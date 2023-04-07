class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal= 5
    def power(self):
        if self.ligada:
            self.ligada =False
        else:
            self.ligada = True
    def aumenta_canal(self):
         if self.ligada:
             self.canal +=1
    def diminue_canal(self):
           if self.ligada:
               self.canal -= 1
televisao = Televisao()
print('Televisao esta ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisao esta ligada: {}'.format(televisao.ligada))
print('canal: {}'.format(televisao.canal))
televisao.power()
televisao.aumenta_canal()
televisao.aumenta_canal()
print('cnal: {}'.format(televisao.canal))
televisao.diminue_canal()
print('canal: {}'.format(televisao.canal))