import math

my_list = [1, 4, 9, 16, 25]
sqrt_list = []

for element in my_list:
    sqrt = math.sqrt(element)
    sqrt_list.append(sqrt)

print("Pradinis sarasas:", my_list)
print("Ištrauktos šaknies sarasas:", sqrt_list)

print ('=============Šaknis ištraukta - 6 užduotis===================')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []

for element in my_list:
    if element % 2 == 0:
        even_list.append(element)

print("Pradinis sarasas:", my_list)
print("Galutinis sarasas:", even_list)
print ('=============Lyginiai sk.7užduotis===================')
my_list = [-5, 3, 0, -2, 7, -1, 4]
positive_list = []
negative_list = []

for element in my_list:
    if element >= 0:
        positive_list.append(element)
    else:
        negative_list.append(element)

print("Pradinis sarasas:", my_list)
print("Teigiami sk.sarasas:", positive_list)
print("Neigiamu sk.sarasas:", negative_list)
print ('=============8 užduotis atlikta===================')
# Sukuriame sąrašą ir atspausdiname vieną jo elementą
my_list = [1, 2, 3, 4, 5]
print("Pirma reikšmė sąraše:", my_list[0])

# Pridedame naują elementą
my_list.append(6)
print("Pridėjome elementą į sąrašą:", my_list)

# Ištriname elementą
my_list.remove(3)
print("Ištrynėme elementą iš sąrašo:", my_list)

# Keičiame elementą
my_list[1] = 10
print("Pakeitėme elementą sąraše:", my_list)

# Sukuriame žodyną ir atspausdiname jo reikšmę
my_dict = {'Jonas': 25, 'Petras': 30, 'Ieva': 27}
print("Jonas turi", my_dict['Jonas'], "metus")

# Ištriname elementą iš žodyno
del my_dict['Petras']
print("Ištrynėme elementą iš žodyno:", my_dict)

#
print('----Code Academy #1 užduotis atlikta---')
# suma = 0
#
# while True:
#     skaicius = int(input("Įveskite skaičių: "))
#
#     if skaicius < 0:
#         break
#     else:
#         suma += skaicius
#         papildomas_skaicius = int(input("Įveskite dar vieną skaičių: "))
#
# print("Visų įvestų teigiamų skaičių suma yra", suma)
#
print('----Code Academy #2 užduotis atlikta---')
# words = []
# count = int(input("Įveskite norimą žodžių kiekį: "))
#
# for i in range(count):
#     word = input(f"Įveskite {i + 1}-ąjį žodį: ")
#     words.append(word)
#
# for i in range(len(words)):
#     length = len(words[i])
#     print(f"{i + 1}-asis žodis yra {words[i]}, jo ilgis yra {length}.")
#
print('----Code Academy #3 užduotis atlikta---')
import random

while True:
    skaiciai = [random.randint(1, 6) for i in range(3)]
    print("Tavo skaičiai:", skaiciai)
    if 5 in skaiciai:
        print("Pralaimėjai...")
        break
    else:
        print("Laimėjai!")
        break

print('----Code Academy #4 užduotis atlikta---')
year = int(input("Įveskite metus: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "yra keliamieji metai")
else:
    print(year, "yra nekeliamieji metai")

print('----Code Academy #5 užduotis atlikta---')
for year in range(1900, 2101):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, " yra keliamieji metai")
    else:
        print(year, " yra nekeliamieji metai")

print('----Code Academy #6 užduotis atlikta---')

