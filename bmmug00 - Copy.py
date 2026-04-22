def calculate_average(numbers):
    # Check if input is None, not a list/tuple, or empty
    if not numbers or not isinstance(numbers, (list, tuple)):
        return 0.0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

data = [10, 20, 30, 40]
result = calculate_average(data)
print(f"The average is: {result}")