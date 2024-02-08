
with open('1.txt', 'rt', encoding='utf-8') as f_1:
    sum_line = {}
    counting_1 = 0
    for line in f_1.readlines():
        counting_1 += 1
        sum_line['1.txt'] = counting_1
"""print(sum_line)"""

with open('2.txt', 'rt', encoding='utf-8') as f_1:
    counting_2 = 0
    for line in f_1.readlines():
        counting_2 += 1
        sum_line['2.txt'] = counting_2
"""print(sum_line)"""

with open('3.txt', 'rt', encoding='utf-8') as f_1:
    counting_3 = 0
    for line in f_1.readlines():
        counting_3 += 1
        sum_line['3.txt'] = counting_3
sorted_file = {}
while len(sorted_file)!=3:
    for i, j in sum_line.items():
        if sum_line[i] == min(sum_line.values()):
            sorted_file[j] = i
            sum_line[i] = 999
print(sorted_file)

"""запись в один файл"""
a = ''
for key, volume in sorted_file.items():
    #print(sorted_file[i])
    with open(sorted_file[key], 'rt', encoding='utf-8') as f_1:
        with open('all_text.txt','a',encoding='utf-8') as f:
            f.write(volume+'\n')
            f.write(str(key)+'\n')
            #print(f_1.read())
            for line in f_1.readlines():
                #print(line)
                f.write(line)
            f.write('\n')
with open('all_text.txt', 'rt', encoding='utf-8') as f:
    print(f.read())



        #f = open('all_text.txt','rt',encoding='utf-8')
        #print(f.read())
"""print(sum_line)

with open('2.txt', 'wt', encoding='utf-8') as f_1:
    counting_2 = 0
    for line in f_1.readlines():
        counting_2 += 1
        sum_line['f_2'] = counting_2
print(sum_line)

with open('3.txt', 'rt', encoding='utf-8') as f_1:
    counting_3 = 0
    for line in f_1.readlines():
        counting_3 += 1
        sum_line['f_3'] = counting_3"""



