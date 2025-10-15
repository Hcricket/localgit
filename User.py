class User:
       def __init__ (self,name,email_address,driver_licence_number):
         self.name = name 
         self.email_address = email_address
         self.driver_licence_number = driver_licence_number
       def __str__(self):
         return f"User:{self.name},Email:(self.email_address),Licence{self.driver_licence_number}" 
User1 = User("HeinHtetAung","hein.123@gmail.com",1242342543)    
User2 = User("CRICKEt","michaelpayit@gmail.com",234234132)       
User3 = User("Phwarlay","Phwarlay@gmail.com",9843889)
print(User1)
print(User2)
print(User3)







# class User:
#     def __init__(self, name, email_address, drivers_license_number):
#         self.name = name
#         self.email_address = email_address
#         self.drivers_license_number = drivers_license_number

#     def __str__(self):
#         return f"User: {self.name}, Email: {self.email_address}, License: {self.drivers_license_number}"

# User1 = User("Cricket", "heinhaung91@gmail.com", 12345)
# User2 = User("SuperMan", "Superduper@gmail.com", 3456)

# print(User1) 
# print(User2)



               