# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:24:00 2018

@author: Lu Liu
"""
import sqlite3 as db

class MusicDB:
    def __init__( self):
      self.conn = db.connect("music.db")
      
    def __del__(self):
      self.conn.close()
    
    def listCustomers(self):       
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor()
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT firstName, lastName, customerID FROM customers")
        
        return(cur)
        # Fetch all the results
#        result = cur.fetchmany(5)
#        for row in result:
#            fname, lname, salary = row
#            print("%s %s" % (fname, lname))
#            print("Salary: %d" % salary)
#            print()
#        
        
    def searchCustomer(self, name):    
        # Create a cursor object to execute queries and retrieve results
        cur = self.conn.cursor();        
        
        # parameters need to be in a python tuple
        # this is how to create a tuple with a single value
        params = (name,)
        
        # Run a query: provide any SQL in a string
        cur.execute("SELECT * FROM customers WHERE lastName like ?", params)
        
        # Fetch all the results
        result = cur.fetchall()
        
        # Print the results, in this case a list of tuples
        return(result)
        
    def createCustomer(self):
        #Create a cursor object to execute queries and review results
        cur = self.conn.cursor();
        
        #Create the python tuple with all the values
        params = (FirstName, LastName, CustomerId, Company, Address, City,
                  State, Country, PostalCode, Phone, Fax, Email, SupportRedId)
        
        # Run a query
        cur.execute("Select FirstName, LastName, CustomerId, Company,"
                    "Address, City, State, Country, PostalCode, Phone,"
                    "Fax, Email, SupportRedId From customers", params)
        
        # Fetch all the results
        result = cur.fetchall()
        for row in results:
            FirstName, LastName, CustomerId, Company, Address,
            City, State, Country, PostalCode = row
            
            print("%s %s" % (FirstName, LastName))
            print("ID: %d" % CustomerId)
            print("Company: %s" % Company)
            print("Address: %s %s %s %s %s" % (Address, City, State, Country,
                                               PostalCode))
            print("Phone: %s" % Phone)
            print("Fax: %s" % Fax)
            print("Email: %s" % Email)
            print("SupportRepId: %d" % SupportRepId)
            print()
            
    def createEmployee(self):
        # Create a cursor object to execute queries and review results
        cur = self.conn.cursor();
        
        # Create the python tuple with all the values
        params = (EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate,
                  HireDate, Address, City, State, Country, PostalCode, Phone,
                  Fax, Email)
        
        # Run a query
        cur.execute("Select EmployeeId, LastName, FirstName, Title, ReportsTo,"
                    "BirthDate, HireDate, Address, City, State, Country," 
                    "PostalCode, Phone, Fax, Email From employees", params)
        
        # Fetch all the results
        result = cur.fetchall()
        for row in results:
            EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate,
            HireDate, Address, City, State, Country, PostalCode, Phone,
            Fax, Email = row
                  
            print("Employee ID: %d" % EmployeeId)
            print("%s %s" % (FirstName, LastName))
            print("Title: %s" % Title)
            print("Reports To: %s" % ReportsTo)
            print("Birth Date: %s" % BirthDate)
            print("Hire Date: %s" % HireDate)
            print("Address: %s %s %s %s %s" % (Address, City, State,
                                                     Country, PostalCode))
            print("Phone: %s" % Phone)
            print("Fax: %s" % Fax)
            print("Email: %s" % Email)
            print()
