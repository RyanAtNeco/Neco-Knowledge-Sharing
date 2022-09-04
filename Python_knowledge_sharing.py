# Python
# Installation:
# Python.org -> Download -> tick 'add to path'

# Usage:
# CMD -> command: python

# Run:
# VSCODE => F5
# CMD / Terminal => python file.py




# log
print('hello guys')

# Variable
name = 'ali'
age = 15
isGoodMan = True

# List
stuffs = [
  'car',
  25, 
  {
    'name': 'mmd',
    'age': 12
  },
  [
    12, 'hello'
  ]
]

# Dict
myDict = {
  'name': 'mahdi',
  'age': 28,
  'likes': ['car', 'bitches', 'weed']
}

# print(stuffs)
# print(myDict['likes'][1])



# For
# range(number) -> 0 to number-1
# range(number1, number2) -> (number1) to (number2)-1
# range(number1, number2, steps) -> (number1) to (number2)-1
# for i in range(15):
#   print(i)

# for i in range(2, 15):
#   print(i)

# for i in range(2, 16, 3):
#   print(i)

# for myVariable in myDict:
#   print(myVariable, myDict[myVariable])


# for aliStuffs in stuffs:
#   print(aliStuffs)  

# for i in range(len(stuffs)):
#   print(stuffs[i])

# while(True):
#   print('hi')
  

# Function
def plus(number1:int, number2:int):
  return number1 + number2

print(plus(1, 2))

