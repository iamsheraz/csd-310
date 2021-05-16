#Muhammad Tariq
#May 15th, 2021
#Assignment whatabook
#https://github.com/iamsheraz/csd-310

import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

""" DISPLAY BOOK LISTINGS METHOD """
def displayBooks(_cursor):

   
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    print("\n -- BOOK LISTINGS --\n")
    for i in books:
        print(f" Book Name: {i[1]}\n Book Author: {i[2]}\n Book Details: {i[3]}\n")

""" DISPLAY MAIN MENU """
def displayMenu():

    print("\n -- WHATABOOK --")
    print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")

    # Array
    mainMenuOptions = ["1", "2", "3", "4"]
    choice = input(" PLEASE ENTER THE NUMBER FOR SELECTION! ")
    while choice not in mainMenuOptions:
        print("\n** INVALID SELECTION: **")
        print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Exit Program\n")
        choice = input(" PLEASE ENTER THE NUMBER FOR SELECTION! ")
     

    if choice in mainMenuOptions:
        validChoice = int(choice)
        return validChoice
    
def displayLocations(_cursor):

    
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()
    print("\n -- CURRENT STORE LOCATIONS -- \n")
    for i in stores:
        print(f" Location: {i[1]}\n")

def validateUser():

    print("\n -- ACCOUNT LOGIN --\n")

    
    validUserIds = ["1", "2", "3"]
    userID = input("PLEASE ENTER YOUR USER ID: ")
    while userID not in validUserIds:
        print("\n** INVALID USER ID. **\n")
        userID = input("PLEASE ENTER YOUR USER ID: ")
    
    if userID in validUserIds:
        validUserID = int(userID)
        return userID

""" DISPLAYING USER ACCOUNT MENU METHOD """
def displayAccountMenu():

    print("\n-- ACCOUNT MAIN MENU --\n")
    print(" 1. Show Wishlist\n 2. Add A Book To Your Wishlist\n 3. Main Menu\n 4. Exit Program\n")

    
    validAccountOptions = ["1", "2", "3", "4"]
    accountOptions = input("\n PLEASE ENTER THE NUMBER FOR SELECTION! ")

    
    while accountOptions not in validAccountOptions:
        print("\n** INVALID SELECTION: **")
        accountOptions = input("\n PLEASE ENTER THE NUMBER FOR SELECTION! ")
    
    if accountOptions in validAccountOptions:
        validAccountOption = int(accountOptions)
        return validAccountOption

def displayBooksToAdd(_cursor, _user_id):

     
    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
         
    _cursor.execute(availableBooks)
    booksThatCanBeAdded = _cursor.fetchall()

    print("\n -- BOOKS THAT CAN BE ADDED -- \n")
    for i in booksThatCanBeAdded:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    
""" ADDING BOOK TO WISHLIST METHOD """
def addBookToWishlist(_cursor, _user_id, _book_id):

    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, addBookID))

""" DISPLAYING USER WISHLIST METHOD """
def displayWishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()


    print("\n -- YOUR WISHLIST BOOKS --\n")
    for i in wishlist:
        print(f" Book Name: {i[4]}\n Author: {i[5]}\n")



try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) 
    # connect to the pysports database   
    cursor = db.cursor()
    print("\n WELCOME TO WHATABOOK! ")
    mainMenuSelection = displayMenu()
    while mainMenuSelection < 4:
        
        if mainMenuSelection == 1:
            displayBooks(cursor)    
        if mainMenuSelection == 2:
            displayLocations(cursor)         
        if mainMenuSelection == 3:
            myID = validateUser()
            accountOption = displayAccountMenu()
            while accountOption != 3:
                if accountOption == 1:
                    displayWishlist(cursor, myID)                       
                if accountOption == 2:
                    displayBooksToAdd(cursor, myID)
                    addBookID = input("\nEnter the Book ID you want to add to your wishlist! ")
                    validBookID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while addBookID not in validBookID:
                        print("\n** Invlaid Book ID. Please try again! **")
                        addBookID = input("\nEnter the Book ID you want to add to your wishlist! ")
                    if addBookID in validBookID:
                        validBookID = int(addBookID)
                    addBookToWishlist(cursor, myID, validBookID)
                    db.commit()
                    print("\nYour Book was added successfully!")
                if accountOption == 4:
                    print("\nProgram Terminated....")
                    sys.exit()
                accountOption = displayAccountMenu()
            
        mainMenuSelection = displayMenu()
        if mainMenuSelection == 4:
            print("\nProgram Terminated....")
            sys.exit()
      

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
