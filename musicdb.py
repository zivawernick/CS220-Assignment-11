# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 18:24:00 2018

@author: your name here
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
        
