from brownie import accounts, config, network, Paciente, Contract
from brownie.network.account import PublicKeyAccount

#Retorna versao mais recente do contrato 
def get_contract(contract_name):
    if len(contract_name)>0:
        contract = contract_name[-1]
        return contract
    else:
        print('Contrato ainda n foi deployado')
        exit()

def get_account(conta):
    return accounts.add(config["wallets"][conta])

def main():
    print(get_contract(Paciente))