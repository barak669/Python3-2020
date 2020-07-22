"""
---------------GLOBAL PROPS------------------
"""
rank= None
is_win= False
turn_counter= 0
play_again = "y"
x_win_counter=0
o_win_counter=0

matrix= None
x_array= None
o_array= None


"""
---------------FUNCTIONS----------------------
"""
def get_board_rank():
    global rank
    rank=int(input("Enter the rank of the board: "))



def build_matrix():
    global matrix
    global x_array
    global o_array
    global turn_counter

    turn_counter= 0
    x_array=[0 for i in range(0,rank*2+2)]
    o_array=[0 for i in range(0,rank*2+2)]
    matrix=[[(row*rank+col+1) for col in range(0,rank)] for row in range(0,rank)]



def print_board():
    global rank
    global matrix
    for row in range(0,rank):  
        for col in range(0,rank):
            print(matrix[row][col],end=" | ")
        print("\n-----------")

def get_position():
    global rank
    global matrix
    global turn_counter

    print_board()
    print(f"************ user {'X' if turn_counter%2==0 else 'O'}****************")
    return int(input("Enter the position (1 - "+ str(rank*rank)+"): "))


def check_if_win(row,col):
    global turn_counter
    global is_win
    global rank
    global x_array
    global o_array
    global x_win_counter
    global o_win_counter
    arr=x_array if turn_counter%2==0 else o_array
    arr[row]+=1
    arr[rank+col]+=1

    if row==col:
        arr[rank+rank]+=1

    if (row+col)==(rank-1):
        arr[rank+rank+1]+=1

    is_win=(arr[row]==rank) or (arr[rank+col]==rank) or (arr[rank+rank+1]==rank) or (arr[rank+rank]==rank)

    if(is_win):
        if turn_counter%2==0:
            x_win_counter+=1
        else:
            o_win_counter+=1
        print(f"{'x' if turn_counter%2==0 else 'o'} won, your total counter is: {x_win_counter if turn_counter%2==0 else 'o'}")
        print_board()
    else:
        if(turn_counter==rank*rank):
            is_win=True
            print("Game Over")



def handle_turn(position):
    global matrix
    global turn_counter
    row=(position-1)//rank
    col= (position-1) %rank

    if matrix[row][col]!='x' and matrix[row][col]!='o':
        matrix[row][col]='x' if turn_counter%2==0 else 'o'     
        check_if_win(row,col)
        turn_counter+=1
        return True
    else:
        return False




"""
---------------MAIN CODE-----------------------
"""

while play_again=="y":
    get_board_rank()
    build_matrix()

    while not is_win:
        flag=False
        while not flag:
            selectedPos=get_position()
            flag=handle_turn(selectedPos)
    

    is_win=False
    play_again=input("Do you want to play again (y or n)")