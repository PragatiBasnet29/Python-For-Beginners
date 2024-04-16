x = 5
y = 2
print("----------------------------------------")
print("          Arithmetic Operators          ")
print("----------------------------------------")
print(x + y) #Addition
print(x - y) #Subtraction
print(x * y) #Multiplication
print(x / y) #Division
print(x % y) #Modulus
print(x ** y) #Exponentiation #same as 5*5
print(y ** x) #Exponentiation #same as 2*2*2*2*2
print(x // y) #Floor Division #rounds the result down to the nearest whole number




print("\n----------------------------------------")
print("          Assignment Operators          ")
print("----------------------------------------")
a = 6
print(a)

a+=3 # a = a + 3
print(a) 

a-=2
print(a)

a*=2 # a = a * 2
print(a)


print("\n----------------------------------------")
print("          Comparison Operators          ")
print("----------------------------------------")

p = 4
q = 7
print(p == q)
print(p != q)
print(p > q)
print(p < q)
print(p <= q)
print(p >= q)


print("\n----------------------------------------")
print("          Logical Operators          ")
print("----------------------------------------")

z = 5
print(z < 10 and z > 2)

print("\n----------------------------------------")
print("          Bitwise Operators          ")
print("----------------------------------------")

print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""


print(6 | 3)

"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""






