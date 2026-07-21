# 1. criando uma lista de frutas disponiveis
frutas_disponiveis = ["banana","maca","laranja"]

# 2. criando uma tupla com informacoes sobre uma fruta
# (nome, preco, quantidade)
info_fruta = ("banana", 3.50, 20)

# 3. criando um conjunto de frutas fora de estoque
frutas_fora_de_estoque = {"maca", "kiwi"}

# 4. criando um dicionario para associar frutas a preços e quantidades
estoque = {
    "banana": {"preco": 3.50, "quantidade": 20},
    "laranja": {"preco": 2.75, "quantidade": 15},
}

#exibindo as informaçoens
print("frutas disponiveis:", frutas_disponiveis)
print("informaçoens sobre a fruta", info_fruta)
print("frutas fora de estoque:", frutas_fora_de_estoque)
print("estoque atualizado:", estoque)

# exibindo preco e quantidade da banana
print("preco da banana:", estoque["banana"]["preco"])
print("quantidade de banana:", estoque["banana"]["quantidade"])