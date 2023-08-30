from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    return str(num1) + ' ' + str(num2)


def game(question):
    nums_list_final = []
    nums_list = question.split()
    for _ in nums_list:
        nums_list_final.append(int(_))
    nums_list_final.sort()

    for greatest_divisor in range(nums_list_final[0], 0, -1):
        num1 = nums_list_final[0]
        num2 = nums_list_final[1]
        if num1 % greatest_divisor == 0 and num2 % greatest_divisor == 0:
            return str(greatest_divisor)
