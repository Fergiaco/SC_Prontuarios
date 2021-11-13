from brownie import  Paciente,Permissao
from scripts.help import get_account,get_contract
from scripts.ipfs import add,cat
class paciente:
    def __init__(self,nome):
        self.nome=nome
        self.contratos=[]

    def addMember(self,hosp):
        account=get_account(self.nome)
        contrato=get_contract(self.contratos[0],Paciente)
        try:
            contrato.addMember(hosp,{"from": account})
            print(hosp,' pode adicionar prontuarios para este paciente')
        except:
            print("Esse hospital já tem permissao")

    def removeMember(self,hosp):
        account=get_account(self.nome)
        contrato=get_contract(self.contratos[0],Paciente)
        contrato.removeMember(get_account(hosp),{"from": account})
        print(hosp,' não pode adicionar prontuarios para este paciente')

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
        r=self.get()
        if len(r)>0:
            x=int(input('Digite um valor valido\n'))
            while x>len(r) or x<0:
                x=int(input('Digite um valor valido\n'))
            #print('\n',r[x][1],'\n')
            return r[x][1]
        else:print('Nenhum prontuario salvo')

    def addCombinacao(self,hosp,cid):
        account=get_account(self.nome)
        combinado=str(get_account(hosp))+str(account)
        contrato=get_contract(self.contratos[1],Permissao)
        contrato.addPront(combinado,cid,{"from": account})
        print('Combinacao Adicionada - Permissao adicionada para',hosp)

    def removeCombinacao(self,hosp,cid):
        account=get_account(self.nome)
        combinado=str(get_account(hosp))+str(account)
        contrato=get_contract(self.contratos[1],Permissao)
        try:
            contrato.removePront(combinado,cid,{"from": account})
            print(hosp,'perdeu o Acesso do',cid)
        except:
            print('esse hospital já está sem Permisssao')