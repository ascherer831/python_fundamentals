# my_list= [14,9,6,5,11,3,1,12,8,7,13,2,4,10]

# def bubble_swap(num_list):
#     for i in range(len(num_list)):
#         if i == len(num_list )-1:
#             continue
#         elif num_list[i] > num_list[i+1]:
#             num_list[i], num_list[i+1] =  num_list[i+1], num_list[i]
#             for i in range(len(num_list)):
#                 if i == len(num_list )-1:
#                     continue
#                 elif num_list[i] > num_list[i+1]:
#                     num_list[i], num_list[i+1] =  num_list[i+1], num_list[i]
#                     for i in range(len(num_list)):
#                         if i == len(num_list )-1:
#                             continue
#                         elif num_list[i] > num_list[i+1]:
#                             num_list[i], num_list[i+1] =  num_list[i+1], num_list[i]
#     return num_list

# print(bubble_swap(my_list))

my_list= [14,9,6,5,11,3,1,12,8,7,13,2,4,10]

def bubble_swap(num_list):
    for j in range(len(num_list)-1):
        for i in range(len(num_list)-1-j):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] =  num_list[i+1], num_list[i]
    return num_list

print(bubble_swap(my_list))