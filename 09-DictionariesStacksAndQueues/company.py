import csv
with open('it_company.csv', 'r') as file:
    company_reader = csv.reader(file)
    for line in company_reader:
        print(line)
