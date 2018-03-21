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
        
        
    def deleteTrack(self, track):
        cur = self.conn.cursor();
        params = (track,)
        cur.execute("DELETE * FROM tracks WHERE trackName like ?", params)
      
        
