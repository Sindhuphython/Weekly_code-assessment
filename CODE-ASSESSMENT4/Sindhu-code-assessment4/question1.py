#CRUD Create,Retrieve,Update and Delete
import pymongo
import re,logging,smtplib
client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client['BlooddonationDb']
collection_name=mydatabase['Blooddonation1']
donorlist=[]
dict1={}
try:
    def validate(vname,vaddress,vmobile_number,vplace):
        valname=re.search("^[A-Z]{1}[A-Z]{0,25}$",vname)
        valaddress=re.search("^[A-Z]{1}[A-Z]{0,200}$",vaddress)
        valmobile_number=re.search("^[7-9][0-9]{9}$",str(vmobile_number))
        valplace=re.search("^[A-Z]{1}[A-Z]{0,25}$",vplace)
        print(valname,valaddress,valmobile_number,valplace)
        if valname and valaddress  and valmobile_number and valplace :
            return True
        else:
            return False

    class BloodBankManagement:
        def addblooddonordetails(self,name,address,pincode,blood_group,mobile_number,last_donated_date,place,email):
            dict1 = {"name":name, "address":address,"pincode":pincode,"blood_group":blood_group,"email":email, "mobile_number":blood_group,"last_donated_date":last_donated_date,"place":place}
            result=collection_name.insert_one(dict1)
            print(result)
            return dict1

    obj = BloodBankManagement()
    while True:
        print("1)Add donor details :")
        print("2)Search donors based on blood group:")
        print("3)Search donors on blood group and place :")
        print("4)Update all the donor details with their mobile number :")
        print("5)Delete the donor using mobile number")
        print("6)Display the total number of donors on each blood group:")
        print("7)Immediate notification to all via email:")
        print("8)Exit:")
        choice =int(input("Enter your option : "))
        if(choice==1):
            name=input("Enter the donor name:")
            address=input("Enter the donor address:")
            pincode=int(input("Enter the pincode of the donor:"))
            blood_group=input("Enter the donor bloodgroup:")
            mobile_number=int(input("Enter the mobileno:"))
            last_donated_date=input("Enter the lastdonateddate:")
            email=input("Enter the emailid:")
            place=input("Enter the place:")
            if validate(name,address,mobile_number,place):
                obj =BloodBankManagement()
                donorlist.append(obj.addblooddonordetails(name,address,pincode,blood_group,mobile_number,last_donated_date,place,email))
            else:
                logging.error("invalid data enter a valid data")
        if(choice == 2):
            blood_group1 = input("Enter the blood group of the donor to search : ")
            result=collection_name.find({'blood_group':blood_group1})
            for i in result:
                print(i)
        if(choice==3):
            blood_group=input("Enter the blood group of the donor to search:")
            place=input("Enter the place of the donor to search:")
            result=collection_name.find({'blood_group':blood_group,'place':place})
            for i in result:
                print(i)
        if(choice==4):
            name=input("Enter the donor name")
            mobile_number=input("Enter the mobile number of donor to update : ")
            result=collection_name.update_one({"name":name},{"$set":{"mobile_number":mobile_number}})
            print(result)
            
        if(choice==5):
            mobile_number=input("Enter the donor mobile number :")
            result=collection_name.delete_many({"mobile_number":mobile_number})
            print(result)
            
        if(choice==6):
            result=collection_name.aggregate([{"$group":{"_id":"$bloodgroup","no_of_donors":{"$sum":1}}}])
            for i in result:
                print(i)

        if(choice==7):
            result=collection_name.find()
            print(result)
            for i in result:
                print(i['email'])
                message="immediately want A+ blood group in XYZ hospital"
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("sindhubarathipython@gmail.com","984621@ss")
                connection.sendmail("sindhubarathipython@gmail.com",i['email'],message)
                connection.quit
                print("Mail sent")
        if(choice==8):
            break
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")        






