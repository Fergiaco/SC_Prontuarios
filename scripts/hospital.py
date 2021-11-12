from brownie import  Paciente,Permissao
from scripts.help import get_account, get_contract
from scripts.ipfs import add,cat

#Hospital cria ficha referente ao paciente
def cria_ficha(paciente):
    account=get_account('hospital')
    contrato=Paciente.deploy(paciente,{"from": account})
    contrato2=Permissao.deploy(paciente,{"from": account})
    print('=========== Ficha criado para o paciente ',paciente,'===========')
    

#Hospital adiciona prontuario para contrato paciente se tiver permissao
def add_prontuario(dados,cid):
    account=get_account('hospital')
    contrato=get_contract(Paciente)
    contrato.add(dados,cid,{"from": account})
    print('=========== Prontuario adicionado ',dados,'===========')
    return contrato

def get(paciente):
    account=get_account('hospital')
    p=get_account(paciente)
    combinado=str(account)+str(p)
    contrato=get_contract(Permissao)
    r=contrato.get(combinado,{"from": account})
    print(r)


def main():
    #cria_ficha(get_account('paciente'))
    #add_prontuario('dados1','ciddados1')
    #add_prontuario('dados2','ciddados2')
    get('paciente')
    