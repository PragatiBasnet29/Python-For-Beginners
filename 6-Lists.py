# Lists are used to store multiple items in a single variable.

"""
----------------------------
 Python Collections (Arrays)
-----------------------------
There are four collection data types in the Python programming language:

"List" is a collection which is ordered and changeable. Allows duplicate members.
"Tuple" is a collection which is ordered and unchangeable. Allows duplicate members.
"Set" is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
"Dictionary" is a collection which is ordered** and changeable. No duplicate members.
"""

fruitsList = ["Apple", "Mango", "Banana", "Orange"]
print(fruitsList)

oddNumberList = [1,3,5,7,9]
print(oddNumberList)

boolList = [True, False, False, True]
print(boolList)

print("\n")

# Loop Through a List
for x in fruitsList:
    print(x)
