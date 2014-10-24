import random
import re

mqffn = 'mqf'

FIRST_QUESTION = 1
TOTAL_QUESTIONS = 106
TEST_QUESTIONS = 25

questions = {}

def read_file():
    data = []
    f = open(mqffn, 'r+')

    if not f:
        print 'error opening file', mqffn
    else:

        for line in f:
            data.append(line)

    return data


qs = []

for x in range(TEST_QUESTIONS):
    new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)
    
    while new in qs:
        new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)

    qs.append(new)

qs.sort()

print qs

data = read_file()

for line in data:
    print line


q_start = re.compile('(\d?\d?\d\.)')

split_data = q_start.split(''.join(data))

print 'SPLIT:'
for x in range(len(split_data)):
    print 'INDEX:', x, 'TEXT:', split_data[x]

    # split_data[x] = split_data[x].strip()

    if q_start.match(split_data[x]):
        questions[int(split_data[x].strip('.'))] = split_data[x + 1]

keys = questions.keys()
keys.sort()

print 'BY KEY:'
for key in keys:
    print key, questions[key]

print 'KEYS:', len(questions.keys())

print split_data
print 'Length:', len(split_data)
print 'END'