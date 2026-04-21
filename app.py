# app.py
def divide(a, b):
    return a / b  # will crash when b == 0

if __name__ == "__main__":
    print(divide(1, 0))  # this line causes ZeroDivisionError