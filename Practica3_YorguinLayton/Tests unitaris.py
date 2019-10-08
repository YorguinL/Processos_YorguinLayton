class EquacioPrimerGrau:
    def __init__(self, s):
        self.valors_es = s.split()
        print(s)

    def calcula(self):
        self.a = self.valors_es[0]
        self.operador1 = self.valors_es[1]
        self.b = self.valors_es[2]
        self.operador2 = self.valors_es[3]
        self.c = self.valors_es[4]

        if self.operador1 == "+":
            aillarA = float(self.c) - float(self.b)
        elif self.operador1 == "-":
            aillarA = float(self.c) + float(self.b)

        self.a = self.a[:-1]
        aillarX = aillarA / float(self.a)
        print("X" + self.operador2 +  str(aillarX))

equacio = EquacioPrimerGrau("2X + 4 = 10")
equacio.calcula()
