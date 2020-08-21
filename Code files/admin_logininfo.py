import sqlite3
import variables
db = sqlite3.connect("admin_logininfo.db")

def createTable():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists admin_logininfo(ID text, Password text)")

def AddRow(ID, Password):
    db.execute("insert into admin_logininfo values(?,?)", (ID, Password))
    db.commit()

def ListAdmins():
    cursor=db.execute("select * from admin_logininfo")
    for row in cursor:
        print("ID: {}, Password: {}".format(row["ID"],row["Password"]))

def DeleteElement(ID):
    db.row_factory=sqlite3.Row
    db.execute("delete from admin_logininfo where ID='{}'".format(ID))
    db.commit()

def UpdateRecord(ID,Password):
    db.row_factory=sqlite3.Row
    db.execute("update admin_logininfo set Password=? where ID=?",(Password,ID))
    db.commit()

def check_if_exists(ID,Password):
    cursor=db.execute("select Password from admin_logininfo where ID=?",(ID,))
    # print(ID)
    # print(Password)

    passwrd=""
    for row in cursor:
        passwrd=row[0]
        # passwrd="hey"
        break
    # print(passwrd)        
    if passwrd==Password:
        return True
    else:
        return False


def checkPassword():
    db.row_factory = sqlite3.Row
    cursor=db.execute("select * from admin_logininfo where id=?",(variables.id,))
    for row in cursor:
        if row["Password"]==variables.textinput4.text:
            return True
        else:
            return False

def changePassword():
    db.row_factory= sqlite3.Row
    UpdateRecord(variables.id,variables.textinput3.text)

def main():
    createTable()
    # AddRow("Mayank","Mayank@123")
    # AddRow("Shilpa","Shilpa@123")
    # for i in range(19103001,19103121):
    #    AddRow(i,"pass{}".format(i))
    # DeleteElement("Shilpa")
    ListAdmins()
    # check_if_exists("18103020","pass18103020")

if __name__ == '__main__': main()
