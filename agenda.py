import json
import os 

ARQUIVO = "contatos.json"

#------------------ Funções auxiliares -----------------#
def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f) #A função json.loads() (com 's' de string) é usada para analisar uma string JSON e convertê-la diretamente num dicionário Python, enquanto json.load() é usada para ler de um ficheiro. 
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4,ensure_ascii=False)
            
#----------------- Funcionalidades -------------------#

def adicionar_contatos(nome, telefone, email):
    contatos = carregar_contatos()
    contatos.append ({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print(f'Contato {nome} salvo com sucesso!')
    
def listar_contatos():
    contatos = carregar_contatos()
    if not contatos:
        print('Nenhum contato encontrado')
        return
    print("\n Lista de Contatos")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def remover_contatos(nome):
    contatos = carregar_contatos()
    contatos_filtrados = [c for c in contatos if c["nome"].lower() != nome.lower()] #O que acontece aqui é ele pega cada ítem no laço for e se a chave nome for diferente do parametro nome passado, ele irá guardar para a nova lista.
    if len(contatos) == len(contatos_filtrados):
        print(f'Contato {nome} não encontrado')
    else:
        salvar_contatos(contatos_filtrados)
        print(f'Contato {nome} removido com sucesso!')