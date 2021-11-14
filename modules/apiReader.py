# **********************************************************************************************************************
# Author: Pranav H. Deo { phd24@umd.edu }
# Date: 11/13/2021
# Version: v1.0
# Code Description:
# Transaction Data Miner.

# **********************************************************************************************************************

##############################################################
import yaml
import requests
import random as rnd
##############################################################


def pull_data(company_list):
    with open('config/asc_trx_data.txt', 'w') as txt:
        for comp in company_list['track_list']:
            comp_data = requests.get(comp)
            data = comp_data.json()
            rand_val = rnd.uniform(5, 20)
            print('On', data['newsDate1'],
                  'ArrowStreet', 'bought', 20,
                  'shares of', data['ticker'],
                  'at', str('$'+str(round(float(str(data['currentPrice']).replace('$', '')), 4))),
                  'per share', file=txt)
            print('On', data['newsDate1'],
                  'ArrowStreet', 'sold', 15,
                  'shares of', data['ticker'],
                  'at', str('$'+str(round(float(str(data['currentPrice']).replace('$', ''))+rand_val, 4))),
                  'per share', file=txt)

# **********************************************************************************************************************
