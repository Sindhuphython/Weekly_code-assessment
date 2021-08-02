import smtplib
r =0
c =0
m =0
class Che_Restaurant_Food_menu:
    def tea(self,a):
        return a*7
    def coffee(self,a):
        return a*10
    def masalaDosa(self,a):
        return a*50
    def add(self,r,c,m):
        return (r*7)+(c*10)+(m*50)
    

CRFM = Che_Restaurant_Food_menu()

while(True):
    print("Multiple selection from menu")
    print("1.Tea-Rs.7")
    print("2.Coffee-Rs.10")
    print("3.Masala Dosa-Rs.50")
    print("4.view Bill and Email")
    
    choice = int(input("enter your choice: "))

    if choice == 1 :
        
        print("You selected tea for Rs:7 ")
        r = int(input("enter how many tea : "))
        print(CRFM.tea(+r))
    
    if choice == 2:
        
        print("You selected coffee for Rs:10 ")
        c = int(input("enter how many coffee: "))
        print(CRFM.coffee(+c))
    
    if choice == 3:
        print("You selected Masala Dosa:RS.50 ")
        m = int(input("enter how many masaladosa: "))
        print(CRFM.masalaDosa(+m))

    if choice == 4:
        
        message = CRFM.add(r,c,m)
        print("total amount is : ",message)
        print("Thank you! For sending Bill details,Please enter your mail id")
        break   

    else:
        print("Choose next")

try:
    email_id = input("enter a valid email id: ")
    val3 = "r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if val3:
        print("valid email id")
    else:
        print("invalid id")
except:
    print("error in validation")

y = str(message)
w =f'''The amount for your choosen menu without GST :Rs {y} ,
        visit again!,
        Happy day! '''
connection = smtplib.SMTP ("smtp.gmail.com",587)
connection.starttls()
connection.login("chedivya1998@gmail.com","Welcome@2169")
connection.sendmail("chedviya1998@gmail.com",email_id,w)
print("email has sent successfully")
connection.quit()



