
# Database User Interface
#
# Note that these functions contain input and output
# such as print() and input(), but do NOT contain any 
# actual database code. The database is handled by 
# a separate class.


from musicdb import MusicDB

# Create a database object that will handle all the DB stuff.
dbobj = MusicDB()

def listCustomers():
    cur = dbobj.listCustomers()
    
    # Fetch some the results
    result = cur.fetchall()
    for row in result:
        firstName, lastName, customerID = row
        print("%s %s" % (firstName, lastName))
        print("ID: %d" % customerID)
        print()
        
    
def searchCustomers():    
    # Get a string from the user
    name = input("Enter a last name: ")
    
    result = dbobj.searchCustomer(name)
    
    # Print the results, in this case a list of tuples
    for row in result:
        print(row)
        
def deleteTrack():
    track = input("Enter Track ID to Delete")
    result = dbobj.searchCustomer(track)
    for row in result:
        trackID, trackName = row
    