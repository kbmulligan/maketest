import random
import re
import time

mqffn = 'mqf'

FIRST_QUESTION = 1
TOTAL_QUESTIONS = 106
TEST_QUESTIONS = 25

TIME_DELAY = 0

questions = {}

#### REGEX'S ##########################
q_start = re.compile(r'(\n\d?\d?\d\.  ?)')
q_begin = re.compile(r'(^\d?\d?\d\.)')
q_answer = re.compile(r'(Ans:  ?[A-D])') 
q_ref = re.compile(r'(Ref: .*)')
re_midsentence_newlines = re.compile(r'[a-z] ?\n ?[a-z]')
excess_newlines = re.compile(r'\n\s*\n\n')

def get_test(questions):
    qs = []
    for x in range(questions):
        new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)
        while new in qs:
            new = random.randint(FIRST_QUESTION, TOTAL_QUESTIONS)
        qs.append(new)
    qs.sort()
    return qs

def read_file(fn):
    data = []
    f = open(fn, 'r+')

    if not f:
        print 'error opening file', mqffn
    else:

        for line in f:
            data.append(line)

    return data

def remove_excess_newlines(data):
    match = excess_newlines.subn('\n', data)
    if match[1]:
        print 'NEWLINES REMOVED:', match[1]
    
    return match[0]

def remove(data, expr):
    match = expr.subn(expr.group()[0]+''+expr.group()[-1], data)
    
    if match[1]:
        print 'SUBSTITUTIONS:', match[1]
    
    return match[0]

def split_q_and_a(test_data):
    # print type(test_data) is list, len(test_data)
    split_data = q_start.split(test_data)
    # print type(split_data) is list, len(split_data)
    return split_data

def extract_questions(split_data):
    for x in range(len(split_data)):
        split_data[x] = split_data[x].strip()
        if q_begin.match(split_data[x]):
            questions[int(split_data[x][:3].strip().strip('.'))] = split_data[x + 1]
    return questions

def extract_body(qtext):
    body = q_answer.split(qtext)[0]
    return body

def extract_answer(qtext):
    answer = q_answer.search(qtext)
    if answer:
        answer = answer.group()
    return answer

def extract_ref(qtext):
    ref = q_ref.search(qtext)
    if ref:
        ref = ref.group(0)
    return ref

def display_test(test, all_questions):
    for x in test:
        print 'Question #:', test.index(x) + 1
        display_question_delay(x, all_questions)
        print ''
    print 'Test:', test

def display_question(num, all_questions):
    print '(' + str(num) + ')'
    print extract_body(all_questions[num])
    print extract_answer(all_questions[num])
    print extract_ref(all_questions[num])

def display_question_delay(num, all_questions):
    print '(' + str(num) + ')'
    print remove_excess_newlines(extract_body(all_questions[num]))
    delay()
    print extract_answer(all_questions[num])
    print extract_ref(all_questions[num])

def delay():
    if TIME_DELAY:
        time.sleep(TIME_DELAY)
    else:
        raw_input()

def check_all(qs):
    answer_errors = []
    ref_errors = []
    for key in qs.keys():
        if extract_answer(qs[key]) == None:
            answer_errors.append(key)
        if extract_ref(qs[key]) == None:
            ref_errors.append(key)

    # print 'Ans errors:', answer_errors
    # print 'Ref errors:', ref_errors

    return (answer_errors, ref_errors)

def do_check(questions):
    checks = check_all(questions)
    total_errors = len(checks[0]) + len(checks[1])
    if total_errors:
        print 'Total errors:', total_errors
        print 'Ans Errors:', checks[0]
        print 'Ans Errors:', checks[1]
    


#### START HERE #######################
data = read_file(mqffn)
clean_data = remove_excess_newlines(''.join(data))
split_data = split_q_and_a(clean_data)
questions = extract_questions(split_data)

do_check(questions)


display_test(get_test(TEST_QUESTIONS), questions)

