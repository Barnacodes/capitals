import csv


def check_input(input_1):
    with open('CapitalsFolder/capitals.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter = ',')
        for row in csv_reader:
            if row[0] == input_1:
                print("The capital of {} is {}".format(input_1, row[1]))
            elif row[1] == input_1:
                print("The European state whose capital is {} is {}".format(input_1, row[0]))
            else:
                continue