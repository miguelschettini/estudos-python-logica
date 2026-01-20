precos = [100, 250, -10, 500, -5, 80]
precos_corrigidos = []
precos_ignorados = []

for preco in precos:
    if preco > 0:
       precos_corrigidos.append(preco)
    
    else:
     precos_ignorados.append(preco)
     

    
print(f'Lista corrigida: {precos_corrigidos}')
print(f'Quantidade de preços ignorados: {len(precos_ignorados)}')
print(f'Lista de preços que foram ignorados é: {precos_ignorados}')

total = sum(precos_corrigidos)
print(f'Soma dos precos corrigidos é:R$ {total}')