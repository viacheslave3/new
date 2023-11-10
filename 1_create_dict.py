# Словари

# Создаем англо-русский словарь
# Ключ- слово на английском языке
# Значение - слово на русском языке

english_dict={
    'apple':'яблоко',
    'milk':'молоко',
    'cat':'кот',
    'cat':'котик'
}
russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
# Определение количества элементов в словаре
#       len(название_словаря)

# Обращение к элементу словаря по ключу
#       название_словаря[ключ]

# Обращение к элементу словаря с помощью метода get()
# get() - возвращает значение по ключу, если такой ключ есть в словаре
# в противном случае возвращает None

#вывод элементов словаря с помощью цикла
#for key in название_словаря:print(key)
print(english_dict)
print(len(russian_dict))
print(english_dict['apple'])
print(russian_dict['кошка'])
for item in russian_dict["кошка"]:
    print(item)
word=input("Введите слово: ")
if word in russian_dict:
    print(russian_dict[word])
else:
    print("Такого слова нет")
print(english_dict.get(word))
for key in english_dict:
    print(key)
    print(english_dict[key])
