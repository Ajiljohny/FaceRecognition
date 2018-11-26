import pymysql
from datetime import *
db = pymysql.connect("localhost","root","root","hrm")
cursor = db.cursor()
#sql = "SELECT * FROM dataset"
#sql= "INSERT INTO attendance(uid,name,entry) VALUES ('%s','%s','%s')" % ('Aj123',"Ajil",day)
#sql="create or replace view attview as select c.uid,c.name,c.entry,p.eLastName,Year(entry) as Ryear,Month(entry) as Rmonth, monthname(entry) as Month " \
#    "from attendance c,employeeinfo p where c.uid=p.eEmployeeCodeNumber;";
#sql = "Select Ryear, count(*) as total from attview Group By Ryear order by Ryear;";
sql = "Select Ryear, Month, Rmonth,  count(*) as total from attview Group By concat(Ryear, Rmonth), Ryear order by Rmonth"
cursor.execute(sql)
db.commit()
#try:
#   cursor.execute(sql)
results = cursor.fetchall()
for row in results:
      print(row)
#except:
 #  print ("Error: unable to fetch data")
db.close()