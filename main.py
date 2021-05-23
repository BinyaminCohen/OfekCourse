from random import randint

FROM_NUM = 0
TO_NUM = 20


# Fibonacci series calculation
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print("{},".format(a), end="")


def avg():
    sum_num = 0
    count_num = 0

    while True:
        user_input = input("Please enter 'q' to quit or any number to continue:")

        if user_input == 'q':  # if the input was 'q' -> quit the loop
            break

        try:

            user_input = int(user_input)

        except ValueError:
            print("Please enter only 'q' to exit or any number for calc avg!")

        else:
            sum_num += user_input
            count_num += 1

    print("The average of the numbers is: {} ".format(sum_num / count_num))


# def calc_avg():
#     sum_num = 0
#     count_num = 0
#
#     while True:
#         user_input = input("Please enter 'q' to quit or any number to continue: ").split()
#         if 'q' or 'Q' in user_input:
#             break
#         else:
#             try:
#                 strings = [str(i) for i in user_input]
#                 a_string = "".join(strings)
#                 an_integer = int(a_string)
#             # user_input = int([int(i) for i in user_input])
#
#             except ValueError:
#                 print("Please enter only 'q' to exit or any number for calc avg!")
#             sum_num += an_integer
#             count_num += 1
#
#
#     try:
#         print("The avg is {}.".format(sum_num / count_num))
#     except ZeroDivisionError:
#         print("ZeroDivisionError!")
# def generate_random_numbers():
#     rand_num = randint(0, 10)
#     rand_list = []
#     for i in range(5):
#         rand_list.append(randint(0, 30))
#
#     print("The div number: {} ".format(rand_num))
#     print("The list number: {} ".format(rand_list, end=""))
#
#     return rand_num, rand_list


# def change_list_by_div_num(num_to_div, lst):
#     for num_form_lst in lst:
#         if num_form_lst % num_to_div == 0:
#             lst.pop(lst.index(num_form_lst))
#     print(lst)

def generate_random_number():
    return randint(FROM_NUM, TO_NUM)


def change_list_by_div_num():
    num_to_div = generate_random_number()
    if num_to_div == 0:
        raise Exception("We can't divided by zero!")

    rand_lst = []
    for i in range(5):
        rand_lst.append(generate_random_number())

    print("The additional number is: {} ".format(num_to_div))
    print("The list is {} ".format(rand_lst))
    rand_lst[:] = [num_form_lst for num_form_lst in rand_lst if (num_form_lst % num_to_div) != 0]

    print("\nThe numbers that are not divisible by the additional number {}".format(rand_lst))


# def change_list_by_div_num(num_to_div, lst):
#     for num_form_lst in lst:
#         if num_form_lst % num_to_div == 0:
#             lst.pop(lst.index(num_form_lst))
#     print(lst)

if __name__ == "__main__":
    # fib(10)
    # avg()
    change_list_by_div_num()
