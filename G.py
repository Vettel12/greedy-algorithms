"""
Волшебная фея отправила Гоше послание. Чтобы никто не смог перехватить сообщение, фея
его закодировала. Послание записано в матрице по спирали, начиная с левого верхнего угла
вправо. Помогите Гоше прочитать сообщение.
Формат ввода
В первой строке записано число п - количество строк матрицы
Во второй - m - количество столбцов
В следующих и строках записано по n чисел
Формат вывода
Нужно вывести на печать по спирали элементы матрицы: начиная с левого верхнего угла
вправо.

Ввод
3
4
1 2 3 4
5 6 7 8
9 10 11 12

Вывод
1
2
3
4
8
12
11
10
9
5
6
7

Ввод
5
3
-4 3 7
9 1 -3
-7 -8 6
-3 -1 -5
6 2 2

Вывод
-4
3
7
-3
6
-5
2
2
6
-3
-7
9
1
-8
-1
"""

def solution(n, m, matrix):
    result = []
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
                
    return '\n'.join(map(str, result))


def main():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        row = list(map(str, input().split()))
        matrix.append(row)
    print(solution(n, m, matrix))

if __name__ == '__main__':
    main()