from brownie import Paciente,Permissao
from scripts.help import get_account,get_contract
import scripts.ipfs as ipfs
from scripts.paciente import paciente
import random
import os

class hospital:
    def __init__(self,nome):
        try:
            os.mkdir('./dados/hosp/'+nome)
        except:
            pass

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
            return (contrato1,contrato2)

    def geraPront(self,paciente):
        data=str(random.randint(1,28))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1920,2021))
        dados=paciente.nome+'-'+data+'-'+self.nome

        path='./dados/hosp/'+self.nome+'/'+dados+'.txt'
        print(path)

        try:
            pront=open(path,'x')
        except:
            pront=open(path,'w')

        modelo=open('./dados/modelo.txt')
        for linha in modelo:
            linha=linha.replace('\n','')

            if 'Patient Id' in linha:
                linha+=paciente.nome
                print(linha)
            elif 'Date' in linha:
                linha+=data
                print(linha)
            elif 'Hospital Id' in linha:
                linha+=self.nome

            pront.write(linha+'\n')

        return(path,dados)
            
    #Hospital adiciona prontuario para contrato paciente se tiver permissao
    def add_prontuario(self,paciente,dados,cid):
        #ipfs
        #dados=info extraida do prontuario
        #cid =ipfs.add(file)
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
        print('Cids Disponibilizados pelo Paciente ',paciente,p,'para o',self.nome,'\n')
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
        file=open('./dados/hosp/'+hosp.nome+'/infos.txt','r')
        for linha in file:
            l=linha.split('; ')
            self.pacientes[l[0]]=[l[1],l[2],l[3].split(',')]
        self.salvaPacientes()
        
    def importaPacientes(self):
        try:
            file=open('./dados/hosp/'+self.nome+'/infos.txt','x')
        except:
            pass
        try:
            file=open('./dados/hosp/'+self.nome+'/infos.txt','x')
        except:
            pass
        pacientes={}
        file=open('./dados/hosp/'+self.nome+'/infos.txt','r')
        for linha in file:
            l=linha.split('; ')
            pacientes[l[0]]=[l[1],l[2],l[3].split(',')]
        return pacientes

    def salvaPacientes(self):
        file=open('./dados/hosp/'+self.nome+'/infos.txt','w')
        for paciente in self.pacientes.keys():
            dados=''
            for dado in self.pacientes[paciente][2]:
                dados+=dado+','
            s=str(paciente)+'; '+str(self.pacientes[paciente][0])+'; '+str(self.pacientes[paciente][1])+'; '+dados[:-1]+'; \n'
            file.write(s)
        file.close()


    