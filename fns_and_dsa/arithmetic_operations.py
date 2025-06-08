#Define function
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2

    else:
        return "Error: Invalid operation"

#Input user data
print("Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

#Calculations
result = perform_operation(num1, num2, operation)

#results of calculations
print(f"result: {result}")
