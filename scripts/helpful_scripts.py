from brownie import accounts, network

FORKED_LOCAL_ENVO = ['mainnet-fork','mainnet-for-dev']
lOCAL_BLOCKCHAIN_ENVO=['development','ganache-locals']
Decimall=8
starting_price=200000000000


def get_account(index=None, id=None):
    if index:
        return accounts[index]

    if id:
        return  accounts.load(id)     
        

    if network.show_active() in lOCAL_BLOCKCHAIN_ENVO or network.show_active in FORKED_LOCAL_ENVO:
        return accounts[0]

    return  accounts.load("pushanag")      