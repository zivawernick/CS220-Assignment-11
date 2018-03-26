

# Database User Interface
#
# Note that these functions contain input and output
# such as print() and input(), but do NOT contain any
# actual database code. The database is handled by
# a separate class.


from musicdb import MusicDB

# Create a database object that will handle all the DB stuff.
dbobj = MusicDB()
 
def searchArtist():
    name = input("Enter the name of the artist: ")
    result = dbobj.searchAlbum(name)
    for row in result:
        print(row)

def searchLastName():
    name = input("Enter the last name of the employee: ")
    result = dbobj.searchEmployee(name)
    for row in result:
        print(row)

def listCustomers():
    cur = dbobj.listCustomers()

    # Fetch some the results
    result = cur.fetchall()
    for row in result:
        firstName, lastName, customerID = row
        print("%s %s" % (firstName, lastName))
        print("ID: %d" % customerID)
        print()

def readEmployee():
    cur = dbobj.listEmployee()
    result = cur.fetchall()
    for row in result:
        FirstName, LastName, EmployeeId = row
        print("%s %s" % (FirstName, LastName))
        print("ID: %d" % EmployeeId)
        print()

def readAlbums():
    cur = dbobj.listAlbum()
    result = cur.fetchall()
    for row in result:
        AlbumId, Title, ArtistId = row
        print("%d" % (AlbumId))
        print("Title: %s" % (Title))
        print("ID: %d" % ArtistId)
        print()

def readgenres():
    cur = dbobj.listgenres()
    result = cur.fetchall()
    for row in result:
        GenreId, Name = row
        print("Id: %d" % (GenreId))
        print("Name: %s" % Name)
        print()

def updateEmployeeEmail():
    #get the last name of the Employee
    lName = input("Enter a last name: ")
    empID = input("Enter the Employee ID: ")
    newEmail = input("Enter the new email: ")
    dbobj.updateEmployeeEmail(lName, empID, newEmail)
    print()


def updateCustomerEmail():
    dbobj.__init__()
    #get the last name of the Employee
    lName = input("Enter a last name: ")
    cusID = input("Enter the Customers ID: ")
    newEmail = input("Enter the new email: ")
    dbobj.updateCustomerEmail(lName, cusID, newEmail)
    print()

def deleteTrack():
    track = input("Enter Track ID to Delete:")
    result = dbobj.searchTracks(track)
    for row in result:





