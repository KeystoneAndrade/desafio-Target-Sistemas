from datetime import datetime, date

valor = float(input("Valor: ").replace(",", "."))
vencimento = input("Data de vencimento (dd/mm/aaaa): ")
vencimento = datetime.strptime(vencimento, "%d/%m/%Y").date()

dias = (date.today() - vencimento).days

if dias > 0:
    juros = valor * 0.025 * dias
else:
    dias = 0
    juros = 0

print("Dias em atraso:", dias)
print("Juros: R$", round(juros, 2))
print("Total a pagar: R$", round(valor + juros, 2))
