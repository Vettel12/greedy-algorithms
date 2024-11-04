"""
Помогите Алле написать код алгоритма для выбора уроков, которые пройдут в классе.
Дано расписание предметов. Нужно составить расписание, в соответствии с которым в классе
можно будет провести как можно больше уроков.
Формат ввода
В первой строке задано число предметов. Оно не превосходит 1000.
Далее для каждого предмета в отдельной строке записано время начала и окончания урока.
Обратите внимание на формат времени. Указываются только значащие цифры.
Формат вывода
Выведите информацию о всех уроках, которые нужно провести в кабинете, в порядке
возрастания времени начала.

Ввод
5
9 10
9.3 10.3
10 11
10.3 11.3
11 12

Вывод
3
9 10
10 11
11 12

Ввод
3
9 10
11 12.25
12.15 13.3

Вывод
2
9.0 10.0
11.0 12.25

Ввод
7
19 19
7 14
12 14
8 22
22 23
5 21
9 23

Вывод
3
7.0 14.0
19.0 19.0
22.0 23.0


# Реализация по времени O(n^2) и по памяти O(n)

def solution(matrix):
    result = []
    for i in range(len(matrix)-1):
            for j in range(i+1, len(matrix)):
                if matrix[i][1] > matrix[j][1]:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
    result.append(matrix[0])
    k = 0
    for i in range(1, len(matrix)):
        if matrix[i][0] >= matrix[k][1]:
            k = i
            result.append(matrix[i])
    
    return result


"""
# Реализация по времени O(n(logn)) и по памяти O(n)

def solution(matrix):
    result = []
    matrix.sort(key=lambda x: x[1])
    
    last_end = float('-inf')
    
    for interval in matrix:
        if interval[0] >= last_end:
            result.append(interval)
            last_end = interval[1]
    
    return result


def main():
    try:
        n = int(input())
        if n > 1000:
            raise ValueError
        matrix = []
        for x in range(n):
            row = list(map(float, input().split()))
            matrix.append(row)
        result = solution(matrix)
        print(len(result))
        for row in result:
            print(*row)
    except ValueError:
        print("Invalid input")


if __name__ == '__main__':
    main()