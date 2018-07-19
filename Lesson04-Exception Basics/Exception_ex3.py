import math

'''
def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        if j==0:
            continue
        div(i, j)
'''
'''
try:
    print(a[100])
    num = x
except NameError as e:
    print("I'm in NameError! ")
    print(e)
except IndexError as e:
    print("I'm in IndexError!" )
    print(e)
else:
    print("I'm in else!")
'''
'''
try:
    print("hello!")
    x = gggggg
except Exception as e:
    print(type(e))
    print(e)
else:
    print("In else")
finally:
    print("I'm in finally!")
'''

def sqrt(number):
    if number <= 0 :
        raise ValueError("Number can't be zero!")
    else:return math.sqrt(number)

try:
    print(sqrt(81))
    sqrt(0)
except Exception as e:
    print(type(e))
    print(e)
'''
num = 100
sqrt(num)
print(sqrt(num))
sqrt(0)
'''