def write_nonsense_code():
    code = """
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
def hilariously_inefficient_calculator(number1, number2):
"""

    with open("hilariously_inefficient_calculator.py", "w") as file:
        file.write(code)
        for i in range(2, 32):
            file.write(f"\n    if number1 == 1 and number2 == {i} or number1 == {i} and number2 == 1:\n        print({i})")
            for j in range(2, i // 2 + 1):
                file.write(f"\n    elif (number1 == {j} and number2 == {i-j}) or (number1 == {i-j} and number2 == {j}):\n        print({i})")
        file.write("\n")
        file.write("hilariously_inefficient_calculator(number1, number2)")

write_nonsense_code()
