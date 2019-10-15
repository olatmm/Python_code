import csv


def main():
    open_csv()
    FirstName, LastName = open_csv('customers.csv')
    print(FirstName)
    print(LastName)


def open_csv(customers):
    FirstName = []
    LastName = []
    with open(customers, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            FirstName.append(row[0])
            LastName.append(row[1])
    return FirstName, LastName


if __name__ == '__main__':
    main()

