class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Automobilis: {self.metai} {self.modelis} {self.kuro_tipas}")

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


# Sukuriam Automobilis objektą
auto = Automobilis(2022, "Audi", "benzinas")

# Paleidžiam funkcijas vaziuoti, stoveti, pildyti_degalu su Automobilis objektu
auto.vaziuoti()
auto.stoveti()
auto.pildyti_degalu()

print()

# Sukuriam Elektromobilis objektą
elektro = Elektromobilis(2022, "Tesla", "elektra")

# Paleidžiam funkcijas vaziuoti, stoveti, pildyti_degalu su Elektromobilis objektu
elektro.vaziuoti()
elektro.stoveti()
elektro.pildyti_degalu()

# Paleidžiam naują Elektromobilio metodą vaziuoti_autonomiskai
elektro.vaziuoti_autonomiskai()
