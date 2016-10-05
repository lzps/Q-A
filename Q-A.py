#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 存在utf8显示问题

import os, random

t = os.listdir(os.path.split(os.path.realpath(__file__))[0])
f, j, csv = [], 0, []
for i in t:
    if '.csv' in i:
        j = j + 1
        f.append(i)
        print(str(j) + ' --> ' + i[0:-4])
with open(f[int(input('\n 请选择: ')) - 1], 'rb') as f:
    exec(f.read())

headers = csv.pop(0).split('|')
for i, j in enumerate(headers):
    print(str(i) + ' -- ' + j + '（例如：' + csv[0].split('|')[i] + '）')
Q = exec(input('请选择提供什么信息（即已知、输出）' + '\n  可多选，以","分隔 : '))
A = exec(input('请接着选择求什么（即输入）' + '\n  可多选，以"|"分隔 : '))

print('\n1.做选择题' + '\n2.做填空题')
t = input(' 请选择: ') # 如果不选2来做填空题，就是选1
out = 0 if t == '2' else int(input('\n输出几个选项？\n 请输入：'.format(len(csv))))-1

while True:
    random.shuffle(csv)
    for f in csv:
        if os.system('cls'):
            t = os.system('clear')

        doing = f.split('|')
        question, known, rightA = [], [], []
        for i in Q:
            known.append(headers[i] + '：' + doing[i])
        for i in A:
            question.append(headers[i])
            rightA.append(str(doing[i]))
        print('已知：\n' + '  ' + '，'.join(known) + '\n则 ' + '或'.join(question) + '为：')
        if not out:
            answer = input('请输入：')
        else:
            csv2, answer = list(csv), []
            random.shuffle(csv2)
            csv2.remove(f)
            csv2.insert(random.randint(0, out), f)
            for i, j in enumerate(csv2):
                if i > out:
                    break
                for k, l in enumerate(j.split('|')):
                    if k in A:
                        answer.append(l)
            for i, j in enumerate(answer):
                print(str(i) + ' --> ' + str(j))
            answer = answer[int(input('请输入：'))]

        print('The Right Answer:  ' + 'or'.join(rightA))
        if answer in rightA:
            print('Congratulations, You\'re right!')
        input('Press Enter to continue . . .')
