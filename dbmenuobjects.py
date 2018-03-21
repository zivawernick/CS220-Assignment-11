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

def myfunction():
    dbinterface.listCustomers()
    
def function2():
    dbinterface.searchCustomers()


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