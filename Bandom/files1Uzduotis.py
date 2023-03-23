from datetime import datetime

# Sukuriame failą "Tekstas.txt" su gauto kodo tekstų
with open("Tekstas.txt", "w") as f:
    f.write("""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")

# Atspausdiname tekstą iš failo
with open("Tekstas.txt", "r") as f:
    print(f.read())

# Pridedame šiandienos datą ir laiką prie failo pabaigos
with open("Tekstas.txt", "a") as f:
    f.write("\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))

# Sunumeruojame teksto eilutes
with open("Tekstas.txt", "r") as f:
    lines = f.readlines()
    lines_with_numbers = [f"{i}. {line}" for i, line in enumerate(lines, 1)]

with open("Tekstas.txt", "w") as f:
    f.writelines(lines_with_numbers)

# Pakeičiame eilutę "Beautiful is better than ugly." į "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", "r") as f:
    lines = f.readlines()
    updated_lines = [line.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.") for line in lines]

with open("Tekstas.txt", "w") as f:
    f.writelines(updated_lines)

# Atspausdiname visą failo tekstą atbulai
with open("Tekstas.txt", "r") as f:
    text = f.read()
    print(text[::-1])

# Skaičiuojame, kiek yra žodžių, skaičių, didžiųjų ir mažųjų raidžių tekste
with open("Tekstas.txt", "r") as f:
    text = f.read()
    words = len(text.split())
    digits = sum(c.isdigit() for c in text)
    uppercase = sum(c.isupper() for c in text)
    lowercase = sum(c.islower() for c in text)
    print(f"Žodžių: {words}\nSkaičių: {digits}\nDidžiųjų raidžių: {uppercase}\nMažųjų raidžių: {lowercase}")

# Nukopijuojame tekstą į naują failą tik DIDŽIOSIOMIS RAIDĖMIS
with open("Tekstas.txt", "r") as f1, open("DIDZIOSIOMIS.txt", "w") as f2:
    text = f1.read()
    uppercase_text = text.upper()
    f2.write(uppercase_text)

