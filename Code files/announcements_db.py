import sqlite3

db = sqlite3.connect("announcements.db")

def createTable():
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists announcements(Year integer, Branch text, Group_no integer,Announcement text)")

def AddRow(Year, Branch, Group, Announcement):
    db.execute("insert into announcements values(?,?,?,?)", (Year, Branch, Group, Announcement))
    db.commit()

def ListAdmins():
    cursor=db.execute("select * from announcements")
    for row in cursor:
        print("Year: {}, Branch:{}, Group_no:{}, Announcement: {}".format(row["Year"],row["Branch"],row["Group_no"],row["Announcement"]))

# def DeleteElement(ID):
#     db.row_factory=sqlite3.Row
#     db.execute("delete from logininfo where ID='{}'".format(ID))
#     db.commit()

def UpdateRecord(Year, Branch1, Group, Ann):
    db.row_factory=sqlite3.Row
    # db.execute("update logininfo set Announcement=? where Year=? and Branch=? and Group=?",(Announcement, Year, Branch, Group))
    cursor=db.execute("select * from announcements where Group_no=? and Branch=? and Year=?",(Group,Branch1,Year))
    current_ann=""
    for row in cursor:
        current_ann="{} \n{}".format(current_ann,row["Announcement"])
        break
    new_ann="{} {}".format(Ann,current_ann)
    db.execute("update announcements set Announcement=? where Group_no =? and Branch=? and Year=?",(new_ann,Group,Branch1,Year) )
    db.commit()

def Return_Announcements(Year, Branch, Group):
    db.row_factory=sqlite3.Row
    cursor=db.execute("select * from announcements where Group_no=? and Branch=? and Year=?",(Group,Branch,Year))
    ann_list=""
    for row in cursor:
        ann_list=row["Announcement"].split('\n')
        break
    return ann_list



def main():
    createTable()
    # branch=["CSE","ECE"]
    # for year in range(1,3):
    #     for branch_name in branch:
    #         for  group in range(1,3):
    #             AddRow(year,branch_name,group,"No more announcements")
    # anni="Noooooop"
    # UpdateRecord("2","ECE","2",anni)
    # ListAdmins()
    # Return_Announcements("2","ECE","2")

if __name__ == '__main__': main()
