def calculate_average(numbers):
    if not numbers:
        return 0.0
    
    # Use built-in sum() for efficiency and to avoid indexing errors
    total = sum(numbers)
    average = total / len(numbers)
    return average

data = [10, 20, 30, 40]
result = calculate_average(data)

# Use f-string for cleaner and safer string formatting
print(f"The average is: {result}")
