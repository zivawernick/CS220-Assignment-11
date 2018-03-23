# -*- coding: utf-8 -*-

"""
Created on Sun Mar 18 17:26:53 2018
@author: your name here
"""

import dbinterface

menuString = """
    Main Menu:
    1.  Search
    2.  Read
    3.  Create
    4.  Update
    5.  Delete 
    0.  Exit
"""
searchString = """
Search Menu:
    1. Search Employee Info
    2. Search Albums by artist
    0. Exit
"""
readString = """
Read Menu:
    1. Read Artist
    2. Read Genres
    3. Read Employees info
    4. Read Customer info
    0. Exit

createString = """
Create Menu:
    1. Create Employee
    2. Create Customer log in
    0. Exit
"""
updateString = """
Update Menu:
    1. Update Employee info
    2. Update Customer info
    0. Exit
"""
deleteString = """
Delete Menu:
    1. Delete Track
    2. Delete Invoice
    0. Exit
"""
def searchfunction():
    while True:
        print(searchString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            print("Unrecognized Command")
            #searchsubFunction()
        elif (sel == 2):
            print("Unrecognized Command")
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
    
def readfunction():
    while True:
        print(readString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            print("Unrecognized Command")
        elif (sel == 2):
            print("Unrecognized Command")
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")

def createfunction():
    while True:
        print(createString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            print("Unrecognized Command")
        elif (sel == 2):
            print("Unrecognized Command")
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")

def createfunction():
    while True:
        print(createString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            print("Unrecognized Command")
        elif (sel == 2):
            print("Unrecognized Command")
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
            
def updatefunction():
    while True:
        print(updateString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            print("Unrecognized Command")
        elif (sel == 2):
            print("Unrecognized Command")
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
            
def deletefunction():
    while True:
        print(deleteString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            deleteTrack()
        elif (sel == 2):
            deleteInvoice()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
            
#def searchsubFunction():
#    dbinterface.searchCustomers()
    


def main():

    while True:
        print(menuString)
        sel = int(input("Menu Option >> "))
        if(sel == 1):
            searchfunction()
        elif(sel == 2):
            readfunction()
        elif(sel == 3):
            createfunction()
        elif(sel == 4):
            updatefunction()
        elif(sel == 5):
            deletefunction()
        elif(sel == 0):
            # Exits the program
            break
        else:
            print("Unrecognized Command")
   
    
# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()