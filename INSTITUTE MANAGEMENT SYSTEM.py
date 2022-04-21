import pymysql as pm
print("imported successfully")

#connecting database
def getconnect():
    return pm.connect(host="localhost",user="root",password="Rahul@123",database="rk")

#adding employee data
def addemp():
    eid=input("enter employee Id:").lstrip()
    ename=input("enter employee Name:").lstrip()
    ecourse=input("enter employee Course:").lstrip()
    esalary=input("enter employee Salary:").lstrip().upper()

    t=(eid,ename,edepartment,esalary)

    db=getconnect()
    cr=db.cursor()

    sql="insert into ims values(%s,%s,%s,%s);"
    cr.execute(sql, t)

    print("data inserted successfully\n")
    db.commit()
    db.close()


#showing courses
def showcourse():
    db=getconnect()
    cr=db.cursor()

    sql="select ecourse from ims"
    cr.execute(sql)

    data=cr.fetchall()

    for d in data:
        print(f"{d[0]:^20} \n")

    db.commit()
    db.close()

#update course

def updatecourse(uc):
    db=getconnect()
    cr=db.cursor()
    
    if uc=="1":
        
        eid=input("Enter Employee id:").lstrip()
        ecourse=input("enter course you want to update:").lstrip()
        t=(ecourse,eid)
        sql="update ims set ecourse=%s where eid=%s"
        cr.execute(sql,t)

        print("course updated successfully")

    db.commit()
    db.close()

#update employee detail

def updatedata(ued):
    db=getconnect()
    cr=db.cursor()

    if ued == "1":
        eid = input("Enter Employee Id : ").lstrip()
        ename = input("Enter New Name : ").lstrip()
        t = (ename, eid)
        sql = "update ims set ename=%s where eid = %s;"
        cr.execute(sql,t)

    if ued == "2":
        eid = input("Enter Employee Id : ").lstrip()
        ecourse = input("Enter New Course : ").lstrip()
        t = (ecourse, eid)
        sql = "update ims set ecourse=%s where eid = %s;"
        cr.execute(sql,t)

    if ued == "3":
        eid = input("Enter Employee Id : ").lstrip()
        esalary = input("Enter New Salary : ").lstrip()
        t = (esalary, eid)
        sql = "update ims set esalary=%s where eid = %s;"
        cr.execute(sql,t)

    if ued == "4":
        eid = input("Enter Employee Id : ").lstrip()
        neid = input("Enter New Id : ").lstrip()
        t = (neid, eid)
        sql = "update ims set eid=%s where eid = %s;"
        cr.execute(sql,t)

        print("employee details updated successfully")

    db.commit()
    db.close()

#deleting course
def deletecourse():
    eid=input("enter employee id here to delete:").lstrip()
    db=getconnect()
    cr=db.cursor()

    sql="update ims set ecourse=NULL where eid=%s;"
    
    cr.execute(sql, eid)
    print("course deleted successfully")
    db.commit()
    db.close()
    
