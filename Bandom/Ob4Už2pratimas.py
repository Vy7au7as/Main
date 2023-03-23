from datetime import datetime, timedelta

class Sukaktis:
    def __init__(self, metai, menesis, diena, valanda, minute, sekunde):
        self.data = datetime(metai, menesis, diena, valanda, minute, sekunde)

    def __str__(self):
        return self.data.strftime('%Y-%m-%d %H:%M:%S')

    def praėjo_laiko_periodas(self, kitos_datos):
        periodas = kitos_datos.data - self.data
        metų = periodas.days // 365
        savaitės = periodas.days // 7
        dienos = periodas.days
        valandos = periodas.seconds // 3600
        minutės = (periodas.seconds // 60) % 60
        sekundės = periodas.seconds % 60
        print(f"Praėjo {metų} metų, {savaitės} savaičių, {dienos} dienų, {valandos} valandų, {minutės} minučių ir {sekundės} sekundžių.")

    def keliamieji_metai(self):
        metai = self.data.year
        if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
            print(f"{metai} metai yra keliamieji.")
        else:
            print(f"{metai} metai nėra keliamieji.")

    def atimti_dienas(self, dienos):
        nauja_data = self.data - timedelta(days=dienos)
        return Sukaktis(nauja_data.year, nauja_data.month, nauja_data.day, nauja_data.hour, nauja_data.minute, nauja_data.second)

    def pridėti_dienas(self, dienos):
        nauja_data = self.data + timedelta(days=dienos)
        return Sukaktis(nauja_data.year, nauja_data.month, nauja_data.day, nauja_data.hour, nauja_data.minute, nauja_data.second)

# Sukuriam naują sukaktį
sukaktis = Sukaktis(1990, 10, 20, 12, 30, 15)
print(sukaktis)  # spausdinam sukakties datą ir laiką

# Skaičiuojam laiko periodą tarp dviejų sukakčių
kitos_datos = input(2022, 3, 7, 0, 0, 0)
sukaktis.praėjo_laiko_periodas(kitos_datos)

# Tikrinam, ar metai yra keliamieji
sukaktis.keliamieji_metai()

# Atimam dienas ir gautą naują datą spausdinam
nauja_data = sukaktis.atimti_dienas(30)
print(nauja_data)

# Pridedam dienas ir gautą naują datą sp
