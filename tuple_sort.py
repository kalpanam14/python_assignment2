# Creating and Print list
tupList =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List of Tuple before sorting : " + str(tupList))

# Sorting List of Tuples in Increasing order by last element
listLen = len(tupList);
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(tupList[j][-1] > tupList[j + 1][-1]):
            swap = tupList[j]
            tupList[j] = tupList[j + 1]
            tupList[j + 1] = swap

#Printing Sorted List
print("List of Tuple after sorting : " + str(tupList))