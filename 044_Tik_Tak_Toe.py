import random

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|   " + row[0] + "   |   " + row[1] + "   |   " + row[2] + "   |") #Establecer el formato que se va a visualizar
        print("+-------+-------+-------+")

def enter_move(board): #Funcion para realizar un movimiento
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): ")) #Solicitar el numero de casilla en donde el usuario quiere colocar su movimiento
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] not in ("X", "O"):  # Verifica si la casilla está libre
                    board[row][col] = "O"
                    return
                else:
                    print("¡Esa casilla ya está ocupada!")
            else:
                print("¡Movimiento inválido! Debe ser un número entre 1 y 9.")
        except ValueError:
            print("¡Entrada inválida! Debes ingresar un número.")

def make_list_of_free_fields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ("X", "O"):
                free_fields.append((r, c))
    return free_fields

def victory_for(board, sign): #Funcion que verifica las casillas para definir la victoria
    # Comprobar filas
    for row in board:
        if all(cell == sign for cell in row):
            return True
    # Comprobar columnas
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    # Comprobar diagonales
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False

def draw_move(board): #Funcion para que la computadora realize un movimiento
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = random.choice(free_fields)  # Elige un movimiento aleatorio
        board[move[0]][move[1]] = "X"

def main():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # Inicializa el tablero con números
    board[1][1] = "X"  # La máquina siempre empieza en el centro
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("¡Ganaste!")
            break
        if not make_list_of_free_fields(board):
            print("¡Empate!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("¡La máquina ganó!")
            break
        if not make_list_of_free_fields(board):
            print("¡Empate!")
            break

if __name__ == "__main__":
    main()