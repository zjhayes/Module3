# Zachary Hayes - zjhayes@dmacc.edu


def average():
    score1 = input("Enter score #1: ")
    score2 = input("Enter score #2: ")
    score3 = input("Enter score #3: ")
    average = int((int(score1) + int(score2) + int(score3)) / 3)
    print(average)


def main():
    average()


if __name__ == '__main__':
    main()
