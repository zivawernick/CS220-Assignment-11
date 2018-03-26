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
        cur = self.conn.cursor()
        cur.execute("SELECT firstName, lastName, customerID FROM customers")       
        return(cur)

    def listEmployee(self):
        cur = self.conn.cursor()
        cur.execute("SELECT FirstName, LastName, EmployeeId FROM employees")
        return(cur)
    
    def listAlbum(self):
        cur = self.conn.cursor()
        cur.execute("SELECT AlbumId, Title, ArtistId FROM albums")
        return(cur)
    
    def listgenres(self):
        cur = self.conn.cursor()
        cur.execute("SELECT GenreId, Name FROM genres")
        return(cur)
        
    def searchAlbum(self, name):
        cur = self.conn.cursor();
        params = (name,)
        cur.execute("SELECT albums.* FROM albums, artists WHERE artists.ArtistId = albums.ArtistId AND artists.Name like ?", params)
        result = cur.fetchall()
        return(result)
    
    def searchEmployee(self, name):
        cur = self.conn.cursor();
        params = (name,)
        cur.execute("SELECT * FROM employees WHERE LastName like ?", params)
        result = cur.fetchall()
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
            
    def updateEmployeeEmail(self, name, empID, email):
        #create a cursor object 
        cur = self.conn.cursor();
        params = (email, name, empID)
        print("You updated " + name + "'s email to: " + email)
        #change the database with new info 
        cur.execute("Update employees Set email = ? Where LastName = ? and EmployeeId = ?", params)
        #commit the changes 
        self.conn.commit()
      
    def updateCustomerEmail(self, name, cusID, email):
        #create a cursor object 
        cur = self.conn.cursor();
        params = (email, name, cusID)
        print("You updated " + name + "'s email to: " + email)
        #change the database with new info 
        cur.execute("Update customers Set email = ? Where LastName = ? and CustomerId = ?", params)
        #commit the changes 
        self.conn.commit()