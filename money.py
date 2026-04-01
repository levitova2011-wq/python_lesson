a = float(input("1л молока: "))
b = float(input("1 булка: "))
x = float(input("гроші: "))
c = float(input("морозиво: "))
d = 2*a + b
if x - d > c:
    print("Так, залишиться:", x - d - c, "грн")
elif x - d == c:
    print("Так, нічого не залишиться")
else:
    print("Ні, не вистачить:", c - d, "грн")

x2 = float(input("Enter x: "))
if x2 <=2:
    y=2*x2-3
else:
    y=3*x2-2
print("The value of y is:", y)