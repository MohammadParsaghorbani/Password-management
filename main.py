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
    print("choose an option :\n\t1) create a password\n\t2) check your info\n\t3) edit info\n\t4) exit")
    choise = input("your choice : ")
    if choise == "1":
        site = input("enter the site you want to make password for it: ")
        user_name= input(f"enter your user name in {site}: ")
        description = input("enter description for your password: ")
        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(password)
        file = open(f"{user_name}.txt" , "a")
        file.write(f"\n======================\nsite = {site}\nuser_name = {user_name}\ndescription = {description}\nlength of password = {length}\npassword = \n{password}")
        file.close()
    elif choise == "2":
        file = open(f"{user_name}.txt" , "r")
        content = file.read()
        print(content)
        print("="*22)
        file.close()
    elif choise == "3":
        file_path = input("enter your user name that you enter first: ")
        with open(f"{file_path}.txt") as file:
            print(file.read())
        def change(file_path,line,text):
            with open(f"{file_path}.txt") as file:
                lines = file.readlines()
            if (line <= len(lines)):

                lines[line - 1] = text + "\n"

                with open(f"{file_path}.txt" , "w") as file:
                    for i in lines:
                        file.write(i)
            else:
                print("not in file")
        line = int(input("line: "))
        text = input("text: ")
        change(file_path,line,text)
    elif choise == "4":
        print("good bye!")
        break
    else:
        print("invalid option")