import pickle

def ivesti_ir_saikuoti_duomenis(sarasas):
    try:
        suma = float(input("Iveskite suma: "))
        komentaras = input("Iveskite komentara: ")
        sarasas.append((suma, komentaras))
        with open('duomenys.pkl', 'wb') as f:
            pickle.dump(sarasas, f)
    except ValueError:
        print("Klaida: neteisinga įvestis, prašome įvesti skaičių.")

def skaiciuoti_balansa(sarasas):
    balansas = 0
    for suma, komentaras in sarasas:
        balansas += suma
    return balansas

try:
    with open('duomenys.pkl', 'rb') as f:
        sarasas = pickle.load(f)
except FileNotFoundError:
    sarasas = []

while True:
    print("Pajamos (-) / Islaidos (+) / Baigti (q)")
    pasirinkimas = input("Iveskite pasirinkima\nPajamos= (-)\nIšlaidos= (+)\nBaigti= (q):\n ")
    if pasirinkimas == 'q':
        break
    elif pasirinkimas == '+':
        ivesti_ir_saikuoti_duomenis(sarasas)
    elif pasirinkimas == '-':
        ivesti_ir_saikuoti_duomenis(sarasas)
    else:
        print("Klaida: neteisingas pasirinkimas.")

    print("Pajamos/Islaidos:")
    for suma, komentaras in sarasas:
        print(f"{komentaras}: {suma}")
    print(f"Balansas: {skaiciuoti_balansa(sarasas)}")
