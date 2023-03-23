list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

list3 = []

for i in range(len(list1)):
    if (i+1) % 2 == 0:
        list3.append(list2[i//2])
    else:
        list3.append(list1[i])
print('Rezultatas čia:', list3)
print('-----Užduotis #1 atlikta--------')
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print('Sujungtas sąrašas',list1)
print('-----Užduotis #2 atlikta--------')
sarasas1 = [1, 2, 3, 4]
sarasas2 = [5, 6, 7, 8, 9]

sarasas2.insert(3, sarasas1)

print(sarasas2)

print('-----Užduotis #3 atlikta--------')
# element_count = int(input("Įveskite elementų skaičių: "))
#
# if element_count <= 0:
#     print("Elementų skaičius turi būti didesnis už 0!")
#     exit()
#
# sarasas = []
# for i in range(element_count):
#     elementas = input(f"Įveskite {i+1}-ąjį elementą: ")
#     sarasas.append(elementas)
#
# print("Sąrašas:", sarasas)

print('-----Užduotis #4 atlikta--------')
# numbers = []
# n = int(input("Įveskite, kiek skaičių norite įvesti: "))
# while n <= 0:
#     n = int(input("Įveskite teigiamą skaičių: "))
# for i in range(n):
#     number = int(input("Įveskite skaičių: "))
#     if number > 0:
#         numbers.append(number)
# print("Teigiami skaičiai:", numbers)
print('-----Užduotis #5 atlikta--------')
sarasas = []
while True:
    ilgis = int(input("Įveskite sąrašo ilgį: "))
    if ilgis < 1:
        print("Įvestas neteisingas skaičius, įveskite teigiamą skaičių")
    else:
        break

while len(sarasas) < ilgis:
    elementas = input(f"Įveskite {len(sarasas)+1}-ąjį elementą: ")
    sarasas.append(elementas)
print("Sąrašas:", sarasas)

print('-----Užduotis #5-1 atlikta--------')