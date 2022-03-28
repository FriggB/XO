from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def color (c):
    windll.Kernel32.SetConsoleTextAttribute (h, c)
def colorLine(c,s):

    color(c)
    print ("*"* (len(s)+2))
    print(" "+ s)
    print("*" * (len(s) + 2))

def intro ():
    colorLine(11, "                 Приветствую Вас на игре крестики нолики.\n"
                  "                  Выберите наиболее удобный вариант ввода:")
    colorLine(14, "1.  Ход - через выбор номера ячейки")
    print()

    doska(board)
    print()
    colorLine(14, "2 . Ход через указания координат")
    doska_v2(board_v2)
    a = int(input("Ваш выбор?"))
    if a == 1:
        main1(board)
    elif a == 2:
        main2(board_v2)
    else:
        print("Введите 1 или 2")


X="X"
O="0"

board = list(range(1, 10))
board_v2= [['-'] * 3 for _ in range (3)]
def doska_v2(f):
    color(10)
    print ('  0 1 2')
    for i in range(len(board_v2)):
        print(str(i), *board_v2[i])

def doska(board):
    color(9)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")

def take_input_v2 (f):
    while True:
        place = input(" Куда идем? (Введите 2 цифры через пробел. Первая столбец , вторая строка): ").split()
        if len(place)!= 2:
            print(" Две циферки и между ними пробел")
            continue
        if not (place [0].isdigit() & place [1].isdigit()):
            print(" Нужно выбрать 2 числа от 0 до 2")
            continue
        x,y = map(int,place)
        if not (0<=x<3 and 0 <= y < 3):
            print("Только от 0 до 2")
            continue
        if f [x] [y] != "-":
            print("Тут занято же")
            continue
        break
    return x,y


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token +"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Тут занято же")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")



def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def check_win_v2(f, user):
    board_list = []
    for d in f :
        board_list += d
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    indicet = set ([i for i, x in enumerate (board_list) if x == user ])
    for p in win_coord:
        if len(indicet.intersection(set(p))) == 3:
            return True
    return False

def main1(board):
    counter = 0
    win = False
    while not win:
        doska(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    doska(board)

def main2 (board_v2):
    counter = 0
    while True:
        if counter % 2 == 0:
            user = "X"
        else:
            user = "O"
        doska_v2(board_v2)
        x,y = take_input_v2 (board_v2)
        board_v2 [x] [y] = user
        if counter == 9:
            print ("Ничья!")
        if  check_win_v2(board_v2, user):
            print(user, "выиграл!")
            doska_v2(board_v2)
            break
        counter += 1
#main2(board_v2)
#main(board)

intro()
