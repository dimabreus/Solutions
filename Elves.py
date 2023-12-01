import re

func1 = lambda a: sum(int("".join(re.findall(r'\d', i))) for i in a)


def func2(strings: []):
    result = 0
    for i in strings:
        result += int("".join(re.findall(r'\d', i)))
    return result


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
        numbers = re.findall(r'\d', string)

        for number in numbers:
            numbers_in_stroke += str(number)

        if numbers_in_stroke != "":
            finally_result += int(numbers_in_stroke)

    return int(finally_result)


test_functions = lambda a: print(f"func1: {func1(a)}"
                                 f"\nfunc2: {func2(a)}"
                                 f"\nhelping_elves: {helping_elves(a)}")

test_functions(
    [
        "a1b2",
        "c3d4"
    ]
)
