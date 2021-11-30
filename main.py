import sqlite3
from data import Data
import re as regex
# from sqlite3.dbapi2 import register_converter was made by itself????????????????????????????? CRAZY
# Connection and cursor.


# A bunch of functions used for the log-in phase.
class login():
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_user(self,user):
        # takes input from the information in a tuple when it's run through Data(username,password,balance)
        with self.conn:
            self.cursor.execute("INSERT INTO database VALUES (:username, :password, :balance)", {"username": user.username, "password": user.password, "balance": user.balance})
            print ("Sucessfully created user.")

    def check_login(self,username,password):
        # check if to see if it "logs in".
        self.cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {'username': username, 'password': password })
        info = self.cursor.fetchall()
        # searched up google on how to join a list (info) into a string so I can check it with an if statment if it hold any value.
        infoString = ' '.join(map(str,info))

        if infoString == "":
            return False
        elif infoString != "":
            self.cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {"username": username, "password": password })
            return True

    def check_registered(self,username):
        # chec if there a user wih that log in registered in the database. if there is return True if there isn't False and create user.
        # !!!! RETURNS TRUE OR FALSE !!!!!!
        self.cursor.execute("SELECT * FROM database WHERE username=:username", {"username": username})
        info = self.cursor.fetchall()
        info = ' '.join(map(str,info))

        if info != "":
            return True
        elif info == "":
            return False


    def check_passwrod(self,password):
        # Using regex checks wether the string password has the correct lentgh, digits, uppercase characters, lowecase characters and special characters.
        # If it doesn't , It adds 1 to a counter which indicates whether a comma should be placed or not and adds what is needed to a string named "rtrn_list"

        rtrn_list = "Your password is weak, please add: "
        counter_err = 0 
        # lentgh error for checking if the lentgh is below 8
        lentgh_er = len(password) < 8
        if lentgh_er == True: 
            rtrn_list = rtrn_list + "More Characters"
            counter_err = counter_err + 1
        # digit check
        digit_er = regex.search(r"\d", password) is None 
        if counter_err >= 1:
            rtrn_list = rtrn_list + ","
        if digit_er == True: 
            rtrn_list = rtrn_list + "Numbers"
            counter_err = counter_err + 1
        # search for upppercase
        upppercase_er = regex.search(r"[A-Z]", password ) is None
        if counter_err > 1:
            rtrn_list = rtrn_list + ","
        if upppercase_er == True: 
            rtrn_list = rtrn_list + "Uppercase characters"
            counter_err = counter_err + 1
        # serach for lowercase 
        lowercase_er = regex.search(r"[a-z]", password) is None
        if counter_err > 1:
            rtrn_list = rtrn_list + ","
        if lowercase_er == True: 
            rtrn_list = rtrn_list + "Lowercase characters"
            counter_err = counter_err + 1
        # search for symbl
        symbl_er = regex.search(r"[ !#$%&'()*+,-./[\]^_`{|}~"+r'"]', password) is None
        if counter_err > 1:
            rtrn_list = rtrn_list + ","
        if symbl_er == True: 
            rtrn_list = rtrn_list + "Special Characters"
            counter_err = counter_err + 1
        # result
        pass_ok = not (lentgh_er or digit_er or upppercase_er or lowercase_er or symbl_er )

  
        if pass_ok == True:
            return "Password is great!"
        elif pass_ok == False:
            comma = ","
            s_p = rtrn_list.rindex(comma)
            rtrn_list = rtrn_list[:s_p-1] + " and " + rtrn_list[s_p+1:]
            return rtrn_list

    def check_password_crack(self,password):
        print ("siuu")

user1 = Data("Darius", "password", 30000)
user2 = Data("steffy", "passwordy", 32000)

SystemLogin = login()
print (SystemLogin.check_passwrod("rah"))
