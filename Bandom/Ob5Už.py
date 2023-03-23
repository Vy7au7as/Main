class Minibiudzetas:
    def __init__(self):
        self.pajamos = 0
        self.islaidos = 0
        self.irasai = []

    def prideti_pajamas(self, suma):
        self.pajamos += suma
        self.irasai.append(('Pajamos', suma))

    def prideti_islaidas(self, suma):
        self.islaidos += suma
        self.irasai.append(('Išlaidos', suma))

    def gauti_balansa(self):
        return self.pajamos - self.islaidos

    def gauti_ataskaita(self):
        ataskaita = "Biudžeto ataskaita:\n"
        for irasas in self.irasai:
            ataskaita += f"{irasas[0]}: {irasas[1]} EUR\n"
        ataskaita += f"Balansas: {self.gauti_balansa()} EUR\n"
        return ataskaita

minibiudzetas = Minibiudzetas()

while True:
    print("Pasirinkite veiksmą:")
    print("1. Pridėti pajamas")
    print("2. Pridėti išlaidas")
    print("3. Gauti balansą")
    print("4. Gauti biudžeto ataskaitą")
    print("5. Išeiti")

    pasirinkimas = input("Įveskite veiksmo numerį: ")

    if pasirinkimas == "1":
        suma = float(input("Įveskite pajamų sumą: "))
        minibiudzetas.prideti_pajamas(suma)
        print("Pajamos pridėtos.")

    elif pasirinkimas == "2":
        suma = float(input("Įveskite išlaidų sumą: "))
        minibiudzetas.prideti_islaidas(suma)
        print("Išlaidos pridėtos.")

    elif pasirinkimas == "3":
        balansas = minibiudzetas.gauti_balansa()
        print(f"Balansas: {balansas} EUR")

    elif pasirinkimas == "4":
        ataskaita = minibiudzetas.gauti_ataskaita()
        print(ataskaita)

    elif pasirinkimas == "5":
        print("Programa baigia darbą.")
        break

    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")
