from task_lists import comparison
import pytest

@pytest.mark.parametrize(
    'list_1, list_2, expected',
    [
        ('', '', [['', '- не поменял позицию']]),
        ('A, A, B, B', 'B, A, B, A', [['A', '- сдвинулся на: 1'], ['A', '- сдвинулся на: 2'], 
                        ['B', '- не поменял позицию'], ['B', '- сдвинулся на: -3']]),
        ('#, @, $', '#, $, $', [['#', '- не поменял позицию'], ['@', '- этот элемент был удален'], 
                                    ['$', '- не поменял позицию'], ['$', '- добавлен с новым индексом: 1']]),
        ('1, 4, 5, 0', '2, 0, 5, 1, -100', [['1', '- сдвинулся на: 3'], ['4', '- этот элемент был удален'], 
                                    ['5', '- не поменял позицию'], ['0', '- сдвинулся на: -2'], 
                                    ['2', '- добавлен с новым индексом: 0'], ['-100', '- добавлен с новым индексом: 4']]),
        ('A, B, C, D, E, F, G, H, I, J, K, L, M, N', 'B, C, D, A, F, E, Z, M, N, J, K, L', [['A', '- сдвинулся на: 3'], ['B', '- сдвинулся на: -1'], 
                        ['C', '- сдвинулся на: -1'], ['D', '- сдвинулся на: -1'], 
                        ['E', '- сдвинулся на: 1'], ['F', '- сдвинулся на: -1'], 
                        ['G', '- этот элемент был удален'], ['H', '- этот элемент был удален'], 
                        ['I', '- этот элемент был удален'], ['J', '- не поменял позицию'], 
                        ['K', '- не поменял позицию'], ['L', '- не поменял позицию'], 
                        ['M', '- сдвинулся на: -5'], ['N', '- сдвинулся на: -5'], 
                        ['Z', '- добавлен с новым индексом: 6']])
    ]
)

def test_all(list_1, list_2, expected):
    assert comparison(list_1, list_2) == expected

