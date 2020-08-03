# Написать скрипт для сравнения двух списков с указанием что добавилось в список, 
# что ушло, насколько позиций произошло смещение элемента в списке. 
# Порядок элементов важен.
# Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
# Список 2: B, C, D, A, F, E, Z, M, N, J, K, L

#ввод двух списков
list_1 = input().split(', ')
list_2 = input().split(', ')

#функция сравнения
def comparison(list_1, list_2):

    #определение новых элементов списка и их позиций
    new_items = []
    index = 0
    for item in list_2:
        if item not in list_1:
            new_items.append((item, index))
        index += 1

    #определение удаленных элементов из списка
    rm_items = []
    index = 0
    for item in list_1:
        if item not in list_2:
            rm_items.append((item, index))
        index += 1
    
    if len(list_1) > len(list_2):
        list_2 += [0]*(len(list_1) - len(list_2))
    
    index = 0
    for item in list_1:
        if item not in list_2:
            print(item, 'was deleted')
        elif item != list_2[index]:
            new_index = list_2.index(item)
            list_2[new_index] = 0
            print(item, 'has new index', new_index)
        elif item == list_2[index]:
            print(item, 'didnt change position')
        index += 1

        


#точка входа
comparison(list_1, list_2)






