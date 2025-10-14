a = input("enter the first number:")
x = float(a)
op = input("enter the operation (+, -, *, /):")
b = input("enter the second number:")
y = float(b)
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    if y == 0:
        print("mistake:division by zero is prohibited!")
        raise SystemExit
    result = x / y
else:
    print("mistake: unknown operation!")
    raise SystemExit

print(f"Result: {result}")

