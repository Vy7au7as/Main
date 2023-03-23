# def skaiciu_suma(a, b, c):
#     suma = a + b + c
#     return suma
# Įvedame skaičius
# skaicius1 = int(input("Įveskite pirmą skaičių: "))
# skaicius2 = int(input("Įveskite antrą skaičių: "))
# skaicius3 = int(input("Įveskite trečią skaičių: "))

# Iškviečiame funkciją ir išspausdiname rezultatą
# suma = skaiciu_suma(skaicius1, skaicius2, skaicius3)
# print("Skaičių suma:", suma)
# print('=====Užduotis #1 atlikta=====')
#
# def skaiciu_saraso_suma(sarasas):
#     suma = 0
#     for skaicius in sarasas:
#         suma += skaicius
#     return suma
#
# pavyzdys naudojant funkciją
# skaiciu_sarasas = [2, 5, 8, 10]
# rezultatas = skaiciu_saraso_suma(skaiciu_sarasas)
# print(rezultatas) # spausdinama 25

print('=====Užduotis #2 atlikta=====')
# def print_max_number(*args):
#     max_num = max(args)
#     print(f"Didžiausias sk.: {max_num}")
#
# print_max_number(1, 5, 9, -3, 0)
# spausdina Didžiausias sk.: 9
#
#
print('=====Užduotis #3 atlikta=====')
# def reverse_string(string):
#     return string[::-1]
# print(reverse_string("labas")) # spausdins "sabal"
# print(reverse_string("hello world")) # spausdins "dlrow olleh"
# print('=====Užduotis #4 atlikta=====')
#
# def count_chars(string):
#     word_count = len(string.split())
#     upper_count = sum(1 for c in string if c.isupper())
#     lower_count = sum(1 for c in string if c.islower())
#     digit_count = sum(1 for c in string if c.isdigit())
#     print(f"Žodžio sk.: {word_count}") # Žodžių sk.: 6 print
#     print(f"Didžiosios raidžių sk.: {upper_count}") #Didžiosios raidės.: 6
#     print(f"Mažūjų raidžių sk.: {lower_count}") # Mažųjų raidžių sk.: 23
#     print(f"Numerių sk.: {digit_count}") # Skaičių sk.: 8
#
# count_chars("Labas rytas! 2023 m. - COVID19 nugalėsime.")


print('=====Užduotis #5 atlikta=====')
# def get_unique_list(lst):
#     return list(set(lst))
# my_list = [1, 2, 3, 2, 4, 5, 1, 6, 3]
# unique_list = get_unique_list(my_list)
# print(unique_list)  # prints [1, 2, 3, 4, 5, 6]
#
#
print('=====Užduotis #6 atlikta=====')
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
# sk = int(input("Įveskite skaičių, kad sužinotumėte, ar jis pirminis: "))
# print(is_prime(sk))  # output: True or False
#
#
print('=====Užduotis #7 atlikta=====')
# def reverse_words(string):
#     words = string.split()
#     reversed_words = words[::-1]
#     return " ".join(reversed_words)

# text = "Labas rytas, pasauli!"
# reversed_text = reverse_words(text)
# print(reversed_text)  # "pasauli! rytas, Labas"



print('=====Užduotis #8 atlikta=====')
# def is_leap_year(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
# year = int(input("Įveskite metus, kad paskaičiuotų: "))
# print(is_leap_year(year))
print('=====Užduotis #9 atlikta=====')

from datetime import datetime, timedelta

from datetime import datetime

# def time_since(date_string):
#     try:
#         now = datetime.now()
#         date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
#         delta = now - date
#         years = delta.days // 365
#         months = delta.days % 365 // 30
#         days = delta.days % 365 % 30
#         hours = delta.seconds // 3600
#         minutes = delta.seconds % 3600 // 60
#         seconds = delta.seconds % 3600 % 60
#         return f"{years} metų, {months} mėnesių, {days} dienų, {hours} valandų, {minutes} minučių, {seconds} sekundžių praėjo nuo {date_string}."
#     except ValueError:
#         return "NEGALIMA PASKAIČIUOTI: neteisinga datos formatas"
#
# date_string = input("Įveskite data ir laiką, kad paskaičiuotų pvz., '2022-01-01 12:00:00': ")
# print(time_since(date_string))


print('=====Užduotis #10 atlikta=====')
def generate_personal_code(passport_number, birth_date):
    # patikriname, ar paduoti parametrai yra teisingo formato
    if not isinstance(birth_date, datetime):
        raise ValueError("Gimimo data turi būti datetime objektas")
    if not isinstance(passport_number, str) or len(passport_number) != 9:
        raise ValueError("Paso numeris turi būti devynių simbolių ilgio")

    # išgauti gimimo datos metus, mėnesį ir dieną iš paso numerio
    birth_year = int("19" + passport_number[0:2])
    birth_month = int(passport_number[2:4])
    birth_day = int(passport_number[4:6])

    # nustatome lyties kodą
    gender_code = "4" if int(passport_number[-2]) % 2 == 0 else "3"

    # nustatome gimimo datos kodą
    year = str(birth_year)[-2:]
    month = f"{birth_month:02d}"
    day = f"{birth_day:02d}"
    birth_code = f"{year}{month}{day}"

    # sujungiame visus kodų dalis, kad gautume pilną asmens kodą
    personal_code = f"{birth_code}{gender_code}{passport_number[-3:]}"

    def validate_personal_code(personal_code):
        factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        try:
            nums = [int(n) for n in personal_code]
        except ValueError:
            return False
        if len(nums) != 11:
            return False
        s = sum([a * b for a, b in zip(nums, factors)])
        return s % 11 == 0

    # patikriname, ar sugeneruotas asmens kodas yra validus
    if not validate_personal_code(personal_code):
        raise ValueError("Sugeneruotas asmens kodas yra neteisingas")

    print(f"Sugeneruotas asmens kodas: {personal_code}")
    return personal_code


print('=====Užduotis #11 atlikta=====')
from datetime import datetime

def generate_personal_code(passport_number: str, birth_date: datetime) -> str:
    # Patikriname, ar paduoti parametrai yra teisingo formato
    if not isinstance(birth_date, datetime):
        raise ValueError("Gimimo data turi būti datetime objektas")
    if not isinstance(passport_number, str) or len(passport_number) != 9:
        raise ValueError("Paso numeris turi būti devynių simbolių ilgio")

    # Išgauti gimimo datos metus, mėnesį ir dieną iš paso numerio
    birth_year = int("19" + passport_number[0:2])
    birth_month = int(passport_number[2:4])
    birth_day = int(passport_number[4:6])

    # Nustatome lyties kodą
    gender_code = "4" if int(passport_number[-2]) % 2 == 0 else "3"

    # Nustatome gimimo datos kodą
    year = str(birth_year)[-2:]
    month = f"{birth_month:02d}"
    day = f"{birth_day:02d}"
    birth_code = f"{year}{month}{day}"

    # Sujungiame visus kodų dalis, kad gautume pilną asmens kodą
    personal_code = f"{birth_code}{gender_code}{passport_number[-3:]}"

    # Patikriname, ar sugeneruotas asmens kodas yra validus
    if not (len(personal_code) == 11 and personal_code.isdigit()):
        raise ValueError("Sugeneruotas asmens kodas yra neteisingas")

    # Sugeneruotas asmens kodas yra validus
    return personal_code


print('=====Užduotis #13 atlikta=====')
# import random
#
#
# def asmens_kodo_generavimas(lytis, gim_data, eil_nr):
#     # Lyčių skaičių priskyrimas pagal gimimo metus
#     metai = gim_data.split('-')[0]
#     if int(metai) >= 2000:
#         vyru_sk = '1'
#         moteru_sk = '2'
#     else:
#         vyru_sk = '3'
#         moteru_sk = '4'
#
#     # Pagal lytį priskiriama pirmoji asmens kodo skaitmenų dalis
#     if lytis == 'Vyras':
#         pirmas_sk = '3'
#     else:
#         pirmas_sk = '4'
#
#     # Asmens kodo skaičių dalis
#     asmens_kodo_dalis = pirmas_sk + vyru_sk + gim_data.replace('-', '')[2:] + eil_nr
#
#     # Skaičių patikrinimas ir kontrolinio skaičiaus apskaičiavimas
#     skaiciai = list(map(int, asmens_kodo_dalis))
#     kontrolinis_skaicius = (1 * skaiciai[0] + 2 * skaiciai[1] + 3 * skaiciai[2] + 4 * skaiciai[3] + 5 * skaiciai[
#         4] + 6 * skaiciai[5] + 7 * skaiciai[6] + 8 * skaiciai[7] + 9 * skaiciai[8] + 1 * skaiciai[9]) % 11
#     if kontrolinis_skaicius == 10:
#         kontrolinis_skaicius = (3 * skaiciai[0] + 4 * skaiciai[1] + 5 * skaiciai[2] + 6 * skaiciai[3] + 7 * skaiciai[
#             4] + 8 * skaiciai[5] + 9 * skaiciai[6] + 1 * skaiciai[7] + 2 * skaiciai[8] + 3 * skaiciai[9]) % 11
#         if kontrolinis_skaicius == 10:
#             kontrolinis_skaicius = 0
#
#     # Asmens kodo sugeneravimas
#     asmens_kodas = asmens_kodo_dalis + str(kontrolinis_skaicius)
#
#     return asmens_kodas



print ('==========================================================================')

# Vartotojo įvestų duomenų nuskaitymas
# lytis = input('Įveskite lytį: ')
# gim_data = input('Įveskite gimimo data formatu mmmm-mm-dd: ')

# Atsitiktinis eilės numeris
# eil_nr = str(random.randint(1, 999)).zfill(3)
#
# Asmens kodo sugeneravimas
# asmens_kodas = asmens_kodo_generavimas(lytis, gim_data, eil_nr)
#
# print(f"Jūsų asmens kodas:", asmens_kodas)
print('=====================================================')
def get_next_number(string):
    result = ""
    for i in range(len(string) - 1):
        result += f"{string[i]} - {int(string[i])+1}{string[i+1]}, "
    result += f"{string[-1]} - {int(string[-1])+1}"
    return result

number = input("Įveskite sk. pvz. - 5678: ")

print(get_next_number(number)) # 5 - 46, 6 - 57, 7 - 68, 8 - 79

