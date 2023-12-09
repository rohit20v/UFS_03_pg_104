import random

if __name__ == '__main__':
    A = [random.randint(1, 23, ) for _ in range(10)]

    print(A)
    reversedList = A[::-1]
    print(reversedList)
