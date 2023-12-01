result = 0
while True:
    input_string = input("Введите число или слово ")
    try:
        if input_string == "стоп".lower():
            break

        elif int(input_string):
            result += int(input_string)
            print(result)
    except Exception: None
