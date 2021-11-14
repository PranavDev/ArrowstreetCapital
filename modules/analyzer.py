# **********************************************************************************************************************
# Author: Pranav H. Deo { phd24@umd.edu }
# Date: 11/13/2021
# Version: v1.0
# Code Description:
# Transaction Data Analysis.

# **********************************************************************************************************************

##############################################################

# Function to read the txt file for analysis
def transaction_analysis(fl):
    parsed_trx_dict = {}
    company_init_share_value = {}
    with open(fl) as f:
        lines = f.readlines()
        for line in lines:
            init_share_value(line, company_init_share_value)
        # print('Init Share Value : ', company_init_share_value)
        for line in lines:
            parse_transaction(line, parsed_trx_dict, company_init_share_value)
    print(parsed_trx_dict)
    return parsed_trx_dict
    # print(parsed_trx_dict)


def init_share_value(st, company_init):
    list_maker = st.split(" ")
    company = list_maker[8]
    value = list_maker[10]
    dollar_value = float(value.replace('$', ''))
    if company not in company_init.keys():
        company_init[company] = dollar_value


# Function to parse lines in txt file to compute
def parse_transaction(st, trx_dict, company_init):
    list_maker = st.split(' ')
    action = list_maker[4]
    shares = float(list_maker[5])
    company = list_maker[8]
    value = list_maker[10]
    dollar_value = float(value.replace('$', ''))
    Accounting(action, shares, company, dollar_value, trx_dict, company_init)


# Keep Accounts of Sold / Bought Shares
def Accounting(action, shares, company, value, trx_dict, company_init):
    # If company exists in records
    if company in trx_dict.keys():
        previous_balance = trx_dict[company][0]
        if action == 'bought':
            current_bal = previous_balance - (shares * value)
            profit_loss = trx_dict[company][1]
            trx_dict[company] = [round(current_bal, 3), profit_loss, shares]
            # print('> Bought: ', trx_dict)
        else:
            new_shares = trx_dict[company][2] - shares
            if new_shares > 0:
                current_bal = previous_balance + (shares * value)
                profit_loss = trx_dict[company][1] + (shares * value) - (shares * company_init[company])
                trx_dict[company] = [round(current_bal, 3), profit_loss, new_shares]
                # print('> Sold: ', trx_dict)
            else:
                profit_loss = trx_dict[company][1] + (shares * value) - (shares * company_init[company])
                trx_dict[company] = [round(profit_loss, 3), profit_loss, new_shares]
                # print('> Sold: ', trx_dict)
    # If company does not exist in records
    else:
        if action == 'bought':
            current_bal = - (shares * value)
            profit_loss = 0
            trx_dict[company] = [round(current_bal, 3), profit_loss, shares]
            # print('> Bought: ', trx_dict)

# **********************************************************************************************************************
