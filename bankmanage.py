import mysql.connector as a
con= a.connect(host="localhost",user="root",passwd="Vipin@1299",database="bank")
print("=========================================================================!Welcome to Youth Bank!=======================================================================")

print("Connection to Server!!!!! SUCCESS")

def openAcc():
    name=input("Enter Name :")
    account=input("Enter Account number :")
    dob=input("Enter D.O.B :")
    phone=input("Enter Phone: ")
    address=input("Enter Address :")
    OpenBal=int(input("Enter Opening Balance: "))

    data1=[name,account,dob,phone,address,OpenBal]
    data2=[name,account,OpenBal]

    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'

    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("DATA ENTERED SUCESSFULLY")
    main()

def depositAmo():
    amount=int(input("Enter Amount: "))
    account=input("Enter Account No: ")
    sql1="select balance from amount where account_no=%s"

    data=[account]
    c=con.cursor()
    c.execute(sql1,data)

    myresult=c.fetchone()
    if(myresult is None):
        print("Sorry!!!!Can't Deposit Money account no:",account,"does not exist")
    else:
        tam=myresult[0]+amount

        sql2="update amount set balance=%s where account_no=%s"

        d=[tam,account]
        c.execute(sql2,d)
        con.commit()
        print(" Deposited successfully, Updated amount is ",tam)
    main()

def withdrawAmo():
    amount=int(input("Enter Amount : "))
    account=input("Enter Account Number :")
    a="select balance from amount where account_no=%s"

    data=[account]
    c=con.cursor()
    c.execute(a,data)

    myresult=c.fetchone()
    if(myresult is None):
        print("Sorry!!!! Can't Withdraw Money account no:",account,"does not exist")
    else:
        tam=myresult[0]-amount
        sql="update amount set balance=%s where account_no=%s"
        d=[tam,account]
        c.execute(sql,d)
        con.commit()
        print(" Your current amount is", tam)
    main()

def balance():
    account=input("Enter Account number :")
    a="select balance from amount where account_no=%s"

    data=[account]
    c=con.cursor()
    c.execute(a,data)

    myresult=c.fetchone()
    if(myresult is None):
        print("Sorry!!!! Can't Check Balance, account no:",account,"does not exist")
    else:
        print("Balance for Account :",account,"is",myresult[0])
    main()


def displayacc():
    account=input("Enter Account Number :")
    a="select * from account where account_no=%s"

    data=[account]
    c=con.cursor()
    c.execute(a,data)
    
    myresult=c.fetchone()
    if(myresult is None):
        print("Sorry!!!! account no:",account,"does not exist")
    else:
        result=list(myresult)
        print("Name:",result[0])
        print("Account no:",result[1])
        print("DOB:",result[2])
        print("phone no:",result[3])
        print("Address:",result[4])
        print("Opening Balance:",result[5])
    main()

def closeac():
    account=input("Enter Account number :")
    a="select * from account where account_no=%s"
    data1=[account]
    c1=con.cursor()
    c1.execute(a,data1)
    myresult=c1.fetchone()
    if(myresult is None):
        print("Sorry!!!! account no:",account,"does not exist.Please try Again!!!!")
    else:
        sql1="delete from account where account_no=%s"
        sql2="delete from amount where account_no=%s"
        data=[account]
        c=con.cursor()
        c.execute(sql1,data)
        c.execute(sql2,data)
        con.commit()
        print("""Your Account is successfully closed!!!
        Thanks for using our service""")
    main()

def main():
    print("""
    1.  OPEN NEW ACCOUNT
    2.  DEPOSIT AMOUNT
    3.  WITHDRAW AMOUNT
    4.  BALANCE ENQUIRY
    5.  DISPLAY CUSTOMER DETAILS
    6.  CLOSE AN AMOUNT
    7.  EXIT THE APPLICATION
    """)

    choice=input("Enter Task Number :")
    while True:
        if(choice=='1'):
            openAcc()
        elif(choice=='2'):
            depositAmo()
        elif(choice=='3'):
            withdrawAmo()
        elif(choice=='4'):
            balance()
        elif(choice=='5'):
            displayacc()
        elif(choice=='6'):
            closeac()
        elif(choice=='7'):
            print("")
            print("")
            print("")
            print("")
            print("====================Thanks for using Youth Bank Service====================")
            exit(0)
        else:
            print("Wrong choice............")
        main()
main()



































