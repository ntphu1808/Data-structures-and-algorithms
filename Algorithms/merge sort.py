def merge(leftSide, rightSide):
    combination=[]
    i=0
    j=0
    while i<len(leftSide) and j<len(rightSide):
        if leftSide[i] < rightSide[j]:
            combination.append(leftSide[i])
            i+=1
        else:
            combination.append(rightSide[j])
            j+=1
    while i<len(leftSide):
        combination.append(leftSide[i])
        i+=1
    while j<len(rightSide):
        combination.append(rightSide[j])
        j+=1
    return combination

def merge_sort(list):
    if len(list) == 1:
        return list
    leftSide=list[:len(list)//2]
    rightSide=list[len(list)//2:]
    return merge(merge_sort(leftSide), merge_sort(rightSide))

list=[1, 3, 7, 8, 2, 4, 5]
print(merge_sort(list))