def bubble_sort(list):
    for i in range(len(list), 0, -1):                           #best case of bubble sort is O(n) when the list is already sorted or nearly sorted
        for j in range(i-1):                                    #then the nested loop just walk through and do not execute anything. In this case
            if list[j]>list[j+1]:                               #the main loop just iterate throughout the list n time. So this is O(n)
                list[j],list[j+1]=list[j+1],list[j]
    return list

def selection_sort(list):
    for i in range(len(list)):
        min_index=i
        for j in range(i+1, len(list)):
            if list[j]<list[min_index]:
                min_index=j
        if min_index==i: continue
        list[min_index], list[i] = list[i], list[min_index]
    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            index=i
            while (list[index]<list[index-1]):
                list[index], list[index-1] = list[index-1], list[index]
                index-=1
                if index == 0:
                    break
    return list






lst=[6,7]
insertion_sort(lst)
print(lst)