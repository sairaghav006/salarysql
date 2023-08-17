import mysql.connector as mysql
import xlrd

#Use your MySQL connection details to connect to the DB

db = mysql.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "****",
    database = "practice")

cursor = db.cursor(buffered=True)

query1="CREATE SCHEMA `lip` ;"
#cursor.execute(query1)
usedb="""USE LIP"""
##Creating a table

table_query="""CREATE TABLE `lip`.`kaggle` (

  `SNO` INT,
  `AGE` INT NULL,
  `GENDER` VARCHAR(45) NULL,
  `EDUCATION` VARCHAR(45) NOT NULL,
  `JOBTITLE` VARCHAR(45) NOT NULL,
  `YOE` INT NULL,
  `SALARY` BIGINT NULL,
  PRIMARY KEY (`SNO`),
  UNIQUE INDEX `SNO_UNIQUE` (`SNO` ASC) VISIBLE);"""

book=xlrd.open_workbook("KaggleData.xls")
sheet=book.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

delq="""DELETE FROM LIP.kaggle WHERE SNO=2"""
cursor.execute(delq)
db.commit()

age=0
gender=''
education=''
jobtitle=''
yoe=0
salary=0

for i in range(6,sheet.nrows):
    for j in range(sheet.ncols):
        if j==0:
            age=sheet.cell_value(i,j)
        elif j==1:
            gender=sheet.cell_value(i,j)
        elif j==2:
            education=sheet.cell_value(i,j)
        elif j==3:
            jobtitle=sheet.cell_value(i,j)
        elif j==4:
            yoe=sheet.cell_value(i,j)
        elif j==5:
            salary=sheet.cell_value(i,j)
    stdq="""INSERT INTO LIP.kaggle(SNO,age,gender,education,jobtitle,yoe,salary) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    values=(i,age,gender,education,jobtitle,yoe,salary)
    #cursor.execute(stdq,values)
    #db.commit()

query1="""SELECT DISTINCT(education) FROM LIP.KAGGLE"""
cursor.execute(query1)
result1=cursor.fetchall()
print(result1)
