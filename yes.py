import math

history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    else:
        return math.sqrt(x)

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x % y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def natural_log(x):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive numbers."
    else:
        return math.log(x)

def log_base(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Logarithm undefined for non-positive numbers or base 1."
    else:
        return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Factorial is undefined for negative numbers."
    else:
        return math.factorial(int(x))

def show_operations():
    print("\nSelect the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square (^2)")
    print("6. Square Root (√)")
    print("7. Power (x^y)")
    print("8. Modulus (%)")
    print("9. Sine (sin(x))")
    print("10. Cosine (cos(x))")
    print("11. Tangent (tan(x))")
    print("12. Natural Log (ln(x))")
    print("13. Logarithm (log(x, base))")
    print("14. Factorial (x!)")
    print("15. View History")
    print("16. Clear History")

def store_history(result):
    history.append(result)

def main():
    print("Welcome to the Calculator!")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        show_operations()

        operation = input("Enter the operation number (1-16) or 'exit' to quit: ")

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation == '15':
            if history:
                print("\nCalculation History:")
                for idx, result in enumerate(history, start=1):
                    print(f"{idx}. {result}")
            else:
                print("No history available.")
        
        elif operation == '16':
            history.clear()
            print("History cleared.")

        elif operation == '9':
            result = sine(num1)
            print(f"sin({num1}) = {result}")
            store_history(f"sin({num1}) = {result}")

        elif operation == '10':
            result = cosine(num1)
            print(f"cos({num1}) = {result}")
            store_history(f"cos({num1}) = {result}")

        elif operation == '11':
            result = tangent(num1)
            print(f"tan({num1}) = {result}")
            store_history(f"tan({num1}) = {result}")

        elif operation == '12':
            result = natural_log(num1)
            print(f"ln({num1}) = {result}")
            store_history(f"ln({num1}) = {result}")

        elif operation == '13':
            base = float(input("Enter the base for the logarithm: "))
            result = log_base(num1, base)
            print(f"log({num1}, {base}) = {result}")
            store_history(f"log({num1}, {base}) = {result}")

        elif operation == '14':
            result = factorial(num1)
            print(f"{num1}! = {result}")
            store_history(f"{num1}! = {result}")

        else:
            try:
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue

            if operation == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
                store_history(f"{num1} + {num2} = {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
                store_history(f"{num1} - {num2} = {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
                store_history(f"{num1} * {num2} = {result}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
                store_history(f"{num1} / {num2} = {result}")
            elif operation == '5':
                result = square(num1)
                print(f"Result: {num1} ^ 2 = {result}")
                store_history(f"{num1} ^ 2 = {result}")
            elif operation == '6':
                result = square_root(num1)
                print(f"Result: √{num1} = {result}")
                store_history(f"√{num1} = {result}")
            elif operation == '7':
                result = power(num1, num2)
                print(f"Result: {num1} ^ {num2} = {result}")
                store_history(f"{num1} ^ {num2} = {result}")
            elif operation == '8':
                result = modulus(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")
                store_history(f"{num1} % {num2} = {result}")
            else:
                print("Invalid operation! Please choose a valid option (1-16).")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator.")
            break

if __name__ == "__main__":
    main()

