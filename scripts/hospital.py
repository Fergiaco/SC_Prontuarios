from brownie import Paciente,Permissao
from scripts.help import get_account,get_contract
from scripts.ipfs import add,cat
from scripts.paciente import paciente

class hospital:
    def __init__(self,nome):
        self.nome=nome
        self.pacientes=self.importaPacientes()

    #Hospital cria ficha para o paciente
    def cria_ficha(self,paciente):
        if paciente in self.pacientes: 
            print('===========Paciente ',paciente,' já tem uma ficha===========\n')
            return self.pacientes[paciente][0],self.pacientes[paciente][1]
        else:
            account=get_account(self.nome)
            contrato1=Paciente.deploy(paciente,{"from": account})
            contrato2=Permissao.deploy(paciente,{"from": account})
            print('=========== Ficha criada para o paciente ',paciente,'===========\n')
            self.pacientes[paciente]=[contrato1,contrato2]
            self.salvaPacientes()
            return contrato1,contrato2
            
    #Hospital adiciona prontuario para contrato paciente se tiver permissao
    def add_prontuario(self,paciente,dados,cid):
        account=get_account(self.nome)
        p=get_account(paciente)
        try:
            contrato=get_contract(self.pacientes[p][0],Paciente)
            contrato.add(dados,cid,{"from": account})
            print('=========== Prontuario adicionado ',dados,'===========\n')
            #return contrato
        except:
            print('Prontuario não Encontrado')


    def get(self,paciente):
        account=get_account(self.nome)
        p=get_account(paciente)
        combinado=str(account)+str(p)
        contrato=get_contract(self.pacientes[p][1],Permissao)
        try:
            r=contrato.get(combinado,{"from": account})
        except:
            print(self.nome,'Não tem Permissão\n')
        return r
    
    def importaPacientes(self):
        try:
            file=open('./dados/map.txt','x')
        except:
            pass
        pacientes={}
        file=open('./dados/map.txt','r')
        for linha in file:
            l=linha.split(',')
            pacientes[l[0]]=[l[1],l[2]]
        return pacientes

    def salvaPacientes(self):
        file=open('./dados/map.txt','a')
        for paciente in self.pacientes.keys():
            s=str(paciente)+','+str(self.pacientes[paciente][0])+','+str(self.pacientes[paciente][1])+'\n'
            file.write(s)
        file.close()

    