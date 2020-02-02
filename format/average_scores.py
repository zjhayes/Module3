# Zachary Hayes - zjhayes@dmacc.edu


def average():
    score1 = input("Enter score #1: ")
    score2 = input("Enter score #2: ")
    score3 = input("Enter score #3: ")
    return float(score1) + float(score2) + float(score3) / 3


def main():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    average_score = average()
    print("%s, %s age: %d average grade: %.2f" % (last_name, first_name, age, average_score))


if __name__ == '__main__':
    main()
