numbers = [i**2 for i in range(10)]

def mean():
    return sum(numbers) / len(numbers)

print(mean())

def median():
    numbers.sort()

print(median())

def mode():
    numbers.sort()
