'''Remember how I said programmers hate the word “Automatically”? On the first day of each month, commission totals are to be calculated for each employee when the program is turned on. Identify the total sales for each employee based on the Subtotal amount in the Sales table. The commission is then calculated at 6% of sales. If the total sales for an employee is over $5,000.00, add an extra $200.00 to the commission amount. List the results in a professional manner.'''

import datetime
today = datetime.date.today()
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year


# here there would be code to read the month and year that the program was last used from constants.dat
# for now they are just manually included

RATE_COMMISSION = 0.06
month_of_last_program_use = 3
year_of_last_program_use = 2023


if month_of_last_program_use < current_month or year_of_last_program_use < current_year:
    pass
    ## code for reading sales data from previous month
    # print("EMPLOYEE COMMISSION RESULTS")
    # print(" EMPLOYEE          EMPLOYEE       COMMISSION ")
    # print("    ID               NAME           EARNED ")
    # print("====================================================")
    # While open('sales.dat", 'r') as a:
        # for salesdataline in a:
            # salesline = salesdataline.split(",")
            # employee_id = salesline[].strip
            # employee_first_name = salesline[].strip
            # employee_last_name = salesline[].strip
            # employee_sale_month = salesline[].strip
            # employee_subototal_amount = salesline[].strip

            # if employee_sale_month == month_of_last_program_use
                # employee_commission = employee_subtotal_amount * RATE_COMISSION
                # if employee_subtotal_amount > 5000:
                    # employee_comission += 200

                # print(f"   {employee_id:<4s}        {f'{employee_first_name:<8s} {employee_last_name:<7s}':<16s}    {f'${employee_comission:<,.2f}':<10s}
    # print("====================================================")

# code goes here to write constants back to the constants.dat, including the current month and current year
    # with open('constants.dat', 'w') as f:
        # f.write(f'{RATE_COMMISSION}\n')
        # f.write(f'{current_month}\n')
        # f.write(f'{current_year}\n')
        
