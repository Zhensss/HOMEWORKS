# 1
# def display_quote():
#     print("""
#         "Don't compare yourself with anyone in this world...
#                   if you do so, you are insulting yourself."
#                                                       Bill Gates""")
# display_quote()


# 2
# def numbers(start, end):
#     if start > end:
#         start, end = end, start
    
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)

# numbers(3, 15)


# 3
# def square(size, symbol, filled):
#     if filled:
#         for i in range(size):
#             print(symbol * size)
#     else:
#         for i in range(size):
#             if i == 0 or i == size - 1:
#                 print(symbol * size)  
#             else:
#                 print(symbol + ' ' * (size - 2) + symbol) 

# square(5, '*', True)  
# print()
# square(5, '#', False) 


# 4
# def minimum(a, b, c, d, e):
#     return min(a, b, c, d, e)

# print("Минимальное число: ", minimum(10, 5, 8, 3, 12))


# 5
# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start
        
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
        
#     return product

# print("Произведение чисел от 5 до 3:", product_in_range(5, 3))



# 6
# def counter(number):
#     amount = list(str(number))
#     return len(amount)

# print(counter(123456))


# 7
# def is_palindrom(number):
#     str_num = str(number)
#     return str_num == str_num[::-1]

# print(is_palindrom(121))  
# print(is_palindrom(-121))  
# print(is_palindrom(12321)) 
# print(is_palindrom(12345))  
