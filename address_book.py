# Python address book using sqlite

import sqlite3

class AddressBook:
    def __init__(self):
        self.con = sqlite3.connect("address_book.db")
        self.cur = self.con.cursor()

    def createdb(self):
        if (self.cur.execute("SELECT name FROM sqlite_master WHERE name='address_book'") == None):
            self.cur.execute("CREATE TABLE address_book(name, address, phone)")
            if (self.cur.execute("SELECT name FROM sqlite_master WHERE name='address_book'") == None):
                print("ERROR - Database creation failed")
                exit()

    def adddata(self):
        self.cur.execute("""
            INSERT INTO address_book VALUES
            ('Fred Blogs', '1, Fish Street, Dudley', '01384 111111'),
            ('Sally Smith', 'Dunroaming, The Lane, Somewhere Posh', '05634 735393')
            """)

    def showdata(self):
        for row in self.cur.execute("SELECT name, phone FROM address_book ORDER BY name"):
            print(row)

    def closedb(self):
        self.con.close()


# Run stuff
if __name__ == "__main__":
    print("Python Address Book")
    ab = AddressBook()

    ab.createdb()
    ab.adddata()
    ab.showdata()
    ab.closedb()