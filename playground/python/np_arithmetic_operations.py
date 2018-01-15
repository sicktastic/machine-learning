import numpy as np

def test_run():
    a = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    print("Original array a:\n", a)

    # Multiply a by 2
    print("\nMultiply a by 2:\n", 2 * a)

    b = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    print("Original array b:\n", b)

    # Divide b by 2
    print("\nDivide b by 2:\n", a / 2.0)

    print(a + b)
    print(a * b)


if __name__ == '__main__':
    test_run()
