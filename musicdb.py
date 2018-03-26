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
        cur = self.conn.cursor()
        params = (name,)
        cur.execute("SELECT * FROM employees WHERE LastName like ?", params)
        result = cur.fetchall()
        return(result)
        
    def findnetID(self, IdType, table):
        cur = self.conn.cursor()
        cur.execute("Select MAX(" + IdType + " + 1) from " + table)
        results = cur.fetchone
        return(results)

    def createCustomer(self, FirstName, LastName, CustomerId, Address, City,
                  State, Country, PostalCode, Phone, Email):
        #Create a cursor object to execute queries and review results
        cur = self.conn.cursor()
        params = (FirstName, LastName, CustomerId, Address, City,
                  State, Country, PostalCode, Phone, Email, '4')
        # Run a query
        #this is not working yet but I am not sure how to fix it - in SQLite this is the setup for the querry 
        cur.execute("Insert into customers (FirstName, LastName, CustomerId, Address, City, State, Country, PostalCode, Phone, Email, SupportRepId) Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
        #commit the changes 
        self.conn.commit()

            
    def createEmployee(self, EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate,
                  HireDate, Address, City, State, Country, PostalCode, Phone,
                  Fax, Email):
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
        results = cur.fetchall()
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
        
    def deleteTrack(self, track):
        cur = self.conn.cursor()
        params = (track,)
        print("You deleted track ID " + track)
        cur.execute("DELETE FROM tracks WHERE TrackID = ?", params)
        cur.execute("DELETE FROM invoice_items WHERE TrackID = ?", params)
        cur.execute("DELETE FROM playlist_track WHERE TrackID = ?", params)
        self.conn.commit()
    
    def deleteInvoice(self, invoiceID):
        cur = self.conn.cursor();
        params = (invoiceID,)
        print("You deleted the invoice with invoiceID " + invoiceID)
        cur.execute("DELETE FROM invoices WHERE invoiceID = ?", params)
        cur.execute("DELETE FROM invoice_items WHERE invoiceID = ?", params)
        self.conn.commit()
