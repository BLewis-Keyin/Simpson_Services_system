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
f = open('constants.dat', 'r')
employee_num = int(f.readline().strip())
customer_num = int(f.readline().strip())
item_num = int(f.readline().strip())
dependent_num = int(f.readline().strip())
HST = float(f.readline().strip())
f.close()

# define province list
provlist = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']


def new_employee():
    global employee_num
    global dependent_num
    is_entering_new_employee = True
    while is_entering_new_employee:
        print("Simpson Carpet World Employee registration\nPlease input the information below:")

        while True:
            e_first_name = input("Employee First Name: ").capitalize()
            break

        while True:
            e_last_name = input("Employee Last Name: ").capitalize()
            break

        while True:
            e_address = input("Employee Street Address: ").capitalize()
            break

        while True:
            e_city = input("Employee City: ").capitalize()
            break

        while True:
            e_postcode = input("Employee Postal Code: ").upper().replace("-", "").replace(" ", "")
            if len(e_postcode) > 6:
                print("ERROR: Postal code length exceeds maximum amount (6 characters)")
            elif len(e_postcode) == 0:
                print("ERROR: Nothing was entered")
            elif e_postcode[0:5:2].isalpha() is False or e_postcode[1:6:2].isdigit() is False:
                print("ERROR: Invalid postal code format (X9X9X9)")
            else:
                break

        while True:
            e_province = input("Employee Province: ").upper()
            if len(e_province) != 2:
                print("Province must be in format XX")
            elif e_province not in provlist:
                print("Invalid Province, please enter a valid province")
            else:
                break

        while True:
            e_telephone = input("Employee Telephone: ").replace('-', '').replace('(', '').replace(')', '').replace(' ',                                                                                        '')
            if e_telephone.isdigit() == False:
                print("Telephone Number must only contain numbers")
            elif len(e_telephone) != 10:
                print("Telephone Number must be on 10 digits in length")
            else:
                break

        while True:
            try:
                e_date_of_hire = input("Employee Date of Hire (MM-DD-YYYY): ")
                e_date_of_hire = datetime.datetime.strptime(e_date_of_hire, "%m-%d-%Y")
                break
            except:
                print("Invalid input, please try again")

        while True:
            e_branch = input("Employee Branch: ")
            break

        while True:
            e_title = input("Employee Job Title: ").capitalize()
            break

        while True:
            try:
                e_salary = float(input("Employee Salary: "))
                break
            except ValueError:
                print("Invalid input, please try again")

        while True:
            e_num_dep = int(input("Employee Amount of Dependants: "))
            if e_num_dep > 0:
                dependant_info = []
                for x in range(e_num_dep):
                    dependant_info.append(input(f" Enter Dependant {x + 1} Name: "))
                    dependant_info.append(input(" Enter Dependant Age: "))
                    dependant_info.append(input(" Enter Dependant Relationship: "))
                break
            else:
                break

        with open('employee.dat', 'a') as e:
            e.write(
                f"{employee_num}, {e_first_name}, {e_last_name}, {e_address}, {e_city}, {e_province}, {e_telephone}, {e_date_of_hire}, {e_branch}, {e_title}, {e_salary}, {e_num_dep}, {dependant_info}")
            employee_num += 1
            print("Employee information saved\n")

        if e_num_dep > 0:
            with open('dependents.dat', 'a') as g:
                g.write(f'{dependent_num},{e_first_name}, {e_last_name}, {dependant_info[0]}, {dependant_info[1]}, {dependant_info[2]}\n')
                dependent_num += 1
                if e_num_dep > 1:
                    for x in range(1, e_num_dep):
                        g.write(f'{dependent_num},{e_first_name}, {e_last_name}, {dependant_info[3 * x]}, {dependant_info[(3 * x) + 1]}, {dependant_info[(3 * x) + 2]}\n')
                        dependent_num += 1

        while True:
            option_1_end = input("Press 1 to enter another employee or END to exit: ").upper()
            if option_1_end == 1:
                break
            elif option_1_end == "END":
                is_entering_new_employee = False
                with open('constants.dat', "w") as r:
                    r.write(f'{employee_num}\n')
                    r.write(f'{customer_num}\n')
                    r.write(f'{item_num}\n')
                    r.write(f'{dependent_num}')
                    r.write(f'{HST}\n')
                break

# Start of the main program
while True:

    # Print the header and menu options
    print("Simpson Carpet World")
    print("Company Services System\n")
    print("1. Enter a New Employee")
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
                new_employee()
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
