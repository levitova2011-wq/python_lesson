def max(x, y):
    if x>y:
        z = x
    else: z = y
    return z
def min(x, y):
    if x>y:
        z = y
    else: z = x
    return z
x1=float(input("x1="))
x2=float(input("x2="))
x3=float(input("x3="))
x4=float(input("x4="))
max1=max(x1, x2)
max2=max(max1, x3)
max3=max(max2, x4)
min1=min(x1, x2)
min2=min(min1, x3)
min3=min(min2, x4)
mean=(x1 + x2 + x3 + x4)/4
print("The biggest value is:", max3, "\nThe smallest value is:", min3, "\nMean value is:", mean)