from statistics import mean, median

# Sukuriame sąrašą iš skaičių nuo 0 iki 50
nums = list(range(51))

# Padauginame visus sąrašo skaičius iš 10 ir atspausdiname
nums_times_10 = [num * 10 for num in nums]
print(nums_times_10)

# Atrinkiname iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdiname
nums_divisible_by_7 = [num for num in nums if num % 7 == 0]
print(nums_divisible_by_7)

# Pakeliame visus sąrašo skaičius kvadratu ir atspausdiname
nums_squared = [num ** 2 for num in nums]
print(nums_squared)

# Atspausdiname sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
print("Suma:", sum(nums_squared))
print("Mažiausias skaičius:", min(nums_squared))
print("Didžiausias skaičius:", max(nums_squared))
print("Vidurkis:", mean(nums_squared))
print("Mediana:", median(nums_squared))

# Surūšiuojame ir atspausdiname kvadratų sąrašą atbulai
nums_squared_reverse = sorted(nums_squared, reverse=True)
print(nums_squared_reverse)
