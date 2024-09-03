import random
import string

lower = string.ascii_lowercase
uppper = string.ascii_uppercase
# print(uppper)
# print(string.ascii_letters)
symbols = "!@#$%^&*()-+[]{}"
numbers = "0123456789"
all = lower + uppper + symbols + numbers

while True:
    print("choose an option :\n\t1) create a password\n\t2) check all of your passwords\n\t3) exit")
    choise = input("your choice : ")
    if choise == "1":
        site = input("enter the site you want to make password for it: ")
        user_name= input(f"enter your user name in {site}: ")
        description = input("enter description for your password: ")
        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(password)
        file = open("password.txt" , "a")
        file.write(f"\n======================\nsite = {site}\nuser_name = {user_name}\ndescription = {description}\nlength of password = {length}\npassword = {password}")
        file.close()
    elif choise == "2":
        file = open("password.txt" , "r")
        content = file.read()
        print(content)
        print("="*22)
        file.close()
    elif choise == "3":
        print("good bye!")
        break
    else:
        print("invalid option")