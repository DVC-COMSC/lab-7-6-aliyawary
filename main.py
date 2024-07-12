def getInput():
    uservalues = input('Enter Values: ')
    numbers = list(uservalues.split())
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers


def makeReverse(numbers):
    revList = []
    for i in range(len(numbers)):
        x = numbers.pop(-1)
        revList.append(x)
    return revList


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
