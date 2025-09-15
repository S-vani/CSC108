print(type(2.0))
print(round(1/3, 1))
print(1/float('inf'))

print(2**-1) # in this case the negative is a unary number not binary

print(9.5//2)
print(9.0%3)
print(0.1+0.2)
print(-2//3) # floor division with negative rounds up so this is -1
# -4 = -1 * 3 + 1
print(5==5)

x = 5
y = 4
x = y+1 * x
print(y//x)


def square(x: int) -> int:
    return x**2


print(square(2))

def example(x: int):
    print(1 * x)
    return 3 * x # return function will simply EXIT the loop and ignore the stuff under
    print(2 * x)

a = example(1)

def example2(x: int):
    print(1 * x)
    return

a = example2(1)
print(a) # will print None

def convert_temp(temp: int, celsius: bool) -> float:
    if celsius:
        return round((temp * (9/5)) +32, 2)
    else:
        return round((temp-32) * (5/9), 2)

print(convert_temp(80, True))

print("test")


