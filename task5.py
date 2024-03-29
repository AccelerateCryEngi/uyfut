with open('students.csv', encoding='utf-8') as f:
    a = f.readlines()
title = a.pop(0)
slovar = {x: y + 1 for y, x in enumerate('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ')}


def hash(string):
    p = 67
    m = 10**9 + 9
    res = []
    for i in range(len(string)):
        res.append(string[0]*p**i%m)
    return res

for i in range(len(a)):
    item = a[i].split(',')
    fio = item[1]
    prehash = [slovar[x] for x in fio]
    hashed = hash(prehash)
    a[i] = [''.join(map(str, hashed))]+a[i].split(',')[1:]

with open('students_with_hash.csv', 'w') as f:
    f.write(title)
    for item in a:
        f.write('\n')
        f.write(','.join(item))