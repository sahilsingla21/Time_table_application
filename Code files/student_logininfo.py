import sqlite3
import variables
db = sqlite3.connect("logininfo.db")

def createTable():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists logininfo(ID text, Password text)")

def AddRow(ID, Password):
    db.execute("insert into logininfo values(?,?)", (ID, Password))
    db.commit()

def ListAdmins():

    db.row_factory = sqlite3.Row
    cursor=db.execute("select * from logininfo")
    for row in cursor:
        print("ID: {}, Password: {}".format(row["ID"],row["Password"]))

def DeleteElement(ID):
    db.row_factory=sqlite3.Row
    db.execute("delete from logininfo where ID='{}'".format(ID))
    db.commit()

def UpdateRecord(ID,Password1):
    db.row_factory=sqlite3.Row
    db.execute("update logininfo set Password=? where ID=?",(Password1,ID))
    db.commit()

def check_if_exists(ID,Password):

    db.row_factory = sqlite3.Row
    cursor1=db.execute("select * from logininfo")
    # print(type(ID))
    for row in cursor1:
        if str(ID)==str(row["ID"]):
            # print("hey")
            cursor=db.execute("select Password from logininfo where ID=?",(ID,))
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
    else:
        return False
    
def checkPassword():
    db.row_factory = sqlite3.Row
    cursor=db.execute("select * from logininfo where id=?",(variables.ID,))
    for row in cursor:
        if row["Password"]==variables.textinput4.text:
            return True
        else:
            return False

def changePassword():
    db.row_factory= sqlite3.Row
    UpdateRecord(variables.ID,variables.textinput3.text)

def main():
    createTable()
    # for i in range(18105001,18105121):
    #    AddRow(i,"pass{}".format(i))
    # ListAdmins()
    # check_if_exists("18103020","pass18103020")
    # UpdateRecord("18103020","pass18103020")
    # changePassword()
if __name__ == '__main__': main()
