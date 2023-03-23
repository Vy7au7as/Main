import datetime

# Šiandienos data ir laikas
print(datetime.datetime.now())

# Tik šiandienos data
print(datetime.date.today())

# Tik laikas
print(datetime.datetime.now().time())
print('Atlikta 1 užduotis')
from datetime import date

# Šiandienos data
print(date.today())
print('Atlikta 2 užduotis')
from datetime import date as data

# Šiandienos data
print(data.today())

print('Atlikta 3 užduotis')