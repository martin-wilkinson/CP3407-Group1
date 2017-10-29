import csv

def getData(source, index):
    with open("CSVTestData.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')

        lines = []
        for line in reader:
            lines.append(line)

        return lines[source][index]