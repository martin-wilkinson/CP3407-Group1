import csv

def getData(source, index):
    source = int(input("Enter the item number:"))
    with open("CSVTestData.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')

        lines = []
        for line in reader:
            lines.append(line)

        # print(lines[marked_item])
        print(lines[source][index])