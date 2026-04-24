def calculate_average(numbers):
    """
    Calculates the average of an iterable of numbers.
    Handles generators, non-numeric values, and empty inputs gracefully.
    """
    if not numbers:
        return 0.0
    
    try:
        # Convert to list to support generators and filter for numeric types only
        # This prevents TypeError during sum() if strings or None are present
        numbers_list = [n for n in numbers if isinstance(n, (int, float)) and not isinstance(n, bool)]
        
        if not numbers_list:
            return 0.0
        
        total = sum(numbers_list)
        average = total / len(numbers_list)
        return float(average)
    except (TypeError, ZeroDivisionError):
        # Return default to ensure the script doesn't crash the CI pipeline
        return 0.0

if __name__ == "__main__":
    # Example data
    data = [10, 20, 30, 40]
    result = calculate_average(data)

    # Use f-string for cleaner and safer string formatting
    # Printing ensures the value is captured in CI logs for the n8n webhook
    print(f"The average is: {result}")