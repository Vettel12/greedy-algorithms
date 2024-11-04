"""
Вася любит играть в игру Подпоследовательность. Даны 2 строки, и нужно понять, является ли
первая из них подпоследовательностью второй. Когда строки достаточно длинные, иногда
очень трудно получить ответ на этот вопрос, просто посмотрев на них. Помогите Васе,
напишите функцию, которая решает эту задачу.
Формат ввода
В первой строке записана строка s.
Во второй - строка t.
Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000.
Формат вывода
Выведите True, если s является подпоследовательностью t, иначе - False.

Ввод
abc
ahbgdcu

Вывод
True

Ввод
abcp
ahpc

Вывод
False


# Реализация по времени O(n+m) и по памяти O(n+m)

def solution(s, t):
    sl1 = {}
    sl2 = {}
    for i in s:
        if i not in sl1:
            sl1[i] = 1
        else:
            sl1[i] += 1
    for j in t:
        if j not in sl2 and j in sl1:
            sl2[j] = 1
        elif j in sl2 and j in sl1:
            sl2[j] += 1
    if sl1 == sl2:
        return True
    else:
        return False


"""

# Реализация по времени O(n) и по памяти O(1)

def solution(s, t):
    count = 0
    for x in t:
        if count < len(s) and x == s[count]:
            count += 1
    return count == len(s)

def main():
    try:
        s = input()
        if len(s) > 150000:
            raise ValueError
        t = input()
        if len(t) > 150000:
            raise ValueError
        print(solution(s, t))
    except ValueError:
        print("Invalid input")

if __name__ == '__main__':
    main()