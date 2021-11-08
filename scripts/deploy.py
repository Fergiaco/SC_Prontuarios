from brownie import  Paciente
from scripts.help import get_account, get_contract
from scripts.ipfs import add,cat


#Deploy do contrato na BC
def deploy_paciente():
    if len(Paciente)<=0:
        account=get_account('paciente')
        contrato=Paciente.deploy({"from": account})
        print('=========== Contrato deployado :) ===========')
    else:
        print('=========== Contrato ja foi deployado ===========')  
        contrato=get_contract(Paciente)
    return contrato

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
        print('\n',r[x][1],'\n')
        #print('\n',cat(r[x][1]),'\n')
    else:print('Nenhum prontuario salvo')

#Remove um prontuario da lista pelo indice
def remove():
    account=get_account('paciente')
    contrato=get_contract(Paciente)
    r=get()

    x=int(input('Digite um indice valido para remover\n'))
    while x>len(r) or x<0:
        x=int(input('Digite um indice valido para remover\n'))

    contrato.remove(x,{"from": account})
    print('Tabela Atualizada')
    get()

#adiciona um prontuario(dados,cid) na lista
def add_pront(dados,cid): 
    account=get_account('paciente')
    contrato=get_contract(Paciente)
    contrato.add(dados,cid,{"from": account})
    print(dados,'Adicionado')
    
def main():
    deploy_paciente()
    get_pront()
    add_pront('hospX - dia ...','QmbPZzJwMFvDusgRrpEdsswzwir371Av4AhGybT4gr6ZxV')
    get_pront()
    remove()