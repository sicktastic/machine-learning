range_iteration = 210
numbers = [i**2 for i in range(range_iteration)]

def mean():
    return sum(numbers) / len(numbers)

def median():
    numbers.sort()

    if (len(numbers) % 2 == 0):
        first_middle_number = (numbers[len(numbers)/2])
        second_middle_number = (numbers[(len(numbers)/2)+1])
        median = (first_middle_number + second_middle_number) / 2.0
        return median
    else:
        median = numbers[len(numbers) / 2]
        return median

print(numbers)
print(mean())
print(median())
