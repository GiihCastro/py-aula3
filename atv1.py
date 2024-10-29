produtos = (
    ("Arroz", 25.50, 100),
    ("Feijão", 10.00, 50),
    ("Macarrão", 5.00, 200),
    ("Açúcar", 4.50, 150),
    ("Sal", 2.00, 300),
    ("Óleo", 6.00, 80),
    ("Leite", 3.20, 120),
    ("Café", 15.00, 40),
    ("Biscoito", 7.50, 70),
    ("Sabão", 8.00, 60)
)

soma_total = 0

maior_produto = produtos[0]

menor_produto = produtos[0]

for produto_da_vez in produtos:
    soma_total += produto_da_vez[1]

    media = soma_total / len(produtos)
    
    if produto_da_vez[1] > maior_produto[1]:
        maior_produto = produto_da_vez
    if produto_da_vez[1] < menor_produto[1]:
        menor_produto = produto_da_vez

print(f"""
    O produto mais caro é o {maior_produto[0]}, custando {maior_produto[1]} reais.
    O produto mais barato é o {menor_produto[0]}, custando {menor_produto[1]} reais.
    O valor médio de um produto na loja é de {media:,.2f} reais
    """) 