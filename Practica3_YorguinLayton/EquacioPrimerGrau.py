class EquacioPrimerGrau1:
    def __init__(self, s):
        self.valors_es = s.split()
        #print(s)

    def calcula(self):
        self.a = self.valors_es[0]
        self.operador1 = self.valors_es[1]
        self.b = self.valors_es[2]
        self.operador2 = self.valors_es[3]
        self.c = self.valors_es[4]

        try:
            self.b = float(self.b)
        except:
            return "l'equacio conte caracter no calculables: " + self.b

        if self.operador1 == "+":
            aillarA = float(self.c) - float(self.b)
        elif self.operador1 == "-":
            aillarA = float(self.c) + float(self.b)
        else:
            return "Operador no valid: " + self.operador1

        self.a = self.a[:-1]
        aillarX = aillarA / float(self.a)
        return aillarX
        #print ("X" + self.operador2 +  str(aillarX))

equacio = EquacioPrimerGrau1("2X + 4 = 10")
equacio.calcula()
