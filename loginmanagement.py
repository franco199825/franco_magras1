# WE CREATE A USERS LIST AND A PASSWORD LIST 

users_list = [ "fede.c", "franco.c", "lee.h", "bob.j", "julian.a", "chris.j", "giulia.m", "ashley.t", "maria.d"]
passwords_list = ["1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"]

# WE ASK THE USER TO ENTER THEIR DETAILS TO GAIN ACCESS

user_log = input("enter your username: ")
password_log = input("enter your password: ")

# WE USE DEF FUNCTION TO GET THE USER AND PASSWORD RIGHT

def loggin(user_log, password_log):
    if user_log in users_list:
        users_index = users_list.index(user_log)
        if password_log == passwords_list[users_index]:
            print("login successfully")      
        else:
            print("incorrect password, please try again")
            exit    

    else:
        print("username not found")
        exit

loggin(user_log , password_log)  

# NOW WE NEED TO CHOOSE A NEW PASSWORD FOR THE ACCOUNT 

new_password = input("do you want to change your password?: " )

def change_pwd(new_password):
    if new_password == "yes":
        new_pwd = input("type your new password: ")
        if user_log in users_list:
            users_index = users_list.index(user_log)
            passwords_list[users_index] = new_pwd
            print(f"password for {user_log} has been change successfully")
    else:
        print("")
        exit


change_pwd(new_password)        

print(passwords_list)      
