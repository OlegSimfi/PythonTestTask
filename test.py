import re

# #1 Необходимо написать функцию, которая перевернет массив неопределенной длины. Условие - нельзя использовать встроенный метод length.
a = ['a', 'b', 'c']
def reverseArray(array):
    return array[::-1]
print ("#1", reverseArray(a))

# #2 Реализовать функцию которая отфильтрует все буквы в строке, которые встречаются более одного раза (> 1).
def findDoubleChars(string):
    found = ''
    for i in range(len(string)):
        char = string[i]
        if char in found:
            continue
        tail = string[i + 1:]
        if char in tail:
            found = found + char
    return found
print ("#2",findDoubleChars('agcdcgia'))

# #3 Необходимо нормализовать строку убрав все дополнительные символы возле слов
b = "  X >      Y    >"
def normalize(string):
    pattern = '[!"$%&\'*+,\-./:;<=?[\\]^`{|}~\t\n\x0b\x0c\r]+'
    pieces = [re.sub(pattern, '', x).strip() for x in string.split('>')]
    pieces = [x for x in pieces if len(x)]
    return ' > '.join(pieces)
print ("#3",normalize(b))

