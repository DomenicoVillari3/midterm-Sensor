import csv

def write_to_csv(data, filename):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
