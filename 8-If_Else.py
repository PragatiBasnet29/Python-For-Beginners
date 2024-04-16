# if
a = 56
b = 450

if b > a:
    print("b is greater than a\n")

# elif, else
x = 45
y = 45

if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x\n")


#and
p = 200
q = 44
r = 600

if p > q and p < r:
    print("Both conditions are True\n")


#nested if

s = 44

if x > 10:
    print("Above 10!")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20!")
else:
    print("Below 10!")