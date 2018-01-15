import numpy as np

def test_run():
    # a = np.random.random((5,4))
    # print(a)
    # print(a.shape)

    # print(a.shape[0]) # number of rows
    # print(a.shape[1]) # number of columns
    # print(len(a.shape))
    # print(a.size)
    # print(a.dtype)

    np.random.seed(693) # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4)) # 5x4 random integers in [0, 10])
    print(" Array: \n", a)
    print("Sum of all elements:\n", a.sum())
    print("Sum of each column:\n", a.sum(axis=0))
    print("Sum of each row:\n", a.sum(axis=1))
    print("Minimum of each colum:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.min(axis=1))
    print("Mean of all elements:", a.mean())


if __name__ == '__main__':
    test_run()
