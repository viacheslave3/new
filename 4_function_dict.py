# Дополнительные полезные функции и методы словарей
# Метод keys() - возвращает список ключей словаря
# Метод values() - возвращает список значений словаря
# Метод items() - возвращает список из пар (кортежи) ключ- значение

#Вывод всех ключей словаря
#for key in название_словаря: print(key)

#Вывод всех значений
#for value in название_словаря.values(): print(value)


#Вывод всех пар «ключ / значение»
#for key,value in название_словаря.items(): print(key,value)


# Метод clear() - полностью очищает словарь (удаляет все пары ключ-значение)
# Метод copy()  - возвращает копию указанного  словаря

# создание нового словаря  из  последовательности key и значениями value. По умолчанию value присваивается значение None.
#название_словаря=dict.fromkeys(['ключ1', 'ключ2','ключ3'],value)

russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely'],
    собака=['dog','psina']
)
print(russian_dict.keys())
print(russian_dict.values())
print(russian_dict.items())
for value in russian_dict.values():
    print(value)
print(russian_dict.copy())
print(russian_dict.clear())
russian_dict=dict.fromkeys(['ключ1', 'ключ2','ключ3'],0)
print(russian_dict)

