from scripts.hospital import hospital
from scripts.paciente import paciente
from scripts.help import get_account
from brownie import Paciente,Permissao

#Fazer 
# Repoduzir uma transacao seguindo os passos criados
# Upload ipfs 
# criptografia

def passoInicial(p,h):
    c1,c2=h.cria_ficha(get_account(p.nome))
    p.contratos=(c1,c2)
    #da permissao para adicionar prontuarios
    p.addMember(get_account(h.nome))
    #add prontuarios
    h.add_prontuario(p.nome,'dados'+p.nome,'cid'+p.nome)
    
def visualizacaoPaciente(p):
    p.getPront()

def addPermissao(p,h):
    #da permissao 
    p.addCombinacao(h.nome)

def removePermissao(p,h):
    #remove permissao 
    p.removeCombinacao(h)

def visualizacaoHospital(p,h):
    #remove permissao 
    h.get(p.nome)
    

def main():
    p1=paciente('benno')
    p2=paciente('waldyr')
    h1=hospital('hosp_1')
    h2=hospital('hosp_2')

    #Consulta
    passoInicial(p1,h1)
    passoInicial(p2,h2)

    #dados atualizados entre hospitais
    h2.importaDados(h1)
    h1.importaDados(h2)

    #Da permissao de acesso
    addPermissao(p1,h1)
    addPermissao(p1,h2)
    addPermissao(p2,h2)
    
    #Funciona
    visualizacaoHospital(p1,h1)
    visualizacaoHospital(p1,h2)
    visualizacaoHospital(p2,h2)

    #Nao funciona
    visualizacaoHospital(p2,h1)

    removePermissao(p1,h2)

    #Nao funciona
    visualizacaoHospital(p1,h2)