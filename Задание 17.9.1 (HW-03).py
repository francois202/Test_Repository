def sort_list(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

try:
    print("Введите последовательность чисел через пробел: ")
    lst = list(map(int, input().split()))
    print(lst)
    lst = sort_list(lst)
    print(lst)
    
except ValueError:
    print("Некорректный ввод последовательности чисел.")