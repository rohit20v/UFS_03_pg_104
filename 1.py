if __name__ == '__main__':
    dim = 10
    A = []
    for i in range(dim):
        try:
            num = int(input("Enter a number"))
            A.append(num)
        except:
            print("Enter a number pls")
