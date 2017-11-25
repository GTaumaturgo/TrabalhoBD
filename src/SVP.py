#Projeto de Banco de Dados - Guilherme Andreuce, Gabriel Taumaturgo, Jadiel Teofilo, Thiago
#Version 1.0
#Imports
import mysql.connector
import csv

#Checando conexao

#DBUsername = input('Type your database username: ')
#DBPassword = input('Type your database password: ')

try:
    cnx = mysql.connector.connect(user = 'root', password = 'root',
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
menu['1']="Make a View"
menu['2']="Read data from a Table"
menu['3']="Make a Procedure"
menu['4']="Make a Trigger"
menu['5']="Exit"
menuSelect = {}
menuSelect['1'] = "Write a Select"
menuSelect['2'] = "Go back to the Menu"
menuView = {}
menuView['1'] = "Write View"
menuView['2'] = "Go back to the Menu"


while True:
    options=list(menu.keys())
    options.sort()
    for entry in options:
        print(entry, menu[entry])
        cursor = cnx.cursor()
#Switch for options
#ATENTION: Modulirize in next versions of this program
#ATENTION: Confirm Option with user

    selection=input("Please Select: ")

    if selection =='1': #MenuEntry para fazer Views
        #ATENTION: Need to save view in database and read in the selection menu.
        #ATENTION: Need to handle errors

        while True:

            optionsView=list(menuView.keys())
            optionsView.sort()
            for entry in optionsView:
                print(entry, menuView[entry])
            selection=input("Please Select: ")
            if selection =='1': #Entry para efetuar Views
                try:
                    query = input("Please type your View: ")
                    cursor.execute(query)
                    for (query) in cursor:
                        print("{}".format(query))
                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(erra))
            elif selection == '2': #Entry para voltar ao Menu
                break

    elif selection == '2': #MenuEntry para fazer Selections

        while True:

            optionsSelect=list(menuSelect.keys())
            optionsSelect.sort()
            for entry in optionsSelect:
                print(entry, menuSelect[entry])
            selection=input("Please Select: ")
            if selection =='1': #Entry para efetuar Selections
                try:
                    query = input("Please type your selection: ")
                    cursor.execute(query)
                except mysql.connector.Error as err:
                    print("Something went wrong: {}".format(err))
                for (query) in cursor:
                    print("{}".format(query))

                    #except:
            elif selection == '2': #Entry para voltar ao Menu
                break

    elif selection == '3': #MenuEntry para fazer Procedures
        print("Construct Procedure")

    elif selection == '4':
        print("Construct Trigger") #MenuEntry para fazer Triggers

    elif selection == '5':
        cnx.close();
        break

    else:
        print("Unknown Option Selected!")
