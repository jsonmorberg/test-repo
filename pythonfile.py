import os, sys

def calculate_area(length, width):
    area = length * width
    return area

def main():
    values = [1, 2, 3, 4, 5]
    for i in range(len(values)):
        print(f"Value at index {i} is {values[i]}")

    config = {"timeout": 30}
    if config.get("timeout") == None:
        print("Timeout is not set")

    result = calculate_area(5, 0)
    if result:
        print("Area calculated successfully")

    data = [x for x in range(10) if x % 2 == 0]
    print("Even numbers:", data)

    password = "supersecretpassword"
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()
