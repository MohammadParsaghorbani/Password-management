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
        while True:
            try:
                user_name= input(f"enter your user name in {site}: ")
                f = open(f"{user_name}.txt")
                print("this user name is already taken!")
                f.close()
            except IOError:
                print("nice!")
                break
        description = input("enter description for your password: ")
        length = int(input("enter the password length : "))
        password = "".join(random.sample(all, length))
        print(password)
        file = open(f"{user_name}.txt" , "a")
        file.write(f"======================\nsite = \n{site}\n---\nuser_name = \n{user_name}\n---\ndescription = \n{description}\n---\nlength of password = \n{length}\n---\npassword = \n{password}\n")
        file.close()
    elif choise == "2":
        while True:
            file_path = input("enter your user name that you enter first: ")
            try:
                file = open(f"{file_path}.txt")
                print("nice!")
                break
            except IOError:
                print("no file with this name")
        content = file.read()
        print(content)
        print("="*22)
        file.close()
    elif choise == "3":
        # file_path = input("enter your user name that you enter first: ")
        while True:
            file_path = input("enter your user name that you enter first: ")
            try:
                file = open(f"{file_path}.txt")
                print("nice!")
                break
            except IOError:
                print("no file with this name")
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