def pin_generator(pin):
    for i in range(10000):
        current_pin = str(i).zfill(4)
        if current_pin == pin:
            yield current_pin
            break
        else:
            yield current_pin
PIN = '0549'
gen = pin_generator(PIN)
for p in gen:
    print(p)
print(f"PIN is {PIN}")
