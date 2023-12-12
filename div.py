def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Example usage:
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

result = divide_numbers(dividend, divisor)

print(f"The result of {dividend} divided by {divisor} is: {result}")
