def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i + 1]   # off‑by‑one: IndexError
    average = total / len(numbers)
    return average

data = [10, 20, 30, 40]
result = calculate_average(data)
print("The average is: " + result)   # TypeError: can't concatenate str + float