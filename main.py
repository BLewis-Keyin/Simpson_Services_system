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
EMPLOYEE_NUM = int(f.readline().strip())
CUSTOMER_NUM = int(f.readline().strip())
ITEM_NUM = int(f.readline().strip())
DEPENDENT_NUM = int(f.readline().strip())
PURCHASE_NUM = int(f.readline().strip())
HST = float(f.readline().strip())
f.close()

# define province list
provlist = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']


def new_employee():
    global EMPLOYEE_NUM, e_entry_confirmed
    global DEPENDENT_NUM
    is_entering_new_employee = True
    while is_entering_new_employee:
        print("SIMPSON CARPET WORLD\nEMPLOYEE REGISTRATION\n:")

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
        print(f"EMPLOYEE NUMBER:                          {EMPLOYEE_NUM}")
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
                        f"{EMPLOYEE_NUM}, {e_first_name}, {e_last_name}, {e_address}, {e_city}, {e_province}, {e_telephone}, {e_date_of_hire}, {e_branch}, {e_title}, {e_salary}, {e_num_dep}\n")
                    EMPLOYEE_NUM += 1
                    print("Employee information saved\n")

                if e_num_dep > 0:
                    with open('dependents.dat', 'a') as g:
                        for x in range(e_num_dep):
                            g.write(f'{DEPENDENT_NUM}, {e_first_name}, {e_last_name}, {dependent_list[x]}\n')
                            DEPENDENT_NUM += 1
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
                    r.write(f'{EMPLOYEE_NUM}\n')
                    r.write(f'{CUSTOMER_NUM}\n')
                    r.write(f'{ITEM_NUM}\n')
                    r.write(f'{DEPENDENT_NUM}\n')
                    r.write(f'{PURCHASE_NUM}\n')
                    r.write(f'{HST}\n')
                break


def new_customer():
    global CUSTOMER_NUM
    global purchases_num
    is_entering_new_customer = True
    while is_entering_new_customer:
        print("SIMPSON CARPET WORLD\nCUSTOMER REGISTRATION\n:")
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
        print(f"CUSTOMER NUMBER:                          {CUSTOMER_NUM}")
        print(f"CUSTOMER BIRTH DATE:                      {c_date_of_birth}")
        print(f"DATE OF JOINING:                          {c_date_of_joining}")
        print(f"BRANCH JOINED AT:                         {c_branch}")

        while True:
            confirm_customer_entry = input("Confirm customer information? (Y/N): ").upper()
            if confirm_customer_entry == 'Y':
                is_entering_new_customer = False
                with open('customers.dat', 'a') as c:
                    c.write(
                        f"{CUSTOMER_NUM}, {c_first_name}, {c_last_name}, {c_address}, {c_city}, {c_province}, {c_telephone}, {c_date_of_birth}, {c_date_of_joining}, {c_branch}\n")
                CUSTOMER_NUM += 1
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
                    r.write(f'{EMPLOYEE_NUM}\n')
                    r.write(f'{CUSTOMER_NUM}\n')
                    r.write(f'{ITEM_NUM}\n')
                    r.write(f'{DEPENDENT_NUM}\n')
                    r.write(f'{PURCHASE_NUM}\n')
                    r.write(f'{HST}\n')
                break


def new_item():
    is_entering_new_item = True
    global ITEM_NUM

    while is_entering_new_item:
        print("SIMPSON CARPET WORLD\nINVENTORY ITEM REGISTRATION\n:")

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

        print(f"ITEM NUMBER:                              {ITEM_NUM}")
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
                    e.write(f"{ITEM_NUM}, {i_name}, {i_type}, {i_desc}, {i_colour}, {i_size}, {i_pattern}, {i_cost}, {i_retail}, {i_qoh}, {i_reorder}, {i_max}\n")
                    ITEM_NUM += 1
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
                    r.write(f'{EMPLOYEE_NUM}\n')
                    r.write(f'{CUSTOMER_NUM}\n')
                    r.write(f'{ITEM_NUM}\n')
                    r.write(f'{DEPENDENT_NUM}\n')
                    r.write(f'{PURCHASE_NUM}\n')
                    r.write(f'{HST}\n')
                break


def new_purchase():
    global PURCHASE_NUM, HST
    is_entering_new_purchase = True

    hst_accum = float(0)
    cost_accum = float(0)
    total_accum = float(0)

    while True:
        while is_entering_new_purchase:
            print("SIMPSON CARPET WORLD\nPURCHASE RECORD REGISTRATION\n")

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

                    p_c_first_name = customerline[1].strip().replace(" ", "", 0)
                    p_c_last_name = customerline[2].strip().replace(" ", "", 0)
                    if p_c_first_name == p_f_name and p_c_last_name == p_l_name:
                        p_CUSTOMER_NUM = customerline[0].strip().replace(" ", "", 0)
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
                print(f"CUSTOMER NUMBER:                        {p_CUSTOMER_NUM}")
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
                                p.write(f"{PURCHASE_NUM}, {today}, {p_f_name}, {p_l_name}, {p_list[x]}\n")
                                PURCHASE_NUM += 1
                            break
                    elif confirm_purchase == 'N':
                        break
                    else:
                        print("Invalid confirm purchase input, please try again.")

            while True:
                option_4_end = input("Press 1 to enter a new purchase record, or END to exit: ").upper()
                if option_4_end == '1':
                    is_entering_new_purchase = True
                    print()
                    break
                elif option_4_end == 'END':
                    with open('constants.dat', "w") as r:
                        r.write(f'{EMPLOYEE_NUM}\n')
                        r.write(f'{CUSTOMER_NUM}\n')
                        r.write(f'{ITEM_NUM}\n')
                        r.write(f'{DEPENDENT_NUM}\n')
                        r.write(f'{PURCHASE_NUM}\n')
                        r.write(f'{HST}\n')
                    break
                else:
                    print("Invalid input, Please try again.")

        if not is_entering_new_purchase:
            break

def print_employee_list():
    with open("employee.dat", "r") as l:
        print(f"SIMPSON CARPET WORLD\nEMPLOYEE LIST\n")
        print(f"EMPLOYEE          EMPLOYEE          DATE OF         EMPLOYEE        EMPLOYEE      EMPLOYEE ")
        print(f" NUMBER             NAME             HIRE            BRANCH           PH #         TITLE ")
        print(f"=============================================================================================")

        employee_counter = 0
        employee_branch_1_counter = 0
        employee_branch_2_counter = 0
        employee_branch_3_counter = 0
        employee_branch_4_counter = 0
        employee_branch_5_counter = 0

        # start of the employee list for loop
        for employeedataline in l:
            dataline = employeedataline.split(",")

            l_EMPLOYEE_NUM = dataline[0].strip().replace(" ", "", 0)
            l_e_first_name = dataline[1].strip().replace(" ", "", 0)
            l_e_last_name = dataline[2].strip().replace(" ", "", 0)
            l_e_telephone = dataline[6].strip().replace(" ", "", 0)
            l_e_doh = dataline[7].strip().replace(" ", "", 0)
            l_e_branch = dataline[8].strip().replace(" ", "", 0)
            l_e_title = dataline[9].strip().replace(" ", "", 0)

            if l_e_branch == '1':
                employee_branch_1_counter += 1
            if l_e_branch == '2':
                employee_branch_2_counter += 1
            if l_e_branch == '3':
                employee_branch_3_counter += 1
            if l_e_branch == '4':
                employee_branch_4_counter += 1
            if l_e_branch == '5':
                employee_branch_5_counter += 1
            employee_counter += 1

            print(f"    {l_EMPLOYEE_NUM:<2s}           {f'{l_e_first_name:<.6s} {l_e_last_name:<.6s}':<13s}    {l_e_doh:<10s}           {l_e_branch}           {l_e_telephone:<10s}    {f'{l_e_title:^.13s}':<13s}")
        print("=============================================================================================")
        print(f"BRANCH #                                      EMPLOYEES")
        print(f"BRANCH 1:                                         {employee_branch_1_counter}")
        print(f"BRANCH 2:                                         {employee_branch_2_counter}")
        print(f"BRANCH 3:                                         {employee_branch_3_counter}")
        print(f"BRANCH 4:                                         {employee_branch_4_counter}")
        print(f"BRANCH 5:                                         {employee_branch_5_counter}")
        print(f" TOTAL NUM EMPLOYEES:     {employee_counter}")
        print()

        input("Press any key to return to the main menu... : ")


def print_customers_by_branch():
    customer_branch_counter = 0
    with open("customers.dat", "r") as j:
        branch_select = input("Enter branch number: ")
        print()
        print(f"SIMPSON CARPET WORLD\nCUSTOMER LIST FOR BRANCH # {branch_select}\n")
        print(f"CUSTOMER          CUSTOMER          DATE OF         CUSTOMER        CUSTOMER        CUSTOMER      CUSTOMER")
        print(f" NUMBER             NAME             JOIN             DOB             PH #            CITY        PROVINCE")
        print(f"==============================================================================================================")
        for customerdataline in j:
            customerline = customerdataline.split(",")

            p_CUSTOMER_NUM = customerline[0].strip().replace(" ", "", 0)
            p_c_first_name = customerline[1].strip().replace(" ", "", 0)
            p_c_last_name = customerline[2].strip().replace(" ", "", 0)
            p_c_branch = customerline[9].strip().replace(" ", "", 0)
            p_c_dob = customerline[7].strip().replace(" ", "", 0)
            p_c_tel = customerline[6].strip().replace(" ", "", 0)
            p_c_doj = customerline[8].strip().replace(" ", "", 0)
            p_c_city = customerline[4].strip().replace(" ", "", 0)
            p_c_prov = customerline[5].strip().replace(" ", "", 0)
            if p_c_branch == branch_select:
                print(f"   {p_CUSTOMER_NUM:<4s}         {f'{p_c_first_name:<.7s} {p_c_last_name:<.8s}':<16s}   {p_c_doj:<10s}      {p_c_dob:<10s}      {p_c_tel:<10s}       {f'{p_c_city:<.10s}':<10s}      {p_c_prov:<2s} ")
                customer_branch_counter += 1
        if customer_branch_counter == 0:
            print(f"                          No customers found in branch {branch_select}")
        print(f"==============================================================================================================")
        print(f"TOTAL CUSTOMERS BRANCH # {branch_select}: {customer_branch_counter}")
        print()

        input("Press any key to return to the main menu... : ")

def print_orders_by_customer():
    customer_order_counter = 0
    customer_total_accum = 0
    with open("purchases.dat", "r") as u:
        customer_select_f = input("Enter customer first name: ").capitalize()
        customer_select_l = input("Enter customer last name: ").capitalize()
        print()
        print(f"SIMPSON CARPET WORLD\nPURCHASES LIST FOR {customer_select_f.upper()} {customer_select_l.upper()}\n")
        print(f"PURCHASE          CUSTOMER          DATE OF         PURCHASED FROM        ITEM        ITEM")
        print(f" NUMBER             NAME            PURCHASE            BRANCH            NAME        COST")
        print(
            f"===============================================================================================")
        for purchasesdataline in u:
            purchasesline = purchasesdataline.split(",")

            l_PURCHASE_NUM = purchasesline[0].strip().replace(" ", "", 0)
            l_p_date = purchasesline[1].strip().replace(" ", "", 0)
            l_p_f_name = purchasesline[2].strip().replace(" ", "", 0)
            l_p_l_name = purchasesline[3].strip().replace(" ", "", 0)
            l_p_branch = purchasesline[4].strip().replace(" ", "", 0)
            l_p_item_name = purchasesline[5].strip().replace(" ", "", 0)
            l_p_item_cost = float(purchasesline[6].strip().replace(" ", "", 0))
            if l_p_f_name == customer_select_f and l_p_l_name == customer_select_l:
                print(
                    f"   {l_PURCHASE_NUM:<4s}           {f'{l_p_f_name:<.7s} {l_p_l_name:<.8s}':<16s} {l_p_date:<10s}             {l_p_branch:<1s}        {f'{l_p_item_name:<.16s}':<16s}    {f'${l_p_item_cost:>,.2f}':<10s} ")
                customer_order_counter += 1
                customer_total_accum += l_p_item_cost
        if customer_order_counter == 0:
            print(f"                       No purchases found for customer {customer_select_f.upper()} {customer_select_l.upper()}")
        print(
            f"===============================================================================================")
        print(f"TOTAL ORDERS FROM CUSTOMER {customer_select_f.upper()} {customer_select_l.upper()}: {customer_order_counter}")
        print(f"TOTAL COST: {f'${customer_total_accum:<,.2f}'}")
        print()

        input("Press any key to return to the main menu... : ")



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
                print_employee_list()
                break
            elif menu_choice == 6:
                print("")
                print_customers_by_branch()
                break
            elif menu_choice == 7:
                print("")
                print_orders_by_customer()
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
