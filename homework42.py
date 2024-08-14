# 1
# def palindrom(text):
#     text1 = ''.join(text.split()).lower()
#     return text1 == text1[::-1]

# input1 = "А роза упала на лапу Азора"
# if palindrom(input1):
#     print(f'"{input1}" палиндром')
# else:
#     print(f'"{input1}" не палиндром')
    

# 2

# def toupperwords(text, my_words):
#     words = text.split()
    
#     upper_words = [
#         word.upper() if word in my_words else word for word in words
#     ]
    
#     new_text = ' '.join(upper_words)
#     return new_text

# input_text = 'Пользователь вводит с клавиатуры некоторый текст, после чегопользователь вводит список зарезервированных слов'
# input_words = ['клавиатуры', 'после', 'зарезервированных']

# result_text = toupperwords(input_text, input_words)

# print(result_text)

    
    
# 3
# text = 'Есть некоторый текст. Посчитайте в этом тексте. количество предложений и выведите. на экран полученный результат.'
# res = text.split('.')
# if res[-1]=='':
#     del res[-1]
# print(res)
# print(len(res))

