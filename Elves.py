import re


# func1 = lambda a: sum(int(re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', i)[0] + re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', i)[-1]) for i in a)
#
#
# def func2(strings: list):
#     result = 0
#     for i in strings:
#         numbers_in_str = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', i)[0] + re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', i)[-1]
#         result += int(numbers_in_str)
#     return result


def helping_elves(strings: list[str]) -> int:
    """
    Принимает массив строк с числами;\n
    Возвращает сумму чисел из строк.\n
    helping_elves(["a1b2"]) #12\n
    helping_elves(["a1b2", "c3d4"]) #46
    """

    for string in strings:
        if not isinstance(string, str):
            return 0

    finally_result = 0

    for string in strings:
        numbers_in_stroke = ""
        numbers = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', string)

        for number in numbers:
            if number == "one":
                numbers_in_stroke += "1"
            elif number == "two":
                numbers_in_stroke += "2"
            elif number == "three":
                numbers_in_stroke += "3"
            elif number == "four":
                numbers_in_stroke += "4"
            elif number == "five":
                numbers_in_stroke += "5"
            elif number == "six":
                numbers_in_stroke += "6"
            elif number == "seven":
                numbers_in_stroke += "7"
            elif number == "eight":
                numbers_in_stroke += "8"
            elif number == "nine":
                numbers_in_stroke += "9"
            elif number in "123456789":
                numbers_in_stroke += str(number)

        if numbers_in_stroke != "":
            finally_result += int(numbers_in_stroke[0] + numbers_in_stroke[-1])

    return int(finally_result)




# def helping_elves_another(strings: list[str]) -> int:
#     """
#     Принимает массив строк с числами;\n
#     Возвращает сумму чисел из строк.\n
#     helping_elves(["a1b2"]) #12\n
#     helping_elves(["a1b2", "c3d4"]) #46
#     """
#
#     for string in strings:
#         if not isinstance(string, str):
#             return 0
#
#     finally_result = 0
#
#     for string in strings:
#         numbers_in_stroke = ""
#
#         for letter in string:
#             if letter in "0123456789":
#                 numbers_in_stroke += letter
#
#         if numbers_in_stroke != "":
#             finally_result += int(numbers_in_stroke[0] + numbers_in_stroke[-1])
#
#     return int(finally_result)


# test_functions = lambda a: print(f"func1: {func1(a)}"
#                                  f"\nfunc2: {func2(a)}"
#                                  f"\nhelping_elves: {helping_elves(a)}"
#                                  f"\nhelping_elves_another: {helping_elves_another(a)}")

print(
    helping_elves(
        open("data.txt", "r", encoding="utf-8").readlines()
    ))
