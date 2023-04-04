def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
gen = fibonacci()
print(next(gen))  # išvestų 0
print(next(gen))  # išvestų 1
print(next(gen))  # išvestų 1
print(next(gen))  # išvestų 2
print(next(gen))  # išvestų 3
# ir taip toliau, grąžindamas sekantį Fibonačio sekos skaičių kiekvien
