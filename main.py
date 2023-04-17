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
today = datetime.date.today()

# import constants from constants.dat
f = open('constants.dat', 'r')
employee_num = int(f.readline().strip())
customer_num = int(f.readline().strip())
item_num = int(f.readline().strip())
dependent_num = int(f.readline().strip())
purchase_num = int(f.readline().strip())
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
            if len(e_first_name) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            e_last_name = input("Employee Last Name: ").capitalize()
            if len(e_last_name) == 0:
                print("Nothing was entered, please try again.")
            else:
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
            if len(e_address) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            e_city = input("Employee City: ").capitalize()
            if len(e_city) == 0:
                print("Nothing was entered, please try again.")
            else:
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
            if len(e_branch) == 0:
                print("Nothing was entered, please try again.")
            else:
                break

        while True:
            e_title = input("Employee Job Title: ").capitalize()
            if len(e_title) == 0:
                print("Nothing was entered, please try again.")
            else:
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
                    r.write(f'{dependent_num}\n')
                    r.write(f'{purchase_num}\n')
                    r.write(f'{HST}\n')
                break


def new_customer():
    global customer_num
    global purchases_num
    is_entering_new_customer = True
    while is_entering_new_customer:
        print("Simpson Carpet World Customer registration\nPlease input the information below:")
        while True:
            c_first_name = input("Customer First Name: ").capitalize()
            break
        while True:
            c_last_name = input("Customer Last Name: ").capitalize()
            break

        while True:
            try:
                c_date_of_birth = input("Customer Date of Birth (MM-DD-YYYY): ")
                c_date_of_birth = datetime.datetime.strptime(c_date_of_birth, "%m-%d-%Y").date()
                break
            except:
                print("Invalid input, please try again")

        while True:
            c_address = input("Customer Street Address: ").capitalize()
            break

        while True:
            c_city = input("Customer City: ").capitalize()
            break

        while True:
            c_postcode = input("Customer Postal Code: ").upper().replace("-", "").replace(" ", "")
            if len(c_postcode) > 6:
                print("ERROR: Postal code length exceeds maximum amount (6 characters)")
            elif len(c_postcode) == 0:
             print("ERROR: Nothing was entered")
            elif c_postcode[0:5:2].isalpha() is False or c_postcode[1:6:2].isdigit() is False:
                print("ERROR: Invalid postal code format (X9X9X9)")
            else:
                break

        while True:
            c_province = input("Customer Province: ").upper()
            if len(c_province) != 2:
                print("Province must be in format XX")
            elif c_province not in provlist:
                print("Invalid Province, please enter a valid province")
            else:
                break

        while True:
            c_telephone = input("Customer Telephone: ").replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
            if c_telephone.isdigit() == False:
                print("Telephone Number must only contain numbers")
            elif len(c_telephone) != 10:
                print("Telephone Number must be on 10 digits in length")
            else:
                break

        while True:
            try:
                c_date_of_joining = input("Customer Date of Joining (MM-DD-YYYY): ")
                c_date_of_joining = datetime.datetime.strptime(c_date_of_joining, "%m-%d-%Y").date()
                break
            except:
                print("Invalid input, please try again")

        while True:
            c_branch = input("Customer Branch: ")
            break
        print()
        print(f"CUSTOMER NAME:                            {c_first_name} {c_last_name}")
        print(f"CUSTOMER NUMBER:                          {customer_num}")
        print(f"CUSTOMER BIRTH DATE:                      {c_date_of_birth}")
        print(f"DATE OF JOINING:                          {c_date_of_joining}")
        print(f"BRANCH JOINED AT                          {c_branch}")

        while True:
            confirm_customer_entry = input("Confirm customer information? (Y/N): ").upper()
            if confirm_customer_entry == 'Y':
                is_entering_new_customer = False
                with open('customers.dat', 'a') as c:
                    c.write(
                        f"{customer_num}, {c_first_name}, {c_last_name}, {c_address}, {c_city}, {c_province}, {c_telephone}, {c_date_of_birth}, {c_date_of_joining}, {c_branch}\n")
                customer_num += 1
                print("Customer information saved\n")
                break
            elif confirm_customer_entry == 'N':
                print()
                break

        while True:
            option_2_end = input("Press 1 to enter another customer or END to exit: ").upper()
            if option_2_end == '1':
                is_entering_new_customer = True
                break
            elif option_2_end == "END":
                with open('constants.dat', "w") as r:
                    r.write(f'{employee_num}\n')
                    r.write(f'{customer_num}\n')
                    r.write(f'{item_num}\n')
                    r.write(f'{dependent_num}\n')
                    r.write(f'{purchase_num}\n')
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
                    r.write(f'{dependent_num}\n')
                    r.write(f'{purchase_num}\n')
                    r.write(f'{HST}\n')
                break


def new_purchase():
    global purchase_num, HST
    is_entering_new_purchase = True

    hst_accum = float(0)
    cost_accum = float(0)
    total_accum = float(0)

    while True:
        while is_entering_new_purchase:

            while True:
                p_f_name = input("Customer First Name: ").capitalize()
                if len(p_f_name) == 0:
                    print("Nothing was entered, please try again.")
                else:
                    break

            while True:
                p_l_name = input("Customer Last Name: ").capitalize()
                if len(p_l_name) == 0:
                    print("Nothing was entered, please try again.")
                else:
                    break

            customer_found = False
            with open('customers.dat', 'r') as p:
                for customerdataline in p:
                    customerline = customerdataline.split(",")

                    p_customer_num = customerline[0].strip().replace(" ", "", 0)
                    p_c_first_name = customerline[1].strip().replace(" ", "", 0)
                    p_c_last_name = customerline[2].strip().replace(" ", "", 0)

                    if p_c_first_name == p_f_name and p_c_last_name == p_l_name:
                        customer_found = True

            if not customer_found:
                is_entering_new_purchase = False
                print()
                print("Customer not found, Please try again")
                print()
            while customer_found:

                while True:
                    try:
                        p_num = int(input("Number of Purchases: "))
                        break
                    except ValueError:
                        print("Invalid input, Please try again")


                if p_num > 0:
                    p_list = []
                    p_list_item_name = []
                    p_list_item_branch = []
                    p_list_item_cost = []
                    p_list_item_HST = []
                    p_list_item_total = []
                    for x in range(p_num):
                        print("    ----------------")

                        while True:
                            p_branch = input(f"    Purchase {x + 1} Branch #: ")
                            if len(p_branch) == 0:
                                print("Nothing was entered, please try again.")
                            elif not p_branch.isdigit():
                                print("Invalid branch, please enter a valid branch number.")
                            else:
                                break

                        while True:
                            p_item_name = input(f"    Purchase {x + 1} Item Name: ")
                            if len(p_item_name) == 0:
                                print("Nothing was entered, please try again.")
                            else:
                                break

                        while True:
                            try:
                                p_item_cost = float(input(f"    Purchase {x + 1} Item Cost: "))
                                break
                            except ValueError:
                                print("Invalid input, please try again.")

                        p_hst = float(p_item_cost * HST)
                        p_total = float(p_item_cost + p_hst)

                        cost_accum += p_item_cost
                        hst_accum += p_hst
                        total_accum += p_total

                        p_info_record = f"{p_branch}, {p_item_name}, {p_item_cost}"
                        p_list.append(p_info_record)
                        p_list_item_name.append(f"{p_item_name}")
                        p_list_item_branch.append(f"{p_branch}")
                        p_list_item_cost.append(f"{p_item_cost}")
                        p_list_item_HST.append(f"{p_hst}")
                        p_list_item_total.append(f"{p_total}")

                elif p_num <= 0:
                    print("Error: Must have at least one purchase, please try again")
                    print()
                    break

                print(f"CUSTOMER NAME:                          {p_f_name} {p_l_name}")
                print(f"CUSTOMER NUMBER:                        {p_customer_num}")
                print(f"TOTAL PURCHASES:                        {p_num}")
                for x in range(p_num):
                    out_item_cost = float(p_list_item_cost[x])
                    out_item_HST = float(p_list_item_HST[x])
                    out_item_total = float(p_list_item_total[x])
                    print()
                    print(f"  PURCHASE {x + 1} NAME:                               {p_list_item_name[x]}")
                    print(f"  PURCHASE {x + 1} BRANCH:                             {p_list_item_branch[x]}")
                    print(f"  PURCHASE {x + 1} COST:                               {f'${out_item_cost:>,.2f}'}")
                    print(f"  PURCHASE {x + 1} HST:                                {f'${out_item_HST:>,.2f}'}")
                    print(f"  PURCHASE {x + 1} TOTAL:                              {f'${out_item_total:>,.2f}'}")
                print()
                print("-------------------------------------------------------------")
                print(f"COST:                            {f'${cost_accum:,.2f}':>9}")
                print(f"HST:                             {f'${hst_accum:,.2f}':>9}")
                print(f"TOTAL:                           {f'${total_accum:,.2f}':>9}")
                print()
                is_entering_new_purchase = False
                customer_found = False

                while True:
                    confirm_purchase = input("Confirm customer purchase(s)? (Y/N): ").upper()
                    if confirm_purchase == 'Y':
                        print(f"Saving purchase record for customer {p_f_name} {p_l_name}")
                        with open('purchases.dat', 'a') as p:
                            for x in range(p_num):
                                p.write(f"{purchase_num}, {today}, {p_f_name}, {p_l_name}, {p_list[x]}\n")
                                purchase_num += 1
                            break
                    elif confirm_purchase == 'N':
                        break
                    else:
                        print("Invalid confirm purchase input, please try again.")

            while True:
                option_4_end = input("Press 1 to enter a new purchase record, or END to exit: ")
                if option_4_end == '1':
                    is_entering_new_purchase = True
                    print()
                    break
                elif option_4_end == 'END':
                    with open('constants.dat', "w") as r:
                        r.write(f'{employee_num}\n')
                        r.write(f'{customer_num}\n')
                        r.write(f'{item_num}\n')
                        r.write(f'{dependent_num}\n')
                        r.write(f'{purchase_num}\n')
                        r.write(f'{HST}\n')
                    break
                else:
                    print("Invalid input, Please try again.")

        if not is_entering_new_purchase:
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
                new_customer()
                break
            elif menu_choice == 3:
                print("")
                new_item()
                break
            elif menu_choice == 4:
                print("")
                new_purchase()
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
