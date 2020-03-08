import hashlib
import csv
with open('super_pin_rainbow_table.csv', "w+") as outfile:
    column_name=['PIN', 'MD5','SHA1','SHA256','SHA512']
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(column_name)
    #4 digit pins
    for pin in range(10000):
        pinMD5 = hashlib.md5(str(f"{pin:04}").encode('utf-8')).hexdigest()
        pinSHA1 = hashlib.sha1(str(f"{pin:04}").encode('utf-8')).hexdigest()
        pinSHA256 = hashlib.sha256(str(f"{pin:04}").encode('utf-8')).hexdigest()
        pinSHA512 = hashlib.sha1(str(f"{pin:04}").encode('utf-8')).hexdigest()
        csv_writer.writerow([str(f"{pin:04}"),pinMD5,pinSHA1,pinSHA256,pinSHA512])
    #6 digit pins
    for pin in range(1000000):
        pinMD5 = hashlib.md5(str(f"{pin:06}").encode('utf-8')).hexdigest()
        pinSHA1 = hashlib.sha1(str(f"{pin:06}").encode('utf-8')).hexdigest()
        pinSHA256 = hashlib.sha256(str(f"{pin:06}").encode('utf-8')).hexdigest()
        pinSHA512 = hashlib.sha1(str(f"{pin:06}").encode('utf-8')).hexdigest()
        csv_writer.writerow([str(f"{pin:06}"),pinMD5,pinSHA1,pinSHA256,pinSHA512])
    #8 digit pins
    for pin in range(100000000):
        pinMD5 = hashlib.md5(str(f"{pin:08}").encode('utf-8')).hexdigest()
        pinSHA1 = hashlib.sha1(str(f"{pin:08}").encode('utf-8')).hexdigest()
        pinSHA256 = hashlib.sha256(str(f"{pin:08}").encode('utf-8')).hexdigest()
        pinSHA512 = hashlib.sha1(str(f"{pin:08}").encode('utf-8')).hexdigest()
        csv_writer.writerow([str(f"{pin:08}"),pinMD5,pinSHA1,pinSHA256,pinSHA512])
