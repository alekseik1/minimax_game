origBoard = ["O", 1, "X", "X", 4, "X", 6, "O", "O"]
huPlayer = "O"
aiPlayer = "X"


class Move:

    def __init__(self, score=-20, index=-1):
        self.score = score
        self.index = index


def emptyIndices(board):
    return list(filter(lambda x: x != "X" and x != "O", board))


def winning(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or (board[3] == player and board[4] == player and board[5] == player) or (board[6] == player and board[7] == player and board[8] == player) or (board[0] == player and board[3] == player and board[6] == player) or (board[1] == player and board[4] == player and board[7] == player) or (board[2] == player and board[5] == player and board[8] == player) or (board[0] == player and board[4] == player and board[8] == player) or (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def minimax(newBoard, player):
    availSpots = emptyIndices(newBoard)
    if winning(newBoard, huPlayer):
        return Move(score=-10)
    elif winning(newBoard, aiPlayer):
        return Move(score=10)
    elif len(availSpots) == 0:
        return Move(score=0)
    moves = []
    for i in range(len(availSpots)):
        move = Move()
        move.index = newBoard[availSpots[i]]

        newBoard[availSpots[i]] = player

        if player == aiPlayer:
            result = minimax(newBoard, huPlayer)
            move.score = result.score
        else:
            result = minimax(newBoard, aiPlayer)
            move.score = result.score

        newBoard[availSpots[i]] = move.index

        moves.append(move)

    bestMove = -1
    if player == aiPlayer:
        bestScore = -10000
        for i in range(len(moves)):
            if moves[i].score > bestScore:
                bestScore = moves[i].score
                bestMove = i
    else:
        bestScore = 10000
        for i in range(len(moves)):
            if moves[i].score < bestScore:
                bestScore = moves[i].score
                bestMove = i
    return moves[bestMove]


def printBoard(board):
    for i in range(0, len(board), 3):
        print(board[i], '|',  board[i+1], '|', board[i+2])


def is_draw(board):
    check = True
    for i in board:
        if type(i) == int:
            check = False
    return check


def startGame():
    print('Добро пожаловать в крестики-нолики!\n'
          'Кем вы хотите играть? [1 - крестики, 0 - нолики, пустая строка - выход]')
    huPlayer = input()
    while True:
        if huPlayer == "1" or huPlayer == "0":
            break
        print("Введите '1' либо '0'")
        huPlayer = input()
    print("Начнем!")
    board = [i for i in range(9)]
    if huPlayer == "1":
        huPlayer = "X"
        aiPlayer = "O"
        printBoard(board)
        while True:
            m = int(input("Ваш ход! Куда двигаться?\n"))
            while True:
                if type(board[m]) == int:
                    break
                print("Сюда уже ходили, выберите другую клетку!")
                m = int(input())
            board[m] = huPlayer

            if is_draw(board):
                print("Ничья!")
                break
            if winning(board, aiPlayer):
                print("Победил компьютер!")
                break
            elif winning(board, huPlayer):
                print("Победил человек!")
                break

            m = minimax(board, aiPlayer)
            board[m.index] = aiPlayer
            printBoard(board)

            if winning(board, aiPlayer):
                print("Победил компьютер!")
                break
            elif winning(board, huPlayer):
                print("Победил человек!")
                break
            if is_draw(board):
                print("Ничья!")
                break
    if huPlayer == "0":
        huPlayer = "O"
        aiPlayer = "X"
        while True:
            m = minimax(board, aiPlayer)
            board[m.index] = aiPlayer
            printBoard(board)

            if is_draw(board):
                print("Ничья!")
                break
            if winning(board, aiPlayer):
                print("Победил компьютер!")
                break
            elif winning(board, huPlayer):
                print("Победил человек!")
                break

            m = int(input("Ваш ход! Куда двигаться?\n"))
            while True:
                if type(board[m]) == int:
                    break
                print("Сюда уже ходили, выберите другую клетку!")
                m = int(input())
            board[m] = huPlayer

            if is_draw(board):
                print("Ничья!")
                break
            if winning(board, aiPlayer):
                print("Победил компьютер!")
                break
            elif winning(board, huPlayer):
                print("Победил человек!")
                break


def startGameBetweenBots(firstBotMove=None):
    print('Добро пожаловать в крестики-нолики!\n'
          'Здесь боты играют с ботами!')
    print("Начнем!")
    board = [i for i in range(9)]
    if 1 == 1:
        huPlayer = "X"
        aiPlayer = "O"
        while True:
            if firstBotMove is None:
                m = minimax(board, huPlayer)
                board[m.index] = huPlayer
            else:
                m = firstBotMove
                board[m] = huPlayer
                firstBotMove = None
            printBoard(board)
            print()
            if is_draw(board):
                print("Ничья!")
                break
            if winning(board, aiPlayer):
                print("Победил бот 2!")
                break
            elif winning(board, huPlayer):
                print("Победил бот 1!")
                break

            m = minimax(board, aiPlayer)
            board[m.index] = aiPlayer
            printBoard(board)
            print()

            if winning(board, aiPlayer):
                print("Победил бот 2!")
                break
            elif winning(board, huPlayer):
                print("Победил бот 1!")
                break
            if is_draw(board):
                print("Ничья!")
                break

#startGame()
startGameBetweenBots()
