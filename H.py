"""
Во сне Гоша долго играл в игру Лампочка. Он то выигрывал, то проигрывал. Ему стало
интересно, сколько максимум партий подряд он получал большее количество очков, чем в
предыдущей.
Формат ввода
В первой строке записано число элементов массива п. Оно не превосходит 100000
Далее в строку записаны чисел, каждое из которых по модулю не превосходит 1000
Формат вывода
Нужно вывести одно число, равное длине наибольшего возрастающего подмассива

Ввод
9
5 6 3 5 7 8 9 1 2

Вывод
5

Ввод
6
10 4 -2 3 -4 2

Вывод
2

Ввод
7
-5 -9 -4 6 -9 8 -2

Вывод
3

"""

# Реализация по времени O(n) и по памяти O(1)

def solution(n, num):
    result = 0
    tmp = 0
    for x in range(n-1):
        if num[x] < num[x+1]:
            tmp += 1
            if tmp > result:
                result = tmp
        else:
            tmp = 0
    if result != 0:
        result += 1
    return result

def main():
    try:
        n = int(input())
        if n > 100000:
            raise ValueError
        num = list(map(int, input().split()))
        for i in range(n):
            if abs(num[i]) > 1000:
                raise ValueError
        print(solution(n, num))
    except ValueError:
        print("Invalid input")
 
if __name__ == '__main__':
    main()