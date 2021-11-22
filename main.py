import sqlite3
from data import Data
import re as regex 
# regex for password checking

# Connection and cursor.

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# A bunch of functions to be used 


def create_user(user):
    with conn:
        cursor.execute("INSERT INTO database VALUES (:username, :password, :balance)", {"username": user.username, "password": user.password, "balance": user.balance})
        print ("Sucessfully created user.")



def check_login(username,password):
    # check if to see if it "logs in".
    x = ("Invalid .")
    cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {'username': username, 'password': password })
    info = cursor.fetchall()

    # searched up google on how to join a list (info) into a string so I can check it with an if statment if it hold any value.

    infoString = ' '.join(map(str,info))

    print(infoString, "this is the infoString")

    if infoString == "":
        return x , "this is x"
    elif infoString != "":
        cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {"username": username, "password": password })
        return cursor.fetchall() , "fetchall"

    # * FIXED *
    # !!!!! TRY IT AND SEE IF IT ACTUALLY WORKS AGAIN AND MAKE SURE IT'S NEAT AND READY

def check_registered(username):
    # chec if there a user wih that log in registered in the database. if there is return True if there isn't False and create user.
    # !!!! RETURNS TRUE OR FALSE !!!!!!
    cursor.execute("SELECT * FROM database WHERE username=:username", {"username": username})
    info = cursor.fetchall()
    info = ' '.join(map(str,info))

    if info != "":
        return True
    elif info == "":
        return False

def check_passwrod(password):
    # lentgh error for checking if the lentgh is below 8
    lentgh_er = len(password) < 8
    # digit check
    digit_er = regex.search(r"\d", password) is None 
    # search for upppercase
    upppercase_er = regex.search(r"[A-Z]", password ) is None
    # serach for lowercase 
    lowercase_er = regex.search(r"[a-z]", password) is None
    # search for symbl
    symbl_er = regex.search(r"[ !#$%&'()*+,-./[\]^_`{|}~"+r'"]', password) is None

    # result
    pass_ok = not (lentgh_er or digit_er or upppercase_er or lowercase_er or symbl_er )






user1 = Data("Darius", "password", 30000)
user2 = Data("steffy", "passwordy", 32000)

# print (check_login(user1.username,user2.password))

if check_registered("Darius") == True:
    print ("he's aight")
elif check_registered("alizein") == False: 
    print ("he aint vibin")
