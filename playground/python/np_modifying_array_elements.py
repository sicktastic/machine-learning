import numpy as np

def test_run():
    a = np.random.rand(5, 4)
    print("Array:\n", a)

    # a[0, 0] = 1
    a[:, 3] = [1,2,3,4,5]
    print("\nModified (replaced one element:)\n", a)


if __name__ == '__main__':
    test_run()
