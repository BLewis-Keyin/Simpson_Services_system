# Made by Group 5
# 4/05/2023

'''
Constants that could be defined:

Customer Number Counter
Employee Number Counter
Inventory Item Number Counter
HST

'''


# Import modules
import datetime

# import constants from constants.dat
f = open('constants.dat')
employee_num = int(f.readline().strip())
customer_num = int(f.readline().strip())
item_num = int(f.readline().strip())
HST = float(f.readline().strip())

# Start of the main program
while True:

    # Print the header and menu options
    print("Simpson Carpet World")
    print("Company Services System\n")
    print("1. Enter a New Employee.")
    print("2. Enter a New Customer")
    print("3. Enter a New Inventory Item")
    print("4. Record Customer Purchase")
    print("5. Print Employee Listing")
    print("6. Print Customers by Branch")
    print("7. Print Orders By Customer")
    print("8. Print Reorder Listing")
    print("9. Quit Program\n")

    # Menu option processing
    while True:
        try:
            menu_choice = int(input("   Enter choice (1-9)  : "))
            if menu_choice < 1:
                print("")
                print("ERROR: Value must be 1-5.")
                print("")
            elif menu_choice == 1:
                print("")
                break
            elif menu_choice == 2:
                print("")
                break
            elif menu_choice == 3:
                print("")
                break
            elif menu_choice == 4:
                print("")
                break
            elif menu_choice == 5:
                print("")
                break
            elif menu_choice == 6:
                print("")
                break
            elif menu_choice == 7:
                print("")
                break
            elif menu_choice == 8:
                print("")
                break
            elif menu_choice == 9:
                exit()
            elif menu_choice > 9:
                print("")
                print("ERROR: Value must be 1-9.")
                print("")
        except ValueError:
            print("Invalid input, please try again.")

