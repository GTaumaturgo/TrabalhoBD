#Projeto de Banco de Dados - Guilherme Andreuce, Gabriel Taumaturgo, Jadiel, Thiago
#Version 1.0
#Imports
import mysql.connector
import csv

#Checando conexao

DBUsername = input('Type your database username: ')
DBPassword = input('Type your database password: ')

try:
    cnx = mysql.connector.connect(user = DBUsername, password = DBPassword,
                host = '127.0.0.1',
                database = 'bd_enem_2015')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Bad username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist or invalid name")
    else:
        print(err)
else:
    print("Connection estabilished successfuly")

#Menu entry
print("Welcome to the Enem 2015 database analyser!")
print("Select what you want to do next")
#Create menu options
menu = {}
menu['1']="Create a Table"
menu['2']="Read data from a Table"
menu['3']="Update data from a Table"
menu['4']="Delete a Table"
menu['5']="Exit"
while True:
    options=list(menu.keys())
    options.sort()
    for entry in options:
        print(entry, menu[entry])
#Switch for options
#ATENTION: Modulirize in next versions of this program
#ATENTION: Confirm Option with user
    selection=input("Please Select: ")
    if selection =='1':
        print("Create")

    elif selection == '2':

        #ATENTION: Need to handle invalid Selections
        #ATENTION: Need to handle multiple queries
        cursor = cnx.cursor()
        query = input("Please type your selection: ")
        cursor.execute(query, multi = true)
        for (query) in cursor:
            print("{}".format(query))
        cnx.close();

    elif selection == '3':
        print("Update")

    elif selection == '4':
        print("Delete")

    elif selection == '5':
        break

    else:
        print("Unknown Option Selected!")
