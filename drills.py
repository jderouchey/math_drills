#!/usr/bin/env python3

"""drill.py: Simple math drills."""

__author__ = "Joel DeRouchey"
__copyright__ = "No Copyright 2017, Reno, Nevada"

import random
import datetime

count = 1
correct = 0
questions = [0] * 145
equations = [None] * 145

for x1 in range(1, 13):
    for x2 in range(x1, 13):
        answer = x1 * x2
        questions[count] = answer
        equations[count] = f'{x1} * {x2} = '
        count += 1

rq = random.sample(range(1, 79), 78)

then = datetime.datetime.now()
for q in rq:
    estimation = int(input(equations[q]))
    if estimation == questions[q]:
        print('Correct')
        correct += 1
    else:
        print('Incorrect')
now = datetime.datetime.now()
duration = now - then
print(f'You have answered {correct} out of 78 in {duration}')
print(f'Accuracy: {correct / 78:.2%}')
print(f'Speed: {duration.total_seconds() / 78:.2f} seconds per question')

with open('math.log', 'a') as f:
    st = datetime.datetime.now().strftime('%Y-%m-%d,%H:%M:%S')
    f.write(f'{st},{correct / 78},{duration.total_seconds() / 78}\n')
