from random import choice

options = ["piedra", "tijeras", "papel"]

#Generamos una funci[on con todas las combinaciones posibles
def search_winner(player1, player2):
    if player1 == player2:
        result = 0
    elif player1 == "piedra" and player2 == "tijeras":
        result = 1
    elif player1 == "piedra" and player2 == "papel":
        result = 2
    elif player1 == "tijeras" and player2 == "piedra":
        result = 2
    elif player1 == "tijeras" and player2 == "papel":
        result = 1
    elif player1 == "papel" and player2 == "piedra":
        result = 1
    elif player1 == "papel" and player2 == "tijeras":
        result = 2
    return result

resultado=search_winner("papel", "tijeras")
print("Gana el jugador ",resultado)

test = [
    ["piedra", "piedra", 0],
    ["piedra", "tijeras", 1],
    ["piedra", "papel", 2],
]

for partida in test:
    print ("Player 1: %s player 2: %s Winner: %s Validation: %s"
           % (
                partida[0],
                partida[1],
                search_winner(partida[0], partida[1]),
                partida[2])
           )
    
#Eleccion de player 1 de forma aleatria
def get_choice():
    return choice(options)

for i in range(10):
    player1 = get_choice()
    player2 = get_choice()
    print ("Player 1: %s Player 2: %s Winner: %s"
           % (
                player1,
                player2,
                search_winner(player1, player2)
                )
           )
    
#Inicia la red neuronal
def str_to_listo(option):
    if option == "piedra":
        res = [1, 0, 0]
    elif option == "tijeras":
        res = [0, 1, 0]
    elif option == "papel":
        res = [0, 0, 1]
    return res

data_X = list(map(str_to_listo, ["piedra", "tijeras", "papel"]))
data_y = list(map(str_to_listo, ["papel", "piedra", "tijeras"]))
print(data_X)
print(data_y)
