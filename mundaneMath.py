#Casey Zhu
#Software Carpentry WC3
#mundaneMath.py

#Adds together all even numbers from 0 to 100 (inclusive and exclusive)

inc = 0
exc = 0

for i in range (0, 100):
    if i % 2 == 0:
        exc += i

for i in range(0, 101):
    if i % 2 == 0:
        inc += i
    
print('The sum of the even numbers between 0 and 100 (inclusive) is', inc)
print('The sum of the even numbers between 0 and 100 (exclusive) is', exc)