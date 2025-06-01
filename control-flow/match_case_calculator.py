num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = int(num1 + num2)
        print(f"The result is {result}")

    case "-":
        result = int(num1 - num2)
        print(f"The result is {result}")

    case "*":
        result = int(num1 * num2)
        print(f"The result is {result}")

    case "/":
        result = int(num1 / num2)
        print(f"The result is {result}")
