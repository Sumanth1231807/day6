import sqlite3 as sql
from prettytable import PrettyTable

connection=sql.connect("Mobile.db")

listOfTables=connection.execute("select name from sqlite_master where type='table' and name='Smart_Phones'").fetchall()

if listOfTables!=[]:
    print("The Table is already created")
else:
    connection.execute('''create table Smart_Phones(
                                     ID integer primary key autoincrement,
                                     S_NO integer,
                                     Brand text,
                                     Model_Name text,
                                     Manufac_Year integer,
                                     Manufac_Month text,
                                     Price integer
                                     );''')
    print("Table has created successfully.")

while True:
    print("Select Your Option from the menu given below...")
    print("1. Add Mobile Phone :")
    print("2. View Mobile Phones :")
    print("3. Search Mobile Phones using Brand :")
    print("4. Update Mobile Phones using S.NO :")
    print("5. Delete Mobile Phone using S.NO :")
    print("6. EXIT")

    choice=int(input("Enter Your Choice from the Menu to view : "))

    if choice==1:

        getS_No=input("Enter the serial number : ")
        getMobBrand=input("Enter the Mobile Brand : ")
        getModelName=input("Enter the Mobile Model : ")
        getManfac_Year=input("Enter the Mobile Manufacture Year : ")
        getManfac_Month=input("Enter the Mobile Manufacture Month : ")
        getPrice=input("Enter the Price Of the Mobile : ")

        connection.execute("insert into Smart_Phones(S_NO,Brand,Model_Name,Manufac_Year,Manufac_Month,Price)\
                           values("+getS_No+",'"+getMobBrand+"','"+getModelName+"',"+getManfac_Year+",'"+getManfac_Month+"',"+getPrice+")")

        connection.commit()
        print("Mobile Addedd Successfully.")

    elif choice==2:
        result=connection.execute("select * from Smart_Phones")

        table=PrettyTable(["ID","S.NO","BRAND","MODEL","MANUFACTURE YEAR","MANUFACTURE MONTH","PRICE"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice==3:
        getMobBrand=input("Enter the Mobile Brand Looking for : ")

        result=connection.execute("select * from Smart_Phones where Brand='"+getMobBrand+"'")
        table = PrettyTable(["ID", "S.NO", "BRAND", "MODEL", "MANUFACTURE YEAR", "MANUFACTURE MONTH", "PRICE"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        print(table)

    elif choice==4:
        getS_No=input("Enter the S_NO to get Update : ")

        getNewMobBrand = input("Enter the Mobile Brand : ")
        getNewModelName = input("Enter the Mobile Model : ")
        getNewManfac_Year = input("Enter the Mobile Manufacture Year : ")
        getNewManfac_Month = input("Enter the Mobile Manufacture Month : ")
        getNewPrice = input("Enter the Price Of the Mobile : ")

        result=connection.execute("update Smart_Phones set Brand='"+getNewMobBrand+"',Model_Name='"+getNewModelName+"',Manufac_Year="+getNewManfac_Year+",Manufac_Month='"+getNewManfac_Month+"',Price="+getNewPrice+" where S_NO="+getS_No+"")
        connection.commit()
        print("Entery Updated successfully")

    elif choice==5:
        getS_No=input("Enter the serial number that want to delete : ")
        connection.execute=("delete from Smart_Phones where S_NO="+getS_No+"")
        connection.commit()
        print("Mobile Deleted Successfully.")

    elif choice==6:
        break

    else:
        print("oops You entered the INVALID choice Please try again by choosing the VALID option........")
