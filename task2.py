with open('students.csv', encoding='utf-8') as f:
    a = f.readlines()
a.pop(0)
for i in range(len(a)):
    a[i] = a[i].strip().split(',')
    if a[i][-1] == 'None':
        a[i][-1] = 0
    else:
        a[i][-1] = int(a[i][-1])
#     0    1    2
for i in range(1, len(a)):
    value = a[i][-1]
    info = a[i]
    j = i-1
    while j >= 0 and a[j][-1] < value:
        a[j+1],a[j] = a[j], a[j+1]
        j -= 1
    a[j+1] = info

k = 0
print('10 класс:')
for x in a:
    if '10' in x[3]:
        f,i,o = x[1].split()
        name = f'{i[0]}. {f}'
        k += 1
        print(f'{k} место: {name}')
        if k == 3: break
