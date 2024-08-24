# 1
# def mult(int_list):
#     product = 1
#     for num in int_list:
#         product *= num  
#     return product  


# print(mult([1, 2, 3, 4])) 
# print(mult([5, 6, 7]))      
# print(mult([-1, 2, -3]))    


# 2
# def minimum(int_list2):
#     default = 9999999999
#     for num in range(len(int_list2)):
#         if int_list2[num] < default:
#             default = int_list2[num]
#     return default

# print(minimum([45, 66, 23, 67, 11, 7, 55]))
        
    
# 3
# def uncomplex(int_list3):
#     primes = 0
#     for n in int_list3:
#         if n <= 1:
#             continue  
#         is_prime = True
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes += 1
#     return primes

# print(uncomplex([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 23]))


# 4
# def deleter(int_list4, numbers):
#     deleted = 0
    
#     while numbers in int_list4:
#         int_list4.remove(numbers)
#         deleted += 1
    
#     return deleted

# print(deleter([1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 5, 6], 6))


# 5
# def combine(list1, list2):
#     combined_list = list1 + list2
#     return combined_list


# print(combine([1, 2, 3], [4, 5, 6]))


# 6
# def powerer(numbers, grad):
#     powered_list = [num ** grad for num in numbers]
#     return powered_list


# print(powerer([1, 2, 3, 4, 5], 3))


        
