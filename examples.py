# Comments: dette er en kommentar

'''
Multi-
line
comment
'''

# Initialisering af Variable:
myNum = 1
myDouble = 2.87
myString = "Hej!"
myBool = True

# Print til konsolen:
print(myString)

# Operationer (Numbers):
print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 % 2 = ", 5 % 2)
print("5 ** 2 = ", 5 ** 2)

# Operationer (Logisk):
myOtherBool = False
print("myBool and myOtherBool = ", myBool and myOtherBool)
print("myBool or myOtherBool =", myBool or myOtherBool)
print("not myBool = ", not myBool)

# Datastrukturer
# Lists:
myList = [1,2,3]
myList.append(5)
print(myList)
print(len(myList))
myList.remove(5)
print(myList)

# Tuples:
myTuple = (1, 2, 3)
print(myTuple)

# Dictionaries:
myDictionary = {
    "En":1,
    "To":2,
    "Tre":3
}
print('"En" = ', myDictionary.get("En"))

# Control Flow
if myBool:
    print(myBool)
elif myBool or myOtherBool:
    print(True)
else:
    print(False)

i = 0;
while i < 10:
    print(i)
    i = i + 1
    
for j in range(0,10):
    print(j)

# Methods/Functions
def myFunc(arg0, arg1):
    return arg0 + arg1

def myOtherFunc(arg0):
    print(arg0)

    
# Neuralt Netværk fra Aflevering 2:
def h(x,y):
    return [(-x-y > -1.5), (x+y > 0.5)]

def g(x,y):
    return (x+y > 1.5)

def f(x,y):
    return g(h(x,y)[0],h(x,y)[1])

print "f(0,0) = ",f(0,0)

print "f(1,0) = ",f(1,0)

print "f(0,1) = ",f(0,1)

print "f(1,1) = ",f(1,1)
    
# Class
class myClass:
    
    def __init__(self, arg0, arg1):
        self.attr0 = arg0
        self.attr1 = arg1
    
    def classFunc(self):
        print(self.attr0)

# Object
obj = myClass("Some text", 78)
obj.classFunc()

# Input
myInput = raw_input("Input:")
print(myInput)

# Filhåndtering
f = open('example_test.txt','r+')
for line in f:
    print(line)
f.close()
