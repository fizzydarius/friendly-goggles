import sqlite3
from data import Data

# Connection and cursor.

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# A bunch of functions to be used 


def create_user(user):
    with conn:
        cursor.execute("INSERT INTO database VALUES (:username, :password, :balance)", {"username": user.username, "password": user.password, "balance": user.balance})
        print ("Sucessfull")



def check_login(username,password):
    x = ("Invalid .")
    cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {'username': username, 'password': password })
    info = cursor.fetchall()

    # !!!!! Fix this please darius, come on now !!!!!!
    
    if info == "[]":
        return x + "ok"
    elif info != "[]":
        cursor.execute("SELECT * FROM database WHERE username=:username And password=:password ", {'username': username, 'password': password })
        return cursor.fetchall()



def get_user_info_by_username(username):
    cursor.execute("SELECT * FROM database WHERE username=:username", {'username': username})
    return cursor.fetchall()

user1 = Data("Darius", "password", 30000)
user2 = Data("steffy", "passwordy", 32000)


# turns the checks_login from a list into a string so it's easier to check if if string is empty .
# if empty, user does not exist ask user to make an account (or password wrong)
# if it retruns with value then the inputed username/password is correct.

list1 = (check_login(user1.username,user1.password))
string = ''.join(map(str,list1))

print (string)

