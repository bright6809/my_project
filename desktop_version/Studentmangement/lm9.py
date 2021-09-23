
import os
import sqlite3

if __name__=="__main__":

  #  if not os.path.exists ("my_database"):
    con=sqlite3.connect("my_database")
    cur=con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS STUDENT(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,"
                "SEX TEXT,AGE INTEGER,PARENTNAME TEXT,TEL TEXT);")
    con.commit()
#    else:
 #       con=sqlite3.connect("my_database")
#        cur=con.cursor()
    con.execute("INSERT INTO STUDENT(NAME,SEX,AGE,PARENTNAME,TEL) VALUES('lILY','F',3,'Jhon','9029780966');")
    con.execute("INSERT INTO STUDENT(NAME,SEX,AGE,PARENTNAME,TEL) VALUES('SHAW','M',4,'TOM','9029782311');")

    cur.execute("SELECT * FROM STUDENT;")
    result=cur.fetchall()
    print(result)
    con.close()

    stu_list=[]
    for item in result:
        item1=[]
        for k in range(6):
            item1.append(item[k])
        stu_list.append(item1)
    print(stu_list)



