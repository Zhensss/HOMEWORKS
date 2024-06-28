# 1
# def palindrom(phrase):
#     rev_phrase = phrase[::-1]
#     if rev_phrase==phrase:
#         print('YES!')
#     else:
#         print('NO')
        
        
# palindrom('asa')
# palindrom('asa1')



# 2
# text = input('Введите текст: ')
# slova = input('Введите слова через пробел: ')

# li_of_text = text.split(' ')
# li_of_slova = slova.split(' ')
# print(li_of_text)
# print(li_of_slova)

# for i in range(len(li_of_text)):
#     for t in range(len(li_of_slova)):
#         if li_of_text[i]==li_of_slova[t] or li_of_text[i]==(li_of_slova[t] + ','):
#             # li_of_text[i].upper()
#             li_of_text[i] = li_of_text[i].upper()
            
# text =  ' '.join(li_of_text)
# print(text)



# 3
# text = input('Введите текст: ')

# text2 = text.split('.')
# if text2[-1]=='':
#     del(text2[-1])
# print(len(text2))