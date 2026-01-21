vendas = [
    {"produto": "Teclado", "preco": 150},
    {"produto": "Mouse", "preco": -10},  
    {"produto": "Monitor", "preco": 900},
    {"produto": "Fone", "preco": 0}      
]

vendas_efetuadas = []
vendas_recusadas = []
total = 0

for item in vendas:
    if item['preco'] > 0:
        vendas_efetuadas.append(item)

    else:
        vendas_recusadas.append(item)

print(f"-------- VENDAS EFETUADAS --------")
for venda in vendas_efetuadas:
    print(f"Produto: {venda['produto']} - Valor: R$ {venda['preco']}")
    total += venda["preco"]
    
print(f"A soma das vendas efetuadas são de: R$ {total}")

print(f"\n-------- VENDAS RECUSADAS --------")
for venda in vendas_recusadas:
    print(f"Produto: {venda['produto']} - Valor: R$ {venda['preco']}")






