def pivot(list, start_index, end_index):
    swap_index=start_index
    for i in range(start_index+1, end_index):
        if list[i]<list[start_index]:
            swap_index+=1
            list[i], list[swap_index]= list[swap_index], list[i]
    list[start_index], list[swap_index] = list[swap_index], list[start_index]
    return swap_index

def quick_sort_helper(list, start_index, end_index):
    if start_index==end_index:
        return list
    pivot_index=pivot(list, start_index, end_index)
    quick_sort_helper(list, start_index, pivot_index)
    quick_sort_helper(list, pivot_index+1, end_index)

def quick_sort(list):
    return quick_sort_helper(list, 0, len(list))

list=[6,7,3,2,1,0,10,8,9,5,4]
quick_sort(list)
print(list)