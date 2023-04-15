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
    global employee_num, e_entry_confirmed
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
            try:
                e_date_of_birth = input("Employee Date of Birth (MM-DD-YYYY): ")
                e_date_of_birth = datetime.datetime.strptime(e_date_of_birth, "%m-%d-%Y").date()
                break
            except:
                print("Invalid input, please try again")

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
                e_date_of_hire = datetime.datetime.strptime(e_date_of_hire, "%m-%d-%Y").date()
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
                dependent_list = []
                dependent_list_name = []
                dependent_list_age = []
                dependent_list_relationship = []
                for x in range(e_num_dep):
                    dependent_info = {}
                    dependent_info['Name'] = input(f"Dependent {x + 1} Name: ")
                    dependent_info['Age'] = input(f"Dependent {x + 1} Age: ")
                    dependent_info['Relationship'] = input(f"Dependent {x + 1} Relationship: ")
                    dependent_list_name.append(dependent_info['Name'])
                    dependent_list_age.append(dependent_info['Age'])
                    dependent_list_relationship.append(dependent_info['Relationship'])
                    dependent_info_record = f"{dependent_info['Name']}, {dependent_info['Age']}, {dependent_info['Relationship']}"
                    dependent_list.append(dependent_info_record)
                break
            else:
                break

        print(f"EMPLOYEE PHONE:                           {e_telephone}")
        print(f"EMPLOYEE NAME:                            {e_first_name} {e_last_name}")
        print(f"EMPLOYEE ADDRESS:                         {e_address}")
        print(f"EMPLOYEE CITY:                            {e_city}")
        print(f"EMPLOYEE PROVINCE:                        {e_province}")
        print(f"EMPLOYEE POSTAL CODE:                     {e_postcode}")
        print(f"EMPLOYEE NUMBER:                          {employee_num}")
        print(f"EMPLOYEE BIRTH DATE:                      {e_date_of_birth}")
        print(f"DATE OF HIRE:                             {e_date_of_hire}")
        print(f"BRANCH                                    {e_branch}")
        print(f"TITLE:                                    {e_title}")
        print(f"SALARY:                                   {e_salary}")
        for x in range(e_num_dep):
            print(f"DEPENDANT {x + 1} INFO: ")
            print(f"    NAME:                                 {dependent_list_name[x]}")
            print(f"    AGE:                                  {dependent_list_age[x]}")
            print(f"    RELATIONSHIP:                         {dependent_list_relationship[x]}")

        while True:
            confirm_employee_entry = input("Confirm employee information? (Y/N): ").upper()
            if confirm_employee_entry == 'Y':
                is_entering_new_employee = False

                with open('employee.dat', 'a') as e:
                    e.write(
                        f"{employee_num}, {e_first_name}, {e_last_name}, {e_address}, {e_city}, {e_province}, {e_telephone}, {e_date_of_hire}, {e_branch}, {e_title}, {e_salary}, {e_num_dep}\n")
                    employee_num += 1
                    print("Employee information saved\n")

                if e_num_dep > 0:
                    with open('dependents.dat', 'a') as g:
                        for x in range(e_num_dep):
                            g.write(f'{dependent_num}, {e_first_name}, {e_last_name}, {dependent_list[x]}\n')
                            dependent_num += 1
                break
            elif confirm_employee_entry == 'N':
                print()
                break

        while True:
            option_1_end = input("Press 1 to enter another employee or END to exit: ").upper()
            if option_1_end == '1':
                is_entering_new_employee = True
                break
            elif option_1_end == "END":
                with open('constants.dat', "w") as r:
                    r.write(f'{employee_num}\n')
                    r.write(f'{customer_num}\n')
                    r.write(f'{item_num}\n')
                    r.write(f'{dependent_num}')
                    r.write(f'{HST}\n')
                break


def new_item():
    is_entering_new_item = True
    global item_num

    while is_entering_new_item:
        print("Simpson Carpet World New Inventory Item\nPlease input the information below:")

        while True:
            i_name = input("Item Name: ")
            if len(i_name) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_type = input("Item Type: ")
            if len(i_type) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_desc = input("Item Description: ")
            if len(i_desc) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_colour = input("Item Colour: ")
            if len(i_colour) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_size = input("Item Size: ")
            if len(i_size) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_pattern = input("Item Pattern: ")
            if len(i_pattern) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_cost = input("Item Cost: ")
            if len(i_cost) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_retail = input("Item Retail Price: ")
            if len(i_retail) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_qoh = input("Item Quantity on Hand: ")
            if len(i_qoh) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_reorder = input("Item Reorder Point: ")
            if len(i_reorder) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            i_max = input("Item Maximum Level: ")
            if len(i_max) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        print(f"ITEM NUMBER:                              {item_num}")
        print(f"ITEM NAME:                                {i_name}")
        print(f"ITEM TYPE:                                {i_type}")
        print(f"ITEM DESCRIPTION:                         {i_desc}")
        print(f"ITEM COLOUR:                              {i_colour}")
        print(f"ITEM SIZE:                                {i_size}")
        print(f"ITEM PATTERN:                             {i_pattern}")
        print(f"ITEM COST:                                {i_cost}")
        print(f"ITEM RETAIL PRICE:                        {i_retail}")
        print(f"ITEM QUANTITY:                            {i_qoh}")
        print(f"ITEM REORDER POINT:                       {i_reorder}")
        print(f"ITEM MAXIMUM LEVEL:                       {i_max}")

        while True:
            confirm_item_entry = input("Confirm item information? (Y/N): ").upper()
            if confirm_item_entry == 'Y':
                is_entering_new_item = False
                with open('items.dat', 'a') as e:
                    e.write(f"{item_num}, {i_name}, {i_type}, {i_desc}, {i_colour}, {i_size}, {i_pattern}, {i_cost}, {i_retail}, {i_qoh}, {i_reorder}, {i_max}\n")
                    item_num += 1
                    print("Item information saved\n")
                break
            elif confirm_item_entry == 'N':
                print()
                break

        while True:
            option_3_end = input("Press 1 to enter another item or END to exit: ").upper()
            if option_3_end == '1':
                is_entering_new_item = True
                break
            elif option_3_end == "END":
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
                print("ERROR: Value must be 1-9.")
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
                new_item()
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
