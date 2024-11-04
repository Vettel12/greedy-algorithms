"""
Гоше стало интересно, можно ли разбить все заработанные им во время игры
в Лампу очки на две части так, чтобы сумма в них была одинаковой.

Формат ввода
В первой строке записано число элементов массива n. Оно не превосходит 10000

Далее в строку записаны n целых неотрицательных чисел, каждое из которых не превосходит 10000

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе — False

Ввод:
4
1 5 7 1

Вывод: True

Ввод:
3
2 10 9

Вывод:
False

"""

# Реализация по времени O(n) и по памяти O(1)

def solution(n, num):
    sum_num = sum(num)
    if sum_num % 2 != 0:
        return False
    else:
        ideal = sum_num/2
        count = 0
        for x in range(n):
            if num[x] < ideal and count < ideal:
                count += num[x]
        return count == ideal
    
def main():
    try:
        n = int(input())
        if n > 100000:
            raise ValueError
        num = list(map(int, input().split()))
        for i in range(n):
            if abs(num[i]) > 10000:
                raise ValueError
        print(solution(n, num))
    except ValueError:
        print("Invalid input")
 
if __name__ == '__main__':
    main()