# Selection sort
# given a list, find the minimum value compared to the current index and place it in the current index

#step 1 - Take the value of the current index location and compare it to all index numbers after to establish the minimum in the index
#step 2 - if the current index location value is not the minimum, swap it with the located minimum

arr = [2,4,2,3,1,5]

# def selection_sort(some_list):
#     for i in range(len(arr)):
#         min_val=arr[0]
#         for j in range(arr[i]+1,len(arr)):
#             if min_val > arr[j]:
#                 min_val = arr[j]
#                 arr[i], arr[j] = arr[j], arr[i]
#             print(arr)
# selection_sort(arr)

# step 1- isolate the first value to compare to the rest of the list (len(arr)-1)
# step 2- find the lowest number of the rest of the list
    # Creat var of lowest_num 
    # start lowest num at arr[i+1]
    # iterate throught the rest of the list
    # use if to compare if lowest_num is lower than the rest of the iterated list
# step 3- comapre step 1 to step 2 to see which is lowest
# step 4- swap if step 2 result is lower than step 1. If not, iterate to the next by starting at step 1....

def selection_sort(some_list):
    for i in range(len(some_list)-1):
        # print(i)
        # lowest_num = some_list[i+1]
        lowest_index = i+1
        for j in range(lowest_index +1,len(some_list)):
            if some_list[lowest_index] > some_list[j]:
                # lowest_num = some_list[j]
                lowest_index= j
        if some_list[lowest_index] < some_list[i]:
            # a,b = b,a
            some_list[i], some_list[lowest_index] = some_list[lowest_index], some_list[i]
            # some_list[lowest_index]= some_list[i]
            # some_list[i]= lowest_num
    return some_list

print(selection_sort(arr))

# for i in range(len(A)):
#     # Find the minimum element in remaining 
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
#     # Swap the found minimum element with 
#     # the first element        
#     A[i], A[min_idx] = A[min_idx], A[i]
