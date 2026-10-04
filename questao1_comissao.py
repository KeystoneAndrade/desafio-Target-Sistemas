import json

arquivo = open("vendas.json", encoding="utf-8")
dados = json.load(arquivo)
arquivo.close()

comissoes = {}

for venda in dados["vendas"]:
    nome = venda["vendedor"]
    valor = venda["valor"]

    if valor < 100:
        comissao = 0
    elif valor < 500:
        comissao = valor * 0.01
    else:
        comissao = valor * 0.05

    if nome not in comissoes:
        comissoes[nome] = 0
    comissoes[nome] += comissao

for nome in comissoes:
    print(nome, "- comissao: R$", round(comissoes[nome], 2))
