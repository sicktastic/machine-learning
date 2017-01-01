range_iteration = 101
numbers = [i**2 for i in range(range_iteration)]

def mean():
    return sum(numbers) / len(numbers)

def median():
    numbers.sort()

    if (len(numbers) % 2 == 0):
        first_meidan_number = (numbers[len(numbers)/2])
        second_median_number = (numbers[(len(numbers)/2)+1])
        median = (first_median_number + second_median_number) / 2.0
        return median
    else:
        median = numbers[len(numbers) / 2]
        return median

def mode():
    return numbers[1]

print(numbers)
print("")
print("The mean of this list is " + str(mean()) + ".")
print("The median of this list is " + str(median()) + ".")
print("The mode of this list is " + str(mode()) + ".")
