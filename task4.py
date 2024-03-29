import string
import random
with open('students.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f.readlines()]
title = a.pop(0)
def create_pass():
    pw = []
    for _ in range(3):
        pw.append(string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)])
    for _ in range(3):
        pw.append(string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase)-1)])
    for _ in range(2):
        pw.append(string.digits[random.randint(0, len(string.digits)-1)])
    random.shuffle(pw)
    return ''.join(pw)
create_pass()

for j in range(len(a)):
    item = a[j]
    f,i,o = item[1].split()
    name = f + '_' + i[0] + o[0]
    a[j].append(name)
    pw = create_pass()
    a[j].append(pw)

with open('students_password.csv', 'w') as f:
    f.write(','.join(title))
    for item in a:
        f.write('\n')
        f.write(','.join(item))
