def populateList(b: list):
    odd = 1
    even = 0
    while odd < len(b) + 1 or even < len(b):
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                if even < 10:
                    if even % 2 == 0:
                        b[even] = number
                        even += 2
                        print(b)
                else:
                    even += 2
                    print("No more even cells are available")
                    continue
            elif number % 2 != 0:
                if odd < 10:
                    if odd % 2 != 0:
                        b[odd] = number
                        odd += 2
                        print(b)
                else:
                    odd += 2
                    print("No more odd cells are available")
        except:
            print("Error!!")


if __name__ == '__main__':
    list = [0 for _ in range(10)]
    print(list)

    populateList(list)

    for index, elems in enumerate(list):
        print("The list contains these number:", elems, "on index:", index)
