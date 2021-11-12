from brownie import  Paciente,Permissao
from scripts.help import get_account, get_contract
from scripts.ipfs import add,cat

def addMember(hosp):
    account=get_account('paciente')
    contrato=get_contract(Paciente)
    contrato.addMember(get_account(hosp),{"from": account})
    print(hosp,' pode adicionar prontuarios para este paciente')

def removeMember(hosp):
    account=get_account('paciente')
    contrato=get_contract(Paciente)
    contrato.removeMember(get_account(hosp),{"from": account})
    print(hosp,' não pode adicionar prontuarios para este paciente')

#Retorna a lista de chaves dos Prontuarios 
def get():
    account=get_account('paciente')
    contrato=get_contract(Paciente)
    r=contrato.get({"from": account})
    for x in range(len(r)):
        print(x,' - ',r[x][0])
    return r

#printa o Prontuario escolhido
def get_pront():
    r=get()
    if len(r)>0:
        x=int(input('Digite um valor valido\n'))
        while x>len(r) or x<0:
            x=int(input('Digite um valor valido\n'))
        #print('\n',r[x][1],'\n')
        return r[x][1]
    else:print('Nenhum prontuario salvo')

def addCombinacao(hosp,cid):
    account=get_account('paciente')
    combinado=str(get_account(hosp))+str(account)
    contrato=get_contract(Permissao)
    contrato.addPront(combinado,cid,{"from": account})
    print('Combinacao Adicionada - Permissao adicionada para',hosp)

def removeCombinacao(hosp):
    account=get_account('paciente')
    contrato=get_contract(Permissao)
    contrato.removeMember(hosp,{"from": account})
    print('Acesso revogado para',hosp)

def main():
    #addMember('hospital')

    cid=get_pront()
    addCombinacao('hospital',cid)
    
    cid=get_pront()
    addCombinacao('hospital',cid)
    #removeCombinacao('hospital')
    #removePerm(get_account('hospital'))
    

#tirar remove de dados - fazer remover acesso