import json

arquivo = open("estoque.json", encoding="utf-8")
dados = json.load(arquivo)
arquivo.close()
produtos = dados["estoque"]

arquivo = open("movimentacoes.json", encoding="utf-8")
movimentacoes = json.load(arquivo)
arquivo.close()

while True:
    print("\nProdutos:")
    for p in produtos:
        print(p["codigoProduto"], p["descricaoProduto"], "- estoque:", p["estoque"])

    codigo = int(input("\nCodigo do produto: "))
    produto = None
    for p in produtos:
        if p["codigoProduto"] == codigo:
            produto = p

    if produto is None:
        print("Produto nao encontrado")
        continue

    tipo = input("Entrada ou saida? (E/S): ").upper()
    qtd = int(input("Quantidade: "))
    descricao = input("Descricao da movimentacao: ")

    if tipo == "E":
        tipo = "Entrada"
        produto["estoque"] += qtd
    elif tipo == "S":
        if qtd > produto["estoque"]:
            print("Nao tem estoque suficiente")
            continue
        tipo = "Saída"
        produto["estoque"] -= qtd
    else:
        print("Tipo invalido")
        continue

    id_mov = len(movimentacoes) + 1
    movimentacoes.append({"id": id_mov, "codigoProduto": codigo, "tipo": tipo, "quantidade": qtd, "descricao": descricao})

    arquivo = open("estoque.json", "w", encoding="utf-8")
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    arquivo.close()

    arquivo = open("movimentacoes.json", "w", encoding="utf-8")
    json.dump(movimentacoes, arquivo, ensure_ascii=False, indent=2)
    arquivo.close()

    print("Movimentacao", id_mov, "feita. Estoque final de", produto["descricaoProduto"], "=", produto["estoque"])

    if input("Fazer outra? (S/N): ").upper() != "S":
        break
