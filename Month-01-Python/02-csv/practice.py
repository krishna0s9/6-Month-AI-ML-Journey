import csv
with open ( 'month-01-Python/02-csv/students.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

   

    with open ( 'month-01-Python/02-csv/new_students.csv', 'w') as new_file:

     fieldnames= [ 'name', 'age']

     csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter ='\t')

     csv_writer.writeheader()

     for line in csv_reader:
        del line ['course']
        csv_writer.writerow(line)
