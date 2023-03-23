
#a = int (5)

#print (type('a'))

#b = float(15.5)
#print(type('b'))

#print (a)
#print (b)

#suma = 5+2
#print(suma)

#suma1 = 5/4
#print(suma1)

# Padidina raides
my_string = "labas rytas!"

# Convert the string to all uppercase using the upper() method
my_string_uppercase = my_string.upper()

# Print the original string and the uppercase version
print("Original string:", my_string)
print("Uppercase string:", my_string_uppercase)

# Example string
my_string = "Laba Diena!"

# Convert the string to all lowercase using the lower() method
my_string_lowercase = my_string.lower()

# Print the original string and the lowercase version
print("Original string:", my_string)
print("Lowercase string:", my_string_lowercase)

# Example string
my_string = "labas vakaras"

# Capitalize the first letter of the string using the capitalize() method
my_string_capitalized = my_string.capitalize()

# Print the original string and the capitalized version
print("Original string:", my_string)
print("Capitalized string:", my_string_capitalized)

# Example string
my_string = "graži diena"

# Convert the string to title case using the title() method
my_string_titlecase = my_string.title()

# Print the original string and the title case version
print("Original string:", my_string)
print("Title case string:", my_string_titlecase)


my_string = "programuoti išmoksi programuojant"

# Find the index of the letter "š" using the index() method
š_index = my_string.index("š")

# Print the index of the letter "š"
print("The index of the letter 'š' is:", š_index)


my_string = "gyvenimas yra gražus"

ž_index = my_string.find("ž")

# Print the index of the letter "ž"
print("The index of the letter 'ž' is:", ž_index)

# Example string
text = "Gyveno kartą senelis ir senelė"

# Replace the substring "senelis" with "Antanas" using the replace() method
new_text = text.replace("senelis", "Antanas")

# Print the original string and the new string with the replaced substring
print("Original string:", text)
print("New string with replaced substring:", new_text)

# Example string
text = "   Gyveno   "

# Remove whitespace from the beginning and end of the string using the strip() method
new_text = text.strip()

# Print the original string and the new string with whitespace removed
print("Original string:", text)
print("New string with whitespace removed:", new_text)
print("========================================================")

# Pirmoji#1 2023-03-07 užduotis
# vardas = input('Koks jūsų vardas?').title()
# pavarde = input('Kokia jūsų pavardė?').title()
# gimimas=input('Įvestkite gigimo metus')
# miestas=input('Kokiame mieste gyvenate?').title()
# age = str (2023 - int(gimimas))
# print("===================REZULTATAS====================")
# print(vardas.upper(),pavarde.lower(), 'dabar esate',age,'metų')

print("========================================================")
# Antroji#2 Užduotis
sentence = "Obuolys ir kriaušė yra vaisiai"

# Find the index of the substring "kr" in the sentence
index = sentence.find("kr")

# Check if the substring was found
if index != -1:
    print("The substring 'kr' was found at index", index)
else:
    print("The substring 'kr' was not found in the sentence.")
print("========================================================")

# Define the sentence
sentence = "Obuolys ir kriaušė yra vaisiai"

# Initialize variables to store the counts
# upper_count = 0
# lower_count = 0
#
# Loop over each character in the sentence
# for char in sentence:
#  Check if the character is an uppercase letter
    # if char.isupper():
    #     upper_count += 1
    # Check if the character is a lowercase letter
    # elif char.islower():
    #     lower_count += 1
#
# print('===================Suskaičiuota=====================')
# print(sentence,f"sakinyje yra {upper_count} didžiosios raidė(-s) ir {lower_count} mažosios raidės")
# print('===================Suskaičiuoti kiek yra žodžių=====================')
# sentence = "Kaip gražu miške, oj gražu, oj gražu"
# word = input("Enter a word from the sentence: ")
# count = sentence.count(word)
#
# print("Original sentence: ", sentence)
# print("Number of times the word appears: ", count)

print("=====================Teksto atvaidavimas===============")
tekstas = "Code Academy"

print(tekstas[:8])
print(tekstas[5:10])
print(tekstas[5:1])
print(tekstas[::-1])
print("============Number tipo kintamieji===================")

import math
a=6
print(math.sin(a))
print("============Užduotis 4 Diena 03/07===================")
import re
text = 'Dažno Studento mokslo metai susiDEda iš 7 mėnESių poilsio ir 2 bemiEgių mėnesių sesijos'

# Change the case of the first letter of each word
text = ' '.join(word.capitalize() for word in text.split())

# Print the modified text and the number of words
print('Modified Text: ', text)
print('Number of Words: ', len(re.findall(r'\b\w+\b', text)))

print("============Užduotis 5 Diena 03/07===================")

tekstas = "Jau saulelė vėl atkopdama budino svietą"
# word = input("Ko tekste ieškoti? ")
# count = tekstas.count(word)

text_to_insert = "Kaip gražu miške, oj gražu, oj gražu"

# new_sentence = sentence + " " + text_to_insert if count > 0 else sentence

# print("Original sentence: ", sentence)
# print("Number of times the word appears: ", count)
# print("New sentence: ", new_sentence)

print("============Užduotis 6 Diena 03/07===================")
# import math
# a=17
# print(math.isqrt(a))
# print("============Užduotis 6-1 Diena 03/07===================")
# import math
#
# sk = int(input('Įvestite norimą sk. kv.šakniai ištraukti:' ))
# root = (math.isqrt(sk))
# print(f"Šaknis iš skaičiaus {sk} yra {root}.")
print("============Užduotis 7 Diena 03/07===================")

# import math
#
# num1 = float(input("Įveskite pirmą nr: "))
# num2 = float(input("Įveskite sekantį nr.: "))
#
# Calculate product
# product = num1 * num2
# print(f"Skaičiaus {num1} ir {num2} yra {product:.2f}.")
#
# Calculate integer power
# power = int(num1 ** num2)
# print(f"{num1} pakeltas {num2} yra {power}.")
#
# Calculate rounded division
# rounded_division = math.ceil(num1 / num2)
# print(f"Skaičiaus {num1} padalintas iš  {num2} = {rounded_division}.")
#
# Calculate remainder
# remainder = num2 % num1
# print(f"Skaičiaus {num2} dalyba iš {num1} yra {remainder}.")
#
# Calculate integer part of root
# root_int = int(num2 ** (1/num1))
# print(f"Iš skaičiaus {num2} traukiant laipsnio šaknį 1/{num1} svveikoji dalis yra {root_int}.")

print("============8 užduotis===================")
# text = "5 5 9 3 12 78 9 6 2"
#
# split text into a list
# text_list = text.split()
#
# ask user for index of list item
# index = int(input("Kelintą sąrašo elementą išsirinkti? "))
#
# get the list item at the specified index
# selected_item = text_list[index]

# calculate the square of the selected item
# square = int(selected_item) ** 2

# display the list, the selected item and its square
# print("Sąrašas:", text_list)
# print(f"Kelintas sąrašo elementą išsirinkti? {index}")
# print(f" {index} Sąrašo elementas yra {selected_item}. Jo kvadratas {square}")

print("============ Diena 03/08===================")

tekstas = ('Metai tUri dvylika menesiu')
print(tekstas.upper().isupper())