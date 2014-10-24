import random

FIRST_QUESTION = 1
TOTAL_QUESTIONS = 106
TEST_QUESTIONS = 25

qs = []

for x in range(TEST_QUESTIONS):
    new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)
    
    while new in qs:
        new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)

    qs.append(new)

qs.sort()

print qs


def get_q(q):
    for x in q:
        yield q.pop(0)

# print get_q(qs)
