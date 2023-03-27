from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f"{self.vardas}, {self.amzius}"

# Inicijuojame Zmogus objektus
zmogus1 = Zmogus("Jonas", 32)
zmogus2 = Zmogus("Petras", 25)
zmogus3 = Zmogus("Ona", 29)
zmogus4 = Zmogus("Marytė", 21)

# Sudedame Zmogus objektus į sąrašą
zmogus_sarasas = [zmogus1, zmogus2, zmogus3, zmogus4]

# Surūšiuojame objektus pagal vardą ir pagal amžių, atspausdiname ir atvirkščiai surūšiuojame ir atspausdiname
print("Surūšiuota pagal vardą:")
vardu_rusiavimas = sorted(zmogus_sarasas, key=attrgetter("vardas"))
print(vardu_rusiavimas)

print("Atvirkščiai surūšiuota pagal vardą:")
vardu_rusiavimas_atvirksciai = sorted(zmogus_sarasas, key=attrgetter("vardas"), reverse=True)
print(vardu_rusiavimas_atvirksciai)

print("Surūšiuota pagal amžių:")
amziaus_rusiavimas = sorted(zmogus_sarasas, key=attrgetter("amzius"))
print(amziaus_rusiavimas)

print("Atvirkščiai surūšiuota pagal amžių:")
amziaus_rusiavimas_atvirksciai = sorted(zmogus_sarasas, key=attrgetter("amzius"), reverse=True)
print(amziaus_rusiavimas_atvirksciai)
