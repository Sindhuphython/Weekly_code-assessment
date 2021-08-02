import re
import smtplib


while(True):
    name=input("Please Enter Customer Name :")
    email=input("Please Enter the Customer Email Id :")
    reg = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    val=re.match(reg,email)
    if val:   #if only the details are valid then only the other things run
        class Tea_pricing:  
            def price_tea(self):
                self.tea_p=7
                return self.tea_p
        class Coffee_pricing:
            def price_coffee(self):
                self.coffe_p=10 
                return self.coffe_p
        class Masala_Dosa_pricing:
            def price_dosa(self):
                self.dosa_p=50
                return self.dosa_p

        class Bill_of_Order(Coffee_pricing,Tea_pricing,Masala_Dosa_pricing): #class derived from above three orders
            pass

        billing=Bill_of_Order()
        c=0

        while(True): #menudriven concept for choosing options for order

            print("\nSelect an option from menu ")
            
            print("1. Tea (Rs.7)")
            print("2. Coffee (Rs.10)")
            print("3. Masala Dosa (Rs.50)")
            print("4. View Bill and Email ")
            choice=int(input("Enter your Order choice: "))
            if choice==1:
                print("Tea selected")
                tea=billing.price_tea()
                c+=tea
            if choice==2:
                print("Coffee selected")
                cofp=billing.price_coffee()
                c+=cofp
            if choice==3:
                print("Masala Dosa Selected")
                dosa=billing.price_dosa()
                c+=dosa
            if choice==4:
                print("Your bill is Rs :",c)
    
                cost=str(c)
                connection=smtplib.SMTP("smtp.gmail.com",587)  #sending email to user
                connection.starttls()
                connection.login("hariompateldada@gmail.com","Sparsh@01")
                connection.sendmail("hariompateldada@gmail.com",email,cost)

                print("Email for your bill successfully sent")
                connection.quit()
                break
        break          
    else:
        print("Please Enter a valid Email ID")
        continue


    