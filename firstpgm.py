# This program reads the CSV file and create the ddl and dml for on boarding new cloud devices
# Next step : read from a json. Identify derived metric and the rules for it.
import csv
with open('urs.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            header = row
            line_count += 1
        else:
            column_count = len(row)
            print(header)
            i = 0
            for i in range(column_count):
               print(header[i],':',row[i])
            line_count += 1
    print(f'Processed {line_count} lines.')
    f = open("ddl.txt", "a")
    f.write("Now the file has four more line!\n")
    f.close()
    f = open("dml.txt", "a")
    f.write("Now the file has four more line!\n")
    f.close()
