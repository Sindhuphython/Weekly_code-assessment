import smtplib
totalamount=0
while(True):
    print("MENU")
    print("1. Tea -Rs.7")
    print("2. Coffee -Rs.10")
    print("3. Masala Dosa -Rs.50")
    print("4. View Bill and Email") 
    choice=int(input("enter your choice: "))
    if choice==1:
        totalamount=totalamount+7
    elif choice==2:
        totalamount=totalamount+10
    elif choice==3:
        totalamount=totalamount+50
    elif choice==4:
        break
print (totalamount) 
message="total bill amount:"+str(totalamount) 
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("sindhubarathipython@gmail.com","984621@ss")
connection.sendmail("sindhubarathipython@gmail.com","sindhubarathiak@gmail.com",message)
connection.quit
print("mail sent successfully")