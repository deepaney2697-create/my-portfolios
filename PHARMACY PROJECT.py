                                                                #PHARMACY MANGEMENT SYSTEM#
import mysql.connector
print("-------------------------------PHARMACY_MANAGEMENT_SYSTEM-----------------------------------")

                                                                        #ADD_DRUGS#
def ADD_DRUGS():
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    while True:
        sno=int(input("ENTER S_NO:"))
        pid=input("ENTER prescription_ID:")
        bno=int(input("ENTER batch_no:"))
        dno=input("ENTER Drug name:")
        cno=input("Enter company name:")
        typ=input("Enter quality:")
        use=input("Enter use:")
        pri=int(input("enter price:"))
        qty=int(input("enter quantity"))
        query="insert into MEDICINE values({},'{}',{},'{}','{}','{}','{}',{},{})".format(sno,pid,bno,dno,cno,typ,use,pri,qty)
        c.execute(query)
        db.commit()
        print("Drug data added succefully!!!!!")
        ch=input("DO YOU WANT TO ENTER MORE RECORD?(Y/N)")
        if ch=='N':
            break


                                                                     #ADD ORDERED DRUGS#
def ADD_ORDERED_DRUGS():
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    while True:
        oid=int(input("ENTER ORDER ID:"))
        dn=input("ENTER Drug name")
        dt=input("ENTER drug type")
        oq=int(input("enter quantity"))
        p=int(input("ENTER price"))
        cn=input("CUSTOMER NAME")
        con=int(input("enter Contact no"))
        a=input("enter adddress")
        query="INSERT INTO ORDERS VALUES({},'{}','{}',{},{},'{}',{},'{}')".format(oid,dn,dt,oq,p,cn,con,a)
        c.execute(query)
        db.commit()
        print("order inserted succesfully......")
        print("-------------------~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-----------------------")
        ch=input("DO YOU WANT TO ENTER MORE RECORD?(Y/N)")
        if ch=='N':
            break
                                                                       #ORDERED DRUGS#


def ORDERED_DRUGS():
    print("------ ORDER DETAILS-----")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("select * from orders")
    d=c.fetchall()
    for i in d:
        print("-------------------~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-------------------------")
        print("ORDER ID:",i[0])
        print("DRUG NAME:",i[1])
        print("DRUG TYPE:",i[2])
        print("DRUG QUANTITY",i[3])
        print("PRICE",i[4])
        print("CUSTOMER NAME",i[5])
        print("PRIVATE NO.",i[6])
        print("ADDRESS",i[7])
        print("-----------~~~~~~~~~~~~~~~~~~~~~THANKS FOR ORDER!!!!!!!------------------------")
        db.commit()

                                                  #STOCK#
def CHECK_STOCK():
    print("--------------------STOCK DETAILS--------------------------------")
    i=input("Enter keyword to see stock details:")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("SELECT * FROM MEDICINE")
    m=c.fetchall()
    for i in m:
        print("----------------------------------------------------------------")
        print("Serial no:",i[0])
        print("Drug name:",i[3])
        print("Batch no.:",i[2])
        print("Stock:",i[8])
        print("PRICE;",i[7])
    print("-----------------------------------------------------------------")
    db.commit()
                                                 #ADD EMPLOYEEE#
def ADD_EMPLOYEE():
    print("---------------------------------------------------------------------")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    while True:
        eid=int(input("ENTER Employee ID:"))
        en=input("ENTER Employee name:")
        r=input("POST:")
        s=int(input("enter salary"))
        pno=int(input("ENTER phone no:"))
        ad=input("ENTER address of employee:")
        query="insert into employee values({},'{}','{}',{},{},'{}')".format(eid,en,r,s,pno,ad)
        c.execute(query)
        db.commit()
        print("DATA INSERTED SUCCESFULLY......")
        print("----------------------------------------------------------------------")
        ch=input("DO YOU WANT TO ENTER MORE RECORD?(Y/N)")
        if ch=='N':
            break
                                                     #EMPLOYEEE#
def EMPLOYEE():
    print("----------------EMPLOYEE DETAIL-------------------")
    i=input("enter keyword to employee:")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("SELECT * FROM EMPLOYEE")
    p=c.fetchall()
    for i in p:
        print("----------------------------------------------------------")
        print("EMPLOYEE ID:",i[0])
        print("EMPLOYEE NAME:",i[1])
        print("POST:",i[2])
        print("SALARY:",i[3])
        print("PHONE NO.:",i[4])
        print("ADDRESS:",i[5])
        print("-----------------------------------------------------------------")
        db.commit()


                                                   #ADD CUSTOMER#
def ADD_CUSTOMER():
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    while True:
        print("------------------------ADD CUSTOMER-----------------------")
        SNO=int(input("enter serial no:"))
        cna=input("enter customer name")
        PNO=int(input("ENTER CONTACT  NO:"))
        add=input("Enter address")
        detail="insert into customer values({},'{}',{},'{}')".format(SNO,cna,PNO,add)
        c.execute(detail)
        db.commit()
        print("-----DATA REGISTERED SUCCESFULLY-----")
        print("---------------------------------------------------------------")
        ch=input("DO YOU WANT TO ENTER MORE RECORD?(Y/N)")
        if ch=='N':
            break

                                                      #CUSTOMER#
def CUSTOMER():
    print("----------------------------------------------------------------------")
    l=input("enter keyword to customer")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("select * from customer where cust_name like'%{}%'".format(l))
    e=c.fetchall()
    for i in e:
        print("----------------------------------------------")
        print("serial no:",i[0])
        print("Customer name:",i[1])
        print("PHoNE NO:",i[2])
        print("address of customer:",i[3])
    db.commit()
              
                                                   #SEARCH_MEDICINE#
def MEDICINE():
    print("---------SEARCH DETAILS-------------------")
    k=input("enter keyword to search medicine:")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("SELECT * from medicine where drug like'%{}%'".format(k))
    a=c.fetchall()
    for i in a:
        print("------------------------------------------")
        print("BATCH NO:",i[2])
        print("DRUG NAME:",i[3])
        print("COMPANY NAME",i[4])
        print("----------------------------------------------")
        db.commit()

                                                # BUY MEDICINE#
def BUY_MEDICINE():
    print("----------------MEDICINE DETAILS----------------")
    n=input("ENTER DRUG NAME:")
    db=mysql.connector.connect(host="localhost",user="root",password="ghz1210",database="pharmacy")
    c=db.cursor()
    c.execute("select * from medicine where drug like'%{}%'".format(n))
    e=c.fetchall()
    for i in e:
        print("-----------------------------------------------")
        print("serial no:",i[0])
        print("prescription id:",i[1])
        print("drug_name",i[3])
        print("price;",i[7])
        db.commit()

                                                     #ADMIN#       
def ADMIN():
    print("----------~~~~~~~~~~~~~~ADMIN MENU~~~~~~~~~~~~~----------")
    print("---------------------------------------------------------")
    while True:
        print("----------------~~~~~~~~~~~~~~~~~~~~----------------")
        print("1.ADD DRUGS")
        print("2.ADD ORDERED DRUGS")
        print("3.ORDERED DRUGS")
        print("4.STOCK")
        print("5.ADD EMPLOYEE")
        print("6.EMPLOYEE")
        print("7.ADD CUSTOMER")
        print("8.CUSTOMER")
        print("9.EXIT")
        print("------------~~~~~~~thank you~~~~~------------")
        ch=int(input("ENTER  YOUR CHOICE-"))
        print("------------------------------------------------------")
        if ch==1:
            ADD_DRUGS()
        elif ch==2:
             ADD_ORDERED_DRUGS()
        elif ch==3:
            ORDERED_DRUGS()
        elif ch==4:
            CHECK_STOCK()
        elif ch==5:
             ADD_EMPLOYEE()
        elif ch==6:
            EMPLOYEE()
        elif ch==7:
            ADD_CUSTOMER()
        elif ch==8:
            CUSTOMER()
        elif ch==9:
            break
            
        




        

                                                     #USER#
def USER():
    print("------------------USER MENU--------------------------")
    while True:
        print("1.SEARCH MEDICINE:")
        print("2.BUY MEDICINE:")
        print("3.EXIT:")
        print("-----------'''''''THANK YOU''''-------------")
        print("------------~~~~~~~~~~~~~~~~~~~~~~~~---------")
        ch=int(input("ENTER  YOUR CHOICE-"))
        print("------------------------------------------------------")
        if ch==1:
            MEDICINE()
        elif ch==2:
             BUY_MEDICINE()
        elif ch==3:
            break

    
while True:
    print("--------~~~~~~~~~~~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~~~~~~---------------")
    print("~~~~~~~~~~~~~~~~~~~~PHARMACY MANAGEMENT SYSTEM~~~~~~~~~~~~")
    print("1.ADMIN:")
    print("2.USER:")
    print("3.exit:-")
    print("-------------------THANK YOU------------------")
    ch=int(input("ENTER WHO ARE YOU--"))
    print("------------------------------------------------------")
    if ch==1:
            ADMIN()
    elif ch==2:
            USER()
    elif ch==3:
            break
    
        
    
    
    
        
    
    
        
        
        
    
    


























    
        
        
