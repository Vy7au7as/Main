print('x\ty')
for x in range(1,10):
    y = x**2
print(str(x) + '\t' + str(y))
print("============ Diena 03/08===================")
print('x\ty\n--\t--')
for x in range(1,10):
    y = x**2

print(str(x) + '\t' + str(y))
print("============ Diena 03/08===================")
import math
print('x\ty\n--\t--')
for x in range(1,10):
    y = math.sqrt(x)
print(str(x) + '\t' + str(y))
print("============ Diena 03/08===================")
s = 'Jonas mokosi %s' % 'Python'
print(s)
print("============ Diena 03/08===================")
s = '%s mokosi %s' % ('Asta', 'C++')
print(s)
print("============ Diena 03/08===================")
import math
print('x\ty\n--\t--')
for x in range(1,10):
    y = math.sqrt(x)
print('%s\t%s' % (x, y))
print("============ Diena 03/08===================")
import math
print('x\ty\n--\t--')
for x in range(1,10):
    y = math.sqrt(x)

print('%s\t%s' % (x, y))
print("============ Diena 03/08===================")
x = 35
print('x = %d' % x)
print('x = %+d' % x)
print('x = %+d%%' % x)
print('x = %+6d%%' % x)
print('x = %-6d' % x)
print('x = %06d' % x)
print("============ Diena 03/08===================")
x = 35.3456789
print('x = %d' % x)
print('x = %f' % x)
print('x = %2.4f' % x)
print('x = %+2.4f' % x)
print('x = %06.2f' % x)
print("============ Diena 03/08===================")
x = 1.34e-6
print('x = %f' % x)
print('x = %e' % x)
print('x = %g' % x)
print("============ Diena 03/08===================")
import math
start, stop = 1, 9
print('%s\t%s' % ('x'.center(3), 'y'.center(6)))
print('%s\t%s' % (3*'-', 6*'-'))
for x in range(start, stop+1):
    y = math.sqrt(x)

print('%3d\t%2.4f' % (x, y))

print("============ Diena 03/08===================")
zodis = '   Patefonas   '
print (zodis)
zodis1 = zodis.strip('Pate')
print (zodis1)