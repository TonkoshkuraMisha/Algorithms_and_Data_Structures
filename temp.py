objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
print(len(objects))

def count(myList):
    unique = []
    for item in myList:
        if item not in unique:
             unique.append(item)
    #print(unique)
    print(len(unique)+1)

count(objects)