# Paprašome vartotojo įvesti eilučių kiekį
num_lines = int(input("Įveskite eilučių kiekį: "))

# Paprašome vartotojo įvesti failo pavadinimą
filename = input("Įveskite failo pavadinimą (su plėtiniu): ")

# Atidarome failą ir įrašome įvestas eilutes
with open(filename, "w") as f:
    i = 1
    while i <= num_lines:
        line = input(f"Įveskite {i}-ąją eilutę: ")
        if line == "":
            break
        f.write(line + "\n")
        i += 1

print(f"Failas {filename} sėkmingai sukurtas!")
