import random

if __name__ == '__main__':
    A = [random.randint(1, 69) for _ in range(10)]
    print(A)
    while True:
        try:
            num = int(input("Enter a number you wanna find "))
            if num in A:
                print("Number you've entered exists in the list")
                break
            else:
                print("\nThe number you've entered does not exist in the list")
        except:
            print("Enter a number pls")
