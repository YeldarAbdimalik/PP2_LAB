#task 1

def square_generator(n):
    for i in range(n + 1):
        yield i * i


# Test
for value in square_generator(5):
    print(value)

#task 2

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input("Enter n: "))

print(",".join(str(num) for num in even_numbers(n)))

#task 3

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for num in divisible_by_3_and_4(100):
    print(num)

#task 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


# Test
for value in squares(3, 7):
    print(value)

#task 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Test
for number in countdown(5):
    print(number)
    