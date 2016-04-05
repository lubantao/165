# table EIA
import psycopg2 as dbapi
import csv
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

file = open(r'EIA_CO2_Electricity_2015.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
        A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE EIA (%s)"%(", ".join(A))\
 )
con.commit()

for row in list1[1:]:
     cur.execute("INSERT INTO EIA  VALUES  ( %s)"%(str(row)[1:-1]))

con.commit()

file.close()

file = open(r'EIA_MkWh_2015.CSV', 'r')
csvObject = csv.reader(file)
list1 = list(csvObject )

for row in list1[1:]:
     cur.execute("INSERT INTO EIA  VALUES  ( %s)"%(str(row)[1:-1]))


con.commit()

file.close()


file = open(r'EIA_CO2_Transportation_2015.csv', 'r')
csvObject = csv.reader(file)
list1 = list(csvObject )

for row in list1[1:]:
     cur.execute("INSERT INTO EIA  VALUES  ( %s)"%(str(row)[1:-1]))

con.commit()

file.close()

cur.close()
con.close()

# tables for  NHTS

import psycopg2 as dbapi
import csv
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

file = open(r'DAYV2PUB.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
        A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE DAYV2PUB (%s)"%(", ".join(A))\
 )
con.commit()


for row in list1[1:]:
     cur.execute("INSERT INTO DAYV2PUB  VALUES  ( %s)"%(str(row)[1:-1]))


con.commit()

file.close()

cur.close()
con.close()

import psycopg2 as dbapi
import csv
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

file = open(r'HHV2PUB.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
        A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE HHV2PUB (%s)"%(", ".join(A))\
 )
con.commit()


for row in list1[1:]:
     cur.execute("INSERT INTO HHV2PUB  VALUES  ( %s)"%(str(row)[1:-1]))


con.commit()

file.close()

cur.close()
con.close()

import psycopg2 as dbapi
import csv
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

file = open(r'PERV2PUB.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
        A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE PERV2PUB (%s)"%(", ".join(A))\
 )
con.commit()


for row in list1[1:]:
     cur.execute("INSERT INTO PERV2PUB  VALUES  ( %s)"%(str(row)[1:-1]))


con.commit()

file.close()


cur.close()
con.close()

import psycopg2 as dbapi
import csv
con = dbapi.connect(database="dbname", user="username")
cur = con.cursor()

file = open(r'/VEHV2PUB.CSV', 'r')

csvObject = csv.reader(file)
list1 = list(csvObject )
head = list1[0]
NumVar = len(head)

A=["%s varchar(100)"%head[0]]
for i in range(1,NumVar):
        A.append("%s varchar(100)"%head[i])


cur.execute("CREATE TABLE VEHV2PUB (%s)"%(", ".join(A))\
 )
con.commit()


for row in list1[1:]:
     cur.execute("INSERT INTO VEHV2PUB  VALUES  ( %s)"%(str(row)[1:-1]))

con.commit()

file.close()

cur.close()
con.close()
