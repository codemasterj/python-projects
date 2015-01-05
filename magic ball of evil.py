import random

while True:
    answers = ['yea',
               'no',
               'maybe',
               'im evil',
               'uh dont know',
               'im not positive]


    print('welcome to magic eight ball')
    print('ask your question below.')

    question = input('<')

    answer = random.choice(answers)
    print(answer)
