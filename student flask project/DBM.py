import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='kalyani')
    
def addstud(t):
    db=getConnection()
    sql='insert into student values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllstud():
    db=getConnection()
    sql='select * from student'
    cr=db.cursor()
    cr.execute(sql)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist

    
def deletestud(roll_no):
    db=getConnection()
    sql='delete from  student where roll_no=%s'
    cr=db.cursor()
    cr.execute(sql,roll_no)
    db.commit()
    db.close()

def selectstudById(roll_no):
    db=getConnection()
    sql='select * from student where roll_no=%s'
    cr=db.cursor()
    cr.execute(sql,roll_no)
    slist=cr.fetchall()
    db.commit()
    db.close()
    return slist[0]

def updatestud(t):
    db=getConnection()
    sql='update student set name=%s,clg=%s,email=%s,age=%s,gender=%s where roll_no=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
