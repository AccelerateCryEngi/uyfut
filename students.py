with open('students.csv', encoding='utf-8') as infile:
    a = infile.readlines()
a.pop(0)
for i in range(len(a)):
    a[i] = a[i].strip().split(',')
    note = a[i]
    if 'Хадаров Владимир' in note[1]:
        print('Ты получил: %s, за проект - %s' % (note[4], note[2]))
d = {}
for note in a:
    if note[4] != 'None':
        if note[3] in d:
            d[note[3]][0] += 1
            d[note[3]][1] += int(note[4])
        else:
            d[note[3]] = [1, int(note[4])]
for note in d:
    d[note] = round(d[note][1]/d[note][0], 3)
for i in range(len(a)):
    if a[i][4] == 'None':
        a[i][4] = d[a[i][3]]

f = open('student_new.csv', 'w', encoding='utf-8')
f.writelines('id,Name,titleProject_id,class,score\n')
for x in a:
    f.writelines(','.join(map(str, x))+'\n')
f.close()
