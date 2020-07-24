def take(n,xs):
    return xs[:n]

def drop(n,xs):
    return xs[n:]

def fst(xs):
    return xs[0]

def merge(xs,ys):
    if len(xs) == 0:
        return ys
    elif len(ys) == 0:
        return xs
    elif xs[0] <= ys[0]:
        return [fst(xs)] + merge(drop(1,xs),ys)
    else:
        return [fst(ys)] + merge(xs,drop(1,ys))

def mergeSort(xs):
    if len(xs) == 0:
        return []
    elif (len(xs)) == 1:
        return xs
    else:
        n = len(xs) // 2
        return merge(mergeSort(take(n,xs)), mergeSort(drop(n,xs)))

userList = []
noOfElements = int(input("Enter number of elements : "))
print("Enter the elements")
for i in range(0,noOfElements):
	element = int(input())
	userList.append(element)
print("Given list is ", userList)

sortedList = mergeSort(userList)

print(sortedList)