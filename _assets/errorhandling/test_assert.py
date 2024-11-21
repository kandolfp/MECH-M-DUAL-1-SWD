import numbers
numberlist = [-2, -1, 0, 1, 2, "a", 1/4]

for number in numberlist:
    try:
        assert isinstance(number, numbers.Number)
        assert number != 0
        inverse = 1.0 / number
    except AssertionError:
        print(f"Error: I can not compute the inverse of {number}!")
    else:
        print(f"Check: {inverse} * {number} = {inverse * number}")
