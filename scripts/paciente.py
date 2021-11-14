from brownie import  Paciente,Permissao
from scripts.help import get_account,get_contract
from scripts.ipfs import add,cat
class paciente:
    def __init__(self,nome):
        self.nome=nome
        self.contratos=()

    def addMember(self,hosp):
        account=get_account(self.nome)
        contrato=get_contract(self.contratos[0],Paciente)
        try:
            contrato.addMember(hosp,{"from": account})
            print(hosp,'pode adicionar prontuarios para',self.nome)
        except:
            print(hosp,"já tem permissao para adicionar em",self.nome)

    def removeMember(self,hosp):
        account=get_account(self.nome)
        contrato=get_contract(self.contratos[0],Paciente)
        contrato.removeMember(get_account(hosp),{"from": account})
        print(hosp,'não pode mais adicionar prontuarios para',self.nome)

    #Retorna a lista de chaves dos Prontuarios 
    def get(self):
        account=get_account(self.nome)
        contrato=get_contract(self.contratos[0],Paciente)
        r=contrato.get({"from": account})
        for x in range(len(r)):
            print(x,' - ',r[x][0])
        return r

    #printa o Prontuario escolhido
    def get_pront(self):
        print("\n===================================================")
        print('Dados do Paciente',self.nome)
        r=self.get()
        if len(r)>0:
            x=int(input('Digite um valor valido\n'))
            while x>len(r) or x<0:
                x=int(input('Digite um valor valido\n'))
            #print('\n',r[x][1],'\n')
            return r[x]
        else:print('Nenhum prontuario salvo\n')

    def addCombinacao(self,hosp):
        print("\n===================================================")
        print('Escolha o dado que deseja compartilhar com ',hosp)
        r=self.get_pront()
        info=r[0]
        cid=r[1]
        account=get_account(self.nome)
        combinado=str(get_account(hosp))+str(account)
        contrato=get_contract(self.contratos[1],Permissao)
        perms=contrato.getPronts(combinado,{"from": account})
        if cid not in perms:
            contrato.addPront(combinado,cid,{"from": account})
            print('Permissao adicionada para',hosp,' - ',info)
        else:
            print(hosp,'Já tem permissao de acesso para',info)

    def removeCombinacao(self,hosp,cid):
        print("\n===================================================")
        print('Escolha o dado que deseja revogar a permissao de',hosp)
        r=self.get_pront()
        info=r[0]
        cid=r[1]
        account=get_account(self.nome)
        combinado=str(get_account(hosp))+str(account)
        contrato=get_contract(self.contratos[1],Permissao)
        try:
            contrato.removePront(combinado,cid,{"from": account})
            print(hosp,'perdeu o Acesso do',info)
        except:
            print(hosp,'já está sem Permisssao para ',info )