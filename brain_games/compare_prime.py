def compare_answers(number, user_answer, name, n):
    for i in range(2, number):
        correct_answer = bool(number % i != 0)
        if correct_answer is False:
            break

    if (correct_answer is True and user_answer == 'yes') \
        or (correct_answer is False and user_answer == 'no'):
        a = 'Correct!'
        n += 1
        print(a)
        return n

    else:
        n = 0
        if correct_answer is True:
            a = user_answer 
                + " is wrong answer ;(. Correct answer was 'yes'\nLet's try again, " 
                + name + "!"
        else:
            a = user_answer 
                + " is wrong answer ;(. Correct answer was 'no'\nLet's try again, " 
                + name + "!"
        print(a)
        return n
