# A lambda function is a small anonymous function.
# Syntax
# lambda arguments : expression

x = lambda a: a + 25
print(x(5))

print("\n")


x = lambda a, b, c : a + b + c
print(x(2, 10, 15))

print("\n")


y = lambda p, r: 2 * p * r
print(y(3.14, 7))