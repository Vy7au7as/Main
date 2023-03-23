
from Bandom.modules.python_kursas import PythonKursas

from Bandom.modules.kursas import Kursas

# Inicijuoti Kursas objektą su norimomis savybėmis
kursas = Kursas("Matematika", "Jonas", "30 valandų")

# Inicijuoti PythonKursas objektą su norimomis savybėmis
python_kursas = PythonKursas("Python Programavimas", "Petras", "50 valandų")

# Paleisti abiejų objektų metodą destyti()
kursas.destyti()
python_kursas.destyti()
