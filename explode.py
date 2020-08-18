#Python test
#import socket
#hostname = socket.gethostname()
#print("Host name is " + hostname)

# Create csv files
import csv
import random
from faker import Faker
def csv_creator():
    fake = Faker()
    csvCount = 0
    numRecordName = int(input("How many would you like to create"))
    print("Creating CSV files")
    for i in range(numRecordName):
        file = open(str(i)+'Addressbook.csv','w+')
        file.write("First Name," + "Last Name," + "Cell Phone Number," + "Street Address" + "\n")
        fileSize=random.randrange(5000)
        csvCount += 1
        for i in range(fileSize):
            name = fake.first_name()
            lname = fake.last_name()
            cell = fake.numerify('(###)-###-####')
            street = fake.street_address()
            file.write(name + "," + lname + "," + cell + "," + street + "\n")
            fileSize=random.randrange(5000)
    file.close()
    print(str(csvCount) + " csv files created.")

#csv_creator()
def docx_creator():
    docNumber = input("How many documents would you like to create?")
    fileSize=random.randrange(500000, 1000000) 
    for i in range(int(docNumber)):
        file=open(str(i)+"document.docx",'w+')
        for i in range(fileSize):
            file.write('Filler data')
            fileSize=random.randrange(5000)
    for i in range(int(docNumber)):
        file.close()
        print(str(docNumber) + " Doc files created")

select = int(input("What type of document would you like to create? Press [1] for .csv [2] for .docx "))
if select == 1:
    csv_creator()
elif select == 2:
    docx_creator()

