import sqlite3

db = sqlite3.connect("ece1_1.db")


def createTable():
    db.row_factory = sqlite3.Row
    db.execute('create table if not exists cse1_2(Day text, "8-9" text, "9-10" text, "10-11" text, "11-12" text, "12-1" text,"1-2" text, "2-3" text, "3-4" text, "4-5" text, "5-6" text)')

def AddRow(Day, Schedule):
    db.execute("insert into cse1_2 values(?,?,?,?,?,?,?,?,?,?,?)", (Day, Schedule[0], Schedule[1], Schedule[2], Schedule[3], Schedule[4], Schedule[5], Schedule[6], Schedule[7], Schedule[8], Schedule[9]))
    db.commit()


def ReturnLecture(day,slot):
    
    db.row_factory=sqlite3.Row
    lecture = db.execute("select * from cse1_2")
    for row in lecture:
        if row["Day"] == day:
            return row[slot]

def DeleteElement(ID):
    db.row_factory=sqlite3.Row
    db.execute("delete from cse1_2 where ID='{}'".format(ID))
    db.commit()

def UpdateRecord(day,slot,text):
    db.row_factory=sqlite3.Row
    db.execute("update cse1_2 set '{}'='{}' where Day='{}'".format(slot,text,day))
    db.commit()



def main():
    createTable()
    # Mon=["a","b","c","d","e","f","g","h","i","j"]
    # Day=["Mon","Tue","Wed","Thurs","Fri"]
    # for i in range(0,5):
    #     AddRow(Day[i],Mon)
    # UpdateRecord("Mon","8-9","No")
    # print(ReturnLecture("Mon","8-9"))    

if __name__ == '__main__': main()
