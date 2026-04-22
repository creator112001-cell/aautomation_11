def calculate_average(numbers):
    if not numbers:
        return 0.0
    
    # Use built-in sum() for idiomatic and efficient calculation
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == "__main__":
    data = [10, 20, 30, 40]
    result = calculate_average(data)
    # f-string handles float-to-string conversion safely
    print(f"The average is: {result}")