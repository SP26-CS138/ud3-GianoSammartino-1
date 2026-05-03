'''
DEVELOPER(S): Giano Sammartino
COLLABORATORS: none
DATE: 4/24/2026
'''

"""
A simple password storage program.

A console based password manager that allows the user to create accounts with a username and 
password and store, view, search, or add more accounts.


I chose to use a dictionary instead of a list because each account is associated with a website name. This allows for fast 
lookup using the site name as a key, which makes all of the functions more efficient than searching through a list of entries one by one.
"""

##########################################
# IMPORTS:
# <list of modules needed for the program and their purpose>
##########################################
# No imports used


##########################################
# FUNCTIONS:
##########################################

#1
def load_accounts(file_name):
    #Loads account data from a file into a dictionary

    accounts = {}
    file_in = open(file_name, "a+") # Creates a file if it doesn't exist
    file_in.seek(0)                 # Moves to start of file so it can be read
    for line in file_in:
        line = line.strip()
        if line != "":
            site, username, password = line.split(",")
            accounts[site] = [username, password]

    file_in.close()
    return accounts


#2
def save_accounts(file_name, accounts):
    #saves the accounts dictionary back into the file & overwrites existing file

    file_out = open(file_name, "w")
    for site in accounts:
        username = accounts[site][0]
        password = accounts[site][1]
        file_out.write(site + "," + username + "," + password + "\n")

    file_out.close()


#3
def view_accounts(accounts):
    #Displays all stored accounts in a formatted way

    print("\n---Stored Accounts---")
    if len(accounts) == 0:
        print("No accounts saved")
    else:
        for site in accounts:
            print("Site:", site)
            print("Username:", accounts[site][0])
            print("Password:", accounts[site][1])
            print("---------------------")


#4
def search_accounts(accounts):
    #Searches for an account by site name

    site = input("Enter site name to search: ").lower()
    if site in accounts:
        print("\nAccount found")
        print("Site:", site)
        print("Username:", accounts[site][0])
        print("Password:", accounts[site][1])
    else:
        print("No account found for that site.")
    

#5
def add_account(accounts):
    #Adds a new account to the dictionary

    site = input("Enter site name: ").lower()
    username = input("Enter username: ")
    password = input("Enter password: ")

    accounts[site] = [username, password]
    print("Account added.")


#6
def get_choice():
    #Gets validated menu choice

    print("\n1. View all accounts")
    print("2. Search account")
    print("3. Add account")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")
    if choice in ["1", "2", "3", "4"]:
        return choice
    else:
        print("Invalid input. Try again")
        return get_choice()


##########################################
# MAIN PROGRAM
##########################################
def main():
    file_name = "accounts.txt"
    accounts = load_accounts(file_name)

    print("Welcome to password manager.")

    running = True
    while running:
        choice = get_choice()
        if choice == "1":
            view_accounts(accounts)
        elif choice == "2":
            search_accounts(accounts)
        elif choice == "3":
            add_account(accounts)
        elif choice == "4":
            save_accounts(file_name, accounts)
            print("Data saved.")
            running = False


main()
