#!/usr/bin/env python

"""drill.py: Simple math drills."""

__author__ = "Joel DeRouchey"
__copyright__ = "No Copyright 2017, Reno, Nevada"

import random
import datetime, time

count = 1
correct = 0
questions = list(xrange(145))
equations = list(xrange(145))

for x1 in xrange(1, 13 ):
    for x2 in xrange(x1, 13):
        answer = x1 * x2
        questions[count] = answer
        equations[count] = str(x1) + ' * ' + str(x2) + ' = '
#        print ('%i.  %i * %i = %i' % (count, x1, x2, questions[count]))
        count += 1



rq = random.sample(xrange(1, 79), 78)

# rq = random questions
then = datetime.datetime.now()
for q in rq:
    estimation = input(equations[q] + ' ')
    if estimation == questions[q]:
        print 'Correct'
        correct += 1
    else:
        print 'Incorrect'
now = datetime.datetime.now()
duration = now - then
print 'You have answered ' + str(correct) + ' out of 78' + ' in ' + str(duration)
print 'Accuracy :' + str(correct/float(78)) 
print 'Speed is :' + str(duration.seconds/float(78))

f = open('math.log', 'a')
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d,%H:%M:%S')
f.write(st)
f.write(',' + str(correct/float(78))) 
f.write(',' + str(duration.seconds/float(78)))
