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
            print('\n===========Paciente ',paciente,' já tem uma ficha===========')
            return self.pacientes[paciente][0],self.pacientes[paciente][1]
        else:
            account=get_account(self.nome)
            print('\n=========== Criando ficha para o paciente ',paciente,'===========')
            contrato1=Paciente.deploy(paciente,{"from": account})
            contrato2=Permissao.deploy(paciente,{"from": account})
            print('\n=========== Ficha criada para o paciente ',paciente,'===========')
            self.pacientes[paciente]=[contrato1,contrato2,[]]
            self.salvaPacientes()
            return contrato1,contrato2
            
    #Hospital adiciona prontuario para contrato paciente se tiver permissao
    def add_prontuario(self,paciente,dados,cid):
        account=get_account(self.nome)
        p=get_account(paciente)
        if p not in self.pacientes:
            print(paciente,'Não ainda não tem uma ficha no',self.nome)
        elif dados not in self.pacientes[p][2]:
            try:
                contrato=get_contract(self.pacientes[p][0],Paciente)
                contrato.add(dados,cid,{"from": account})
                print('\n=========== Prontuario adicionado ',dados,'===========')
                self.pacientes[p][2].append(dados)
                self.salvaPacientes()
                #return contrato
            except:
                print('\nO hospital não tem permissão para adicionar esse prontuário')
        else:
            print(self.nome,'já adicionou esse prontuário para',p)

    def get(self,paciente):
        account=get_account(self.nome)
        p=get_account(paciente)
        print("\n===================================================")
        print('Cids Disponibilizados pelo Paciente ',paciente,p,'\n')
        combinado=str(account)+str(p)
        contrato=get_contract(self.pacientes[p][1],Permissao)
        try:
            r=contrato.get(combinado,{"from": account})
            print(r)
        except:
            print(self.nome,'Não tem Permissão para acessar dados do paciente',paciente,' \n')
        return r

    def importaDados(self,hosp):
        print("\n===================================================")
        print(self.nome,"- importando dados de ",hosp.nome)
        file=open('./dados/hosp/'+hosp.nome+'.txt','r')
        for linha in file:
            l=linha.split('; ')
            self.pacientes[l[0]]=[l[1],l[2],l[3].split(',')]
        self.salvaPacientes()
        

    
    def importaPacientes(self):
        try:
            file=open('./dados/hosp/'+self.nome+'.txt','x')
        except:
            pass
        pacientes={}
        file=open('./dados/hosp/'+self.nome+'.txt','r')
        for linha in file:
            l=linha.split('; ')
            pacientes[l[0]]=[l[1],l[2],l[3].split(',')]
        return pacientes

    def salvaPacientes(self):
        file=open('./dados/hosp/'+self.nome+'.txt','w')
        for paciente in self.pacientes.keys():
            dados=''
            for dado in self.pacientes[paciente][2]:
                dados+=dado+','
            s=str(paciente)+'; '+str(self.pacientes[paciente][0])+'; '+str(self.pacientes[paciente][1])+'; '+dados[:-1]+'; \n'
            file.write(s)
        file.close()


    