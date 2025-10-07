n = int(input("please enter the integer number: "))

a = n // 10000
b = (n // 1000) % 10
c = (n // 100) % 10
d = (n // 10) % 10
e = n % 10

reverse = e * 10000 + d * 1000 + c * 100 + b * 10 + a

print("inverted number:", reverse)
