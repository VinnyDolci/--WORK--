import csv

myDict = [{'name': 'vincent', 'lname': 'dolciato'}]

myDict.append({'name': 'joe', 'lname': 'schmoe'})

newFname = input('What is your first name? ')
newLName = input('What is your last name? ')

myDict.append({'name': newFname, 'lname': newLName})

for a in myDict:
    print(a)

fields = ['name', 'lname', 'surname', 'prefix']

filename = 'dictionarytest.csv'

with open(filename, 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames = fields)

    writer.writeheader()

    writer.writerows(myDict)