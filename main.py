import sys


def run():
    ints_list, error = convert_to_int(sys.argv[1:])
    if error:
        raise Exception(error)
    fizz_buzz_list = fizz_buzz(ints_list[0], ints_list[1])
    print(*fizz_buzz_list, sep="\n")


def fizz_buzz(start, end):
    values_list = list()
    for num in range(start, end + 1):
        value = ""
        if num % 3 == 0:
            value += "Fizz"
        if num % 5 == 0:
            value += "Buzz"
        if not value:
            value = num
        values_list.append(value)

    return values_list


def convert_to_int(args_list):
    if len(args_list) == 0:
        return [1, 100], None
    elif len(args_list) == 1:
        args_list.append(1)
    elif len(args_list) > 2:
        return None, "You cannot enter more than 2 arguments"
    try:
        final_list = []
        for arg in args_list:
            final_list.append(int(arg))
            if int(arg) == 0:
                return (
                    None,
                    "When entering integers ensure they are greater than 0",
                )
        final_list.sort()
        return final_list, None
    except ValueError:
        return None, "Please enter integers only"


run()
