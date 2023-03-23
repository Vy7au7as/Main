from datetime import datetime

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.strptime(dirba_nuo, '%Y-%m-%d').date()

    def __days_worked(self):
        today = datetime.today().date()
        days_worked = (today - self.dirba_nuo).days // 7 * 7
        return days_worked

    def paskaiciuoti_atlyginima(self):
        days_worked = self.__days_worked()
        atlyginimas = 8 * self.valandos_ikainis * days_worked
        return atlyginimas

class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    def paskaiciuoti_atlyginima(self):
        days_worked = self._Darbuotojas__days_worked()
        atlyginimas = 8 * self.valandos_ikainis * days_worked * 5 / 7
        return round(atlyginimas, 2)

# Sukuriame norimus objektus
darbuotojas1 = Darbuotojas('Jonas', 10, '2022-01-01')
normalus_darbuotojas1 = NormalusDarbuotojas('Petras', 10, '2022-01-01')

# Paskaičiuojame atlyginimus ir išvedame rezultatus
print(f'{darbuotojas1.vardas} gavo {darbuotojas1.paskaiciuoti_atlyginima()} eurų už darbą.')
print(f'{normalus_darbuotojas1.vardas} gavo {normalus_darbuotojas1.paskaiciuoti_atlyginima()} eurų už darbą.')

print("==============================================================")
import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo


    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return skirtumas.days * 8

    def paskaiciuoti_atlyginima(self):
        atlyginimas = self.valandos_ikainis * self._kiek_dirba_valandu()
        print (self.vardas + " uždirbo " + str(atlyginimas))

class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dirba_valandu(self):
        nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
        dabar = datetime.datetime.today()
        skirtumas = dabar - nuo_kada_dirba
        return (skirtumas.days * 8) / 7 * 5


donatas = Darbuotojas("Donatas", 10, "2022, 01, 01, 12, 00, 00")
donatas_normalus = NormalusDarbuotojas("Donatas", 10, "2022, 01, 01, 12, 00, 00")
donatas.paskaiciuoti_atlyginima()
donatas_normalus.paskaiciuoti_atlyginima()

