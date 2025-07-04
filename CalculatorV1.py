while True:
    operator = input("Enter an operator (+ - * /), or 'q' to quit: ")

    if operator.lower() == "q":
        print("Calculator closed.")
        break

    try:
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if operator == "+":
        result = num1 + num2
        print("Result:", round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print("Result:", round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print("Result:", round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("You can't divide by zero.")
        else:
            result = num1 / num2
            print("Result:", round(result, 3))
    else:
        print(f"'{operator}' is not a valid operator.")
