"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

string = input("Введите слова через пробел: ").split(" ")
counter = 0
while counter < len(string):
    for i in string:
        if len(i) < 10:
            counter +=1
            print(counter, "-", i)
        else:
            counter +=1
            cut_word = i[:10]
            print(counter, "-", cut_word)
