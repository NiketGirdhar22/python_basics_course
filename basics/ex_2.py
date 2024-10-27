myInt = 1
myFloat = 3.2
myStr = "Niket"
myBool = True
myList = [0,1,"NT",9,False]
myTuple = (0,1,2)
myDict = {"one":1, "two":2}

print("Integer: ",myInt)
print("Float: ",myFloat)
print("String: ",myStr)
print("Boolean: ",myBool)
print("List: ",myList)
print("Tuple: ",myTuple)
print("Dictionary: ",myDict)

myInt = "abc"
print("Updated Integer variable: ",myInt)

print("myList[2]: ",myList[2])
print("myTuple[1]: ",myTuple[1])
print("myList[1:5]: ",myList[1:5])
print("myList[1:5:2]: ",myList[1:5:2])
print("myList[::-1]: ",myList[::-1])

print('myDict["one"]: ',myDict["one"])

print("String" + str(123))

def someFunction():
    global myStr
    myStr = "def"
    print(myStr)

someFunction()
print(myStr)

del myStr
print(myStr)