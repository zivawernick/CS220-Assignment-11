# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:26:53 2018

@author: your name here
"""
import dbinterface

menuString = """
Main Menu:
1.  List customers
2.  Search customers
0.  Exit
"""
searchString = """
Search Menu:
    1. Search Employee Info
    2. Search Albums by artist
    3. Exit
"""
readString = """
Read Menu:
    1. Read Artist
    2. Read Genres
    3. Exit
"""

def myfunction():
    while True:
        print(searchString)
        sel = int(input("SubMenu Options >> "))
        if (sel == 1):
            searchsubFunction()
        elif (sel == 2):
            searchsubFunction2()
        elif (sel == 0):
            break
        else:
            print("Unrecognized Command")
    #dbinterface.listCustomers()
    
#def function2():
#        while True:
#            print(searchString)
#            sel = int(input("SubMenu Options >> "))
#            if (sel == 1):
#                searchsubFunction()
#            elif (sel == 2):
#                searchsubFunction2()
#            elif (sel == 0):
#                break
#            else:
#                print("Unrecognized Command")
    #dbinterface.searchCustomers()
    
def searchsubFunction():
    
def searchsubFunction2():
    

def main():

    while True:
        print(menuString)
        sel = int(input("Menu Option >> "))
        if(sel == 1):
            myfunction()
        elif(sel == 2):
            function2()
        elif(sel == 0):
            # Exits the program
            break
        else:
            print("Unrecognized Command")
   
    
# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()