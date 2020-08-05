# Написать скрипт для сравнения двух списков с указанием что добавилось в список, 
# что ушло, насколько позиций произошло смещение элемента в списке. 
# Порядок элементов важен.
# Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
# Список 2: B, C, D, A, F, E, Z, M, N, J, K, L

#ввод двух списков
list_1 = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N'
list_2 = 'B, C, D, A, F, E, Z, M, N, J, K, L'

#функция сравнения
def comparison(list_1, list_2):
    list_1 = list_1.split(', ')
    list_2 = list_2.split(', ')
    result = []

    #выравниваем второй список по количеству символов если необходимо
    if len(list_1) > len(list_2):
        list_2 += [0]*(len(list_1) - len(list_2))
    
    #анализ удаленных и поменявших позицию элементов
    index = 0
    for item in list_1:
        if item not in list_2:
            result.append([item, '- этот элемент был удален'])
        elif item != list_2[index]:
            new_index = list_2.index(item)
            list_2[new_index] = 0
            result.append([item, '- сдвинулся на: {}'.format(new_index - index)])
        elif item == list_2[index]:
            list_2[index] = 0
            result.append([item, '- не поменял позицию'])
        index += 1
    
    #анализ новых элементов
    index = 0
    for item in list_2:
        if item != 0:
            result.append([item, '- добавлен с новым индексом: {}'.format(index)])
        index += 1
    
    return result

#точка входа
print(comparison(list_1, list_2))
