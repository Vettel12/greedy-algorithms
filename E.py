"""
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Но не всё так просто. Печенья могут быть разного размера. У каждого ребёнка есть фактор
жадности - минимальный размер печенья, которое он возьмёт. Нужно выяснить, сколько
ребят останутся довольными.
Каждый ребёнок может взять не больше одного печенья.
Формат ввода
В первой строке записано n - количество детей.
Во второй - п чисел, разделенных пробелом - фактор жадности для каждого ребенка, целое
число, не превосходящее 1000.
В следующей строке записано - m - количество печенек.
Далее - m чисел, разделенных пробелом - размеры печенек.
Оба числа п и т не превосходят 10000.
Формат вывода
Нужно вывести одно число - количество детей, которые останутся довольными

Ввод
2
1 2
3
1 2 3

Вывод
2

Ввод
3
1 2 3
2
1 1

Вывод
1

"""

# Реализация по времени O(n) и по памяти O(m)

def solution(n, cookies, m, size_cookies):
    count = 0
    set_size_cookies = set(size_cookies)
    for i in range(n):
        if cookies[i] in set_size_cookies:
            count += 1
            set_size_cookies.remove(cookies[i])
    return count

def main():
    try:
        n = int(input())
        if n > 10000:
            raise ValueError
        cookies = list(map(int, input().split()))
        for i in range(n):
            if cookies[i] > 1000:
                raise ValueError
        m = int(input())
        if m > 10000:
            raise ValueError
        size_cookies = list(map(int, input().split()))
        print(solution(n, cookies, m, size_cookies))
    except ValueError:
        print("Ошибка")

if __name__ == '__main__':
    main()