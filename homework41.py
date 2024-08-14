# 1
# inp = input('Введите операцию: ')

# listOps = ['+', '-', '/', '*']
# counter = 0

# for i in range(5):
#     spl1 = inp.split(listOps[i])
#     if len(spl1)>1:
#         print(spl1)
#         break
#     else:
#         counter+=1
                
# if counter == 0:
#     print(int(spl1[0]) + int(spl1[1]))
# elif counter == 1:
#     print(int(spl1[0]) - int(spl1[1]))
# elif counter == 2:
#     print(int(spl1[0]) / int(spl1[1]))
# elif counter == 3:
#     print(int(spl1[0]) * int(spl1[1]))
# else:
#     print('Error')    



# 2
# import random

# n = 20
# random_list = [random.randint(-10, 10) for _ in range(n)]

# # min_element = float('inf')
# # max_element = float('-inf')
# min_element = 0
# max_element = 0
# count_negatives = 0
# count_positives = 0
# count_zeros = 0

# for number in random_list:
#     if number < 0:
#         count_negatives += 1
#     elif number > 0:
#         count_positives += 1
#     else:
#         count_zeros += 1
    
#     if number < min_element:
#         min_element = number
#     if number > max_element:
#         max_element = number

# print("Список случайных чисел:", random_list)
# print("Минимальный элемент:", min_element)
# print("Максимальный элемент:", max_element)
# print("Количество отрицательных элементов:", count_negatives)
# print("Количество положительных элементов:", count_positives)
# print("Количество нулей:", count_zeros)
