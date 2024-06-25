#source code for shop management system

#main
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd='',database="shop")
cur=db.cursor()
cur.execute("USE SHOP")

choice='y'

def custadd():
    cust_id=int(input("enter the customer id"))
    cust_name=input("enter the customer name")
    cust_phone=int(input("enter the phone no"))
    com="INSERT INTO CUSTOMER VALUES({},'{}',{})".format(cust_id,cust_name,cust_phone)
    cur.execute(com)
    
    db.commit()
    print("customer information added successfully")
def custdel():
    try:
     cust_id=int(input("enter the customer id you want to delete"))
     v="DELETE FROM CUSTOMER WHERE CUSTOMER_ID=%s"
     cur.execute(v,(cust_id,))
     db.commit()
     print("the user info has been successfully deleted")
    except:
        print("COULDNT FIND THE ID TO BE DELETED PLEASE CHECK AGAIN")
def custdisp():
    try:
     cust_name=input("enter the customer name")
     v="select * from CUSTOMER WHERE CUSTOMER_NAME=%s"
     cur.execute(v,(cust_name,))
     rec=cur.fetchone()
     print("customer details:")
     for i in rec:
        print(i,end='\t')
     print()
    except:
        print("THE NAME WAS NOT FOUND PLEASE CHECK AGAIN")

def custupd():
    try:
     upcust_id=int(input("enter the customer no of the customer to be upadated"))
     newcust_name=input("enter the updated customer name")
     newcust_phone=int(input("enter the updated phone number"))
     v="UPDATE CUSTOMER SET CUSTOMER_NAME='%s', CUSTOMER_PHONE=%s WHERE CUSTOMER_ID=%s" %(newcust_name,newcust_phone,upcust_id)
     cur.execute(v)
     db.commit()
     print("the information updated successfully")
    except:
        print("COULDNT FIND THE ID TO BE UPDATED")
def empadd():
    emp_id=int(input('enter the employee id'))
    emp_name=input("enter the name of the employee")
    emp_gen=input("enter the gender of the employee")
    emp_phone=int(input("enter the phone number of the employee"))
    cur.execute("insert into EMPLOYEE VALUES({},'{}','{}',{})".format(emp_id,emp_name,emp_gen,emp_phone))
    db.commit()
    print("employee information enetered auccessfully")
def empdel():
    try:
     emp_id=int(input("enter the employee id you want to delete"))
     v="DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID=%s"
     cur.execute(v,(emp_id,))
     db.commit()
     print("the empoyee data has been removed successfully")
    except:
        print("COULDNT FIND THE ID TO BE DELETED")
def empdisp():
    try:
     emp_name=input("enter the employee name")
     v="SELECT * FROM EMPLOYEE WHERE EMPLOYEE_NAME=%s"
     cur.execute(v,(emp_name,))
     res=cur.fetchone()
     for i in res:
        print(i,end='\t')
     print()
    except:
     print("EMPLOYEE NAME DOESNT EXIST")
def empupdate():
    try:
     emp_id=int(input("enter the id of the employee whose information has to be updated"))
     newemp_name=input("enter the corrected name(if any)")
     newemp_gen=input("enter the gender of the employee")
     newemp_phone=int(input("enter the updated phone number"))
     v="UPDATE EMPLOYEE SET EMPLOYEE_NAME='%s',EMPLOYEE_GENDER='%s',EMPLOYEE_PHONE=%s WHERE EMPLOYEE_ID=%s"%(newemp_name,newemp_gen,newemp_phone,emp_id)
     cur.execute(v)
     db.commit()
     print("information successfully updated")
    except:
        print("THE EMPLOYEE ID DOESNT EXIST")
def prodadd():
    prod_id=int(input("enter the product id"))
    prod_name=input("enter the product name")
    prod_stock=int(input("enter the stock left"))
    prod_price=float(input("enter the price of the product"))
    brand=input("enter the brand")
    cur.execute("insert into PRODUCTS VALUES({},'{}',{},{},'{}')".format(prod_id,prod_name,prod_stock,prod_price,brand))
    db.commit()
    print("info added successfully")
def proddisp():
    try:
     prod_name=input("enter the product name")
     v="SELECT PRODUCT_NO,PRODUCT_NAME,STOCK_LEFT,BRAND FROM PRODUCTS WHERE PRODUCT_NAME=%s"

     cur.execute(v,(prod_name,))
     outp=cur.fetchall()
     for i in outp:
        print(i,end='\t')
        
     print()
    except:
        print('PRODUCT DOESNT EXIST')
def produpdate():
    try:
     prod_id=int(input("enter the product id of the product to be updated"))
     newprod_name=input("enter the new product name")
     newprod_stock=int(input("enter the new stock left of the product"))
     newprod_price=int(input("enter the updated price of the product"))
     new_brand=input("enter the updated brand")
     v="UPDATE PRODUCTS SET PRODUCT_NAME='%s',STOCK_LEFT=%s,PRODUCT_PRICE=%s,BRAND='%s' WHERE PRODUCT_NO=%s" %(newprod_name,newprod_stock,newprod_price,new_brand,prod_id)
     cur.execute(v)
     db.commit()
     print("updated product information successfully")
    except:
        print("THE PRODUCT ID DOESNT EXIST")
while choice=="y" or choice=='Y':
    print("1.enter a new customer information")
    print("2.update a customer information")
    print("3.delete a customer information")
    print("4.display a customer information")
    print("5.add a new employee information")
    print("6.update a employee information")
    print("7.delete a employee information")
    print("8.dislpay an employee information")
    
    print("9.add a product information")
    print("10.update a product information")
    print("11.show  a product information")
    opt=int(input("enter your choice"))

    if opt==1:
        custadd()
    elif opt==2:
        custupd()
    elif opt==3:
        custdel()
    elif opt==4:
        custdisp()
    elif opt==5:
        empadd()
    elif opt==6:
        empupdate()
    elif opt==7:
        empdel()
    elif opt==8:
        empdisp()
    elif opt==9:
        prodadd()
    elif opt==10:
        produpdate()
    elif opt==11:
        proddisp()
    else:
        print("wrong option")
    choice=input('do you want to continue?')

cur.close()
db.close()
  


