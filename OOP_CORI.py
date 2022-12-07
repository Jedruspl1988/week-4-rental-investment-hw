def cori_input(msg, error_msg):
    while True:
        try:
            user_input = input(msg)
            if user_input == "q":
                print('\nThank You and have a great day')
                break
            num = float(user_input)
            return num

        except ValueError:
            print(error_msg)
            continue

def cori_info():

    error_msg = '\nInvalid entry, please try again! Make sure entry is an number or press \'q\' to exit.\n'

    print('\nWelcome, let\'s get started with CORI:(Calculator of rental income).')
    print('\nEnter \'q\' to exit CORI at any time!')
    print('\nFirst let\'s discuss monthly income on the property')
    rent_income = cori_input('Please enter rental income now:\n', error_msg)
    storage = cori_input('Will any storage charges apply? Please enter 0 if no, otherwise enter amount now:\n', error_msg)
    laundry = cori_input('Will there be paid laundry on property? If no please enter 0 if yes enter expected monthly amount now:\n', error_msg)
    misc_income = cori_input('Please enter any other not listed above monthly income for this property:\n', error_msg)
    

    print('\nNow let\'s discuss monthly property expenses:\n')
    taxes = cori_input('Enter monthly property taxes now:\n', error_msg)
    insurance = cori_input('Enter monthly insurance payment now:\n', error_msg)
    bills = cori_input('Enter total monthly utilities bills now:\n', error_msg)
    hoa = cori_input('Enter HOA payment amount if applicable, if not enter 0:\n', error_msg)
    out_upkeep = cori_input('Enter any expected amounts for lawn and snow removal services now, if none please enter 0:\n', error_msg)
    vacancy = cori_input('Enter expected vacancy costs now, if none please enter 0: \n', error_msg) 
    repairs = cori_input('Enter expected repair costs now, if none please enter 0: \n', error_msg)
    cap_expenses = cori_input(' Enter expected Capital Expenses now, if none please enter 0:\n', error_msg)
    management = cori_input('Enter monthly amount for property management services now:\n', error_msg)
    mortgage = cori_input('Enter monthly amount for mortgage now: \n', error_msg)

    print('Now let\'s discuss Cash on Cash ROI.')
    down_payment = cori_input('Enter Down Payment amount now: \n', error_msg)
    closing = cori_input('Enter closing costs now:\n', error_msg)
    rehab = cori_input('Enter cost of rehab now:\n', error_msg)
    misc_cost = cori_input('Enter total monthly costs of any other costs not listed above now:\n', error_msg)

    total_income = rent_income + storage + laundry + misc_income
    format(total_income, '.2f')

    total_expense = taxes + insurance + bills + hoa + out_upkeep + vacancy + repairs + cap_expenses + management + mortgage
    total_investment = down_payment + closing + rehab + misc_cost
    mcf = total_income - total_expense
    annual_mcf = mcf * 12
    roi = annual_mcf / total_investment

    print(f'\n\n\n\nCORI is done, here is info on your property')
    print(f'\n\nCORI calculated ROI on this property: {int(roi*100)}%\n')
    print('\n\n\Thank You for using CORI, have a great day and good luck on your new investment')

while True:
    print('\nWelcome!, let\'s get started with CORI:(Calculator of rental income).')

    menu = input('Would you like to calculate your ROI with CORI y = yes or n = no\n')

    if menu == 'y':
        cori_info()
        break 
    elif menu =='n':
        print('\nThank You have a nice day!')
        break
    else:
        print('\n\n\nInvalid Entry please try again\n')
        menu