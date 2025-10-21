while True:
    x = float(input("Enter the first number: "))
    option = input("Enter an option (+, -, *, /): ")
    y = float(input("Enter the second number: "))

    if option == "+":
        result = x + y
    elif option == "-":
        result = x - y
    elif option == "*":
        result = x * y
    elif option == "/":
        if y == 0:
            print("mistake: Division by zero is not allowed!")
            continue
        result = x / y
    else:
        print("Unknown operation!")
        continue

    print(f"Result: {result}")

    choice = input("Do you want to continue? (y/n): ")
    if choice not in ("y", "yes"):
        print("Goodbye!")
        break
