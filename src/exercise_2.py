import sys
import logging

logging.basicConfig(level=logging.INFO, format='\n%(message)s\n')


def sum_arrays(arr1, arr2):
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]

    carry = 0
    result = []

    max_len = max(len(arr1), len(arr2))
    for i in range(max_len):
        digit1 = arr1[i] if i < len(arr1) else 0
        digit2 = arr2[i] if i < len(arr2) else 0

        total = digit1 + digit2 + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return result[::-1]


def factorial(n):
    result = [1]
    for i in range(2, n + 1):
        arr_i = [int(digit) for digit in str(i)]
        result = sum_arrays(result, result)
        for _ in range(i - 2):
            result = sum_arrays(result, arr_i)
    return result


def multiply_arrays(num1, num2, arr1, arr2):
    iterations = min(num1, num2)
    larger_number_array = arr1 if num1 > num2 else arr2

    resul = [0]
    for _ in range(iterations):
        resul = sum_arrays(resul, larger_number_array)

    return resul


def multiply_numbers(num1, num2):
    is_positive = (num1 < 0) == (num2 < 0)
    num1, num2 = abs(num1), abs(num2)
    arr1 = [int(elem) for elem in str(num1)]
    arr2 = [int(elem) for elem in str(num2)]

    partial_result = multiply_arrays(num1, num2, arr1, arr2)
    result = partial_result if is_positive else ["-"] + partial_result

    return result


def multiply_array_by_number(arr, num):
    result = [0]
    for _ in range(num):
        result = sum_arrays(result, arr)
    return result


def factorial(n):
    result = [1]
    for i in range(n, 0, -1):
        result = multiply_array_by_number(result, i)
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python script.py <operation> [arguments]")
        logging.info("Operations: factorial <n>, multiply <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "factorial":
        if len(sys.argv) != 3:
            logging.error("Usage: python script.py factorial <n>")
            sys.exit(1)
        n = int(sys.argv[2])
        fact_result = factorial(n)
        logging.info(f"Factorial of {n}: {''.join(map(str, fact_result))}")

    elif operation == "multiply":
        if len(sys.argv) != 4:
            logging.error("Usage: python script.py multiply <num1> <num2>")
            sys.exit(1)

        try:
            num1 = int(sys.argv[2])
            num2 = int(sys.argv[3])
        except ValueError:
            logging.error("You must insert numbers! ")
            sys.exit(1)

        result = multiply_numbers(num1, num2)
        logging.info(f"Multiplication of {num1} and {
                     num2}: {''.join(map(str, result))}")

    else:
        logging.error("Unsupported operation. Use 'factorial' or 'multiply'.")
        sys.exit(1)
