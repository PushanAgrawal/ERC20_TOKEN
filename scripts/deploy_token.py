 


from brownie import DUToken, accounts
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000 , 'ether')

def main():
     account = get_account()
     DU_token = DUToken.deploy(initial_supply, {'from':account})
     print(DU_token.name())