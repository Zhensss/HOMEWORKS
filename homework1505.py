# 1
# def sort_list(lst):
#     n = len(lst)

#     average = sum(lst) / n
    
#     if average > 0:
#         end_index = int(2 * n / 3)
#         sorted_part = sorted(lst[:end_index])
#         remaining_part = lst[end_index:]
#     else:
#         end_index = int(n / 3)
#         sorted_part = sorted(lst[:end_index])
#         remaining_part = lst[end_index:]

#     remaining_part.reverse()
    
#     return sorted_part + remaining_part, average



# print(sort_list([3, -1, 4, 1, 5, -9, 2, 6]))
# print(sort_list([3, -1, 4, 1, 5, -9, 2, 6, -5, -11]))


# 2
# def main():
#     grades = []

#     print('Введите 10 оценок студента (от 1 до 12):')
#     for i in range(10):
#         while True:
#             try:
#                 grade = float(input(f'Оценка {i + 1}: '))
#                 if 1 <= grade <= 12:
#                     grades.append(grade)
#                     break
#                 else:
#                     print('Оценка должна быть от 1 до 12. Попробуйте снова.')
#             except ValueError:
#                 print('Некорректный ввод. Пожалуйста, введите число.')

#     while True:
#         print('\nМеню:')
#         print('1. Вывести оценки')
#         print('2. Пересдать экзамен')
#         print('3. Проверить, выходит ли стипендия')
#         print('4. Вывести отсортированный список оценок')
#         print('5. Выход')

#         choice = input('Выберите действие (1-5): ')

#         if choice == '1':
#             print("Оценки студента:", grades)

#         elif choice == '2':
#             index = int(input('Введите номер элемента списка (1-10): ')) - 1
#             if 0 <= index < len(grades):
#                 new_grade = float(input('Введите новую оценку (от 1 до 12): '))
#                 if 1 <= new_grade <= 12:
#                     grades[index] = new_grade
#                     print('Оценка обновлена.')
#                 else:
#                     print('Оценка должна быть от 1 до 12.')
#             else:
#                 print('Некорректный номер элемента.')

#         elif choice == '3':
#             average = sum(grades) / len(grades)
#             if average >= 10.7:
#                 print('Стипендия выходит.')
#             else:
#                 print('Стипендия не выходит.')

#         elif choice == '4':
#             order = input("Выберите порядок сортировки (введите 'возрастанию' или 'убыванию'): ")
#             if order == 'возрастанию':
#                 sorted_grades = sorted(grades)
#             elif order == 'убыванию':
#                 sorted_grades = sorted(grades, reverse=True)
#             else:
#                 print('Некорректный ввод.')
#                 continue
#             print('Отсортированные оценки:', sorted_grades)

#         elif choice == '5':
#             print('Выход из программы.')
#             break

#         else:
#             print('Некорректный выбор. Попробуйте снова.')

# main()



# 3
# def improved_bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False 
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True 
        
#         if not swapped:
#             break



# user_input = input('Введите числа через пробел: ')
# arr = list(map(int, user_input.split()))
    

# print(improved_bubble_sort(arr))

