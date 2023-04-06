def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num-1)

def main():
    for i in range(0, 15, 2):
        print("{0}! = {1}".format(i,factorial(i)))

if __name__ == '__main__':
    main()
