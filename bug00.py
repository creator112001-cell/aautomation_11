def calculate_average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

data = [10, 20, 30, 40]
result = calculate_average(data)
print(f"The average is: {result}")