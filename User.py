class User:
 def __init__(self, name, email_address, drivers_license_number):
    self.name = name
    self.email_address = email_address
    self.drivers_license_number = drivers_license_number
 
 def __str__(self):
    return f"User: {self.name}, email_address: {self.email_address}, drivers_license_number: {self.drivers_license_number}"


  
User1 = User(name="Cricket",email_address="heinhaung91@gmail.com",drivers_license_number=12345)
User2 = User("SuperMan","Superduper@gmail.com",3456)
print (User1)
print(User2)

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



               