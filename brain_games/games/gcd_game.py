from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = randint(1, 1000)
    num2 = randint(1, 1000)
    return str(num1) + ' ' + str(num2)


def game(question):
    nums_list_final = []
    nums_list = question.split()
    for _ in nums_list:
        nums_list_final.append(int(_))
    nums_list_final.sort()

    for devider in range(nums_list_final[0], 0, -1):
        if nums_list_final[1] % devider == 0 and nums_list_final[0] % devider == 0:
            return str(devider)
