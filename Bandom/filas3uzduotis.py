import os
from datetime import datetime

dabartinis_laikas = datetime.today()


# Sukuriame katalogą
os.mkdir("Naujas Katalogas")

# Sukuriame tekstinį failą su šiandienos data ir laiku
filename = datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
filepath = os.path.join("Naujas Katalogas", filename)

with open(filepath, "w") as f:
    f.write("Sukurtas " + filename + "\n")

# Atspausdiname failo sukūrimo datą ir dydį baitais
statinfo = os.stat(filepath)
created = datetime.fromtimestamp(statinfo.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
size = statinfo.st_size

print(f"Failas sukurtas {created}. Dydis: {size} baitai.")
