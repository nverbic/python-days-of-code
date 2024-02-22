'''
    Day 42
    Write a program that uses a try-except block to handle division by zero

    Output:
    Division error 20 / 0:-> division by zero
    20 / 10 == 2.0
    20 / 1e+308 == 2e-307
    20 / inf == 0.0
    Division error -20 / 0:-> division by zero
    -20 / 10 == -2.0
    -20 / 1e+308 == -2e-307
    -20 / inf == -0.0
    Division error 1 / 0:-> division by zero
    1 / 10 == 0.1
    1 / 1e+308 == 1e-308
    1 / inf == 0.0
    Division error 1e+308 / 0:-> float division by zero
    1e+308 / 10 == 1e+307
    1e+308 / 1e+308 == 1.0
    1e+308 / inf == 0.0
'''

def handle_division_errors(num1, num2):
    ''' Handle division by zero '''
    result = None
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Division error {num1} / {num2}:-> {e}")
    except Exception as e:
        print(f"An error has occured -> {e}")

    return result

if __name__ == "__main__":
    numbers = [20, -20, 1, 1e308]
    divisors = [0, 10, 1e308, 1e308*1e308]

    for n in numbers:
        for divisor in divisors:
            result = handle_division_errors(n, divisor)
            if result is not None:
                print(f"{n} / {divisor} == {result}")
