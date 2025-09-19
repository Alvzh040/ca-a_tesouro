import random

# Configuração do mapa
map_size = 10
treasure_x, treasure_y = random.randint(0, map_size - 1), random.randint(0, map_size - 1)
player_x, player_y = 0, 0

print("Bem-vindo ao jogo de Caça ao Tesouro!")
print("Você é representado por '@' e o tesouro está escondido no mapa.")

# Função para exibir o mapa
def display_map():
    for y in range(map_size):
        for x in range(map_size):
            if x == player_x and y == player_y:
                print("@", end=" ")
            else:
                print(".", end=" ")
        print()

# Jogo principal
while True:
    display_map()
    move = input("Digite sua jogada (w: cima, s: baixo, a: esquerda, d: direita): ").lower()

    if move == "w" and player_y > 0:
        player_y -= 1
    elif move == "s" and player_y < map_size - 1:
        player_y += 1
    elif move == "a" and player_x > 0:
        player_x -= 1
    elif move == "d" and player_x < map_size - 1:
        player_x += 1
    else:
        print("Movimento inválido. Tente novamente.")

    # Verifica se encontrou o tesouro
    if player_x == treasure_x and player_y == treasure_y:
        print("Parabéns! Você encontrou o tesouro!")
        break
