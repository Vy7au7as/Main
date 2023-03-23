class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas


    def atbulai(self):
        return self.tekstas[::-1]

    def mazosiomis(self):
        return self.tekstas.lower()

    def didziosiomis(self):
        return self.tekstas.upper()

    def zodis(self, eil_nr):
        zodziai = self.tekstas.split()
        if eil_nr <= len(zodziai):
            return zodziai[eil_nr - 1]
        else:
            return "Eilės numeris yra didesnis nei žodžių skaičius tekste."

    def skaicius_simboliai(self, simbolis):
        return self.tekstas.count(simbolis)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def info(self):
        zodziai = 0
        skaiciai = 0
        didziosios = 0
        mazosios = 0

        for simbolis in self.tekstas:
            if simbolis.isalpha():
                if simbolis.isupper():
                    didziosios += 1
                else:
                    mazosios += 1
            elif simbolis.isdigit():
                skaiciai += 1

        zodziai = len(self.tekstas.split())

        print("Žodžių skaičius:", zodziai)
        print("Skaičių tekste skaičius:", skaiciai)
        print("Didžiųjų raidžių skaičius:", didziosios)
        print("Mažųjų raidžių skaičius:", mazosios)


# Testavimas:
tekstas = input("Įveskite tekstą: ")

s1 = Sakinys(tekstas)

print("Atvirkštinis tekstas:", s1.atbulai())
print("Mažosios raidės:", s1.mazosiomis())
print("Didžiosios raidės:", s1.didziosiomis())
print("3-as žodis:", s1.zodis(3))
print("Skaičius 2 yra tekste kartu:", s1.skaicius_simboliai('2'), "kartus")
print("Tekstas su pakeistu žodžiu:", s1.pakeisti("programuotojams", "programuotojų"))
s1.info()
