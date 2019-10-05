# defining all the global variables
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
winner = None
who_won = None
player = "X"


#displaying the board in desired format
def display_board() :
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])
display_board()  


#function to flip player
def flip_player() :
  global player
  if (player == "X"):
    player = "O"
  else:
   player = "X"  
  


# function to play the game
def play_game() :
  global player 
  any = input("Player " + player + ",select empty cell on board (1 and 9): ")
  any = int(any) -1  
  if (board[int(any)] != "-"):
    print("Select another cell")
    play_game()
  else:  
    board[int(any)] = player 
    display_board()


#function to check a win across row
def row_win() :
  global winner
  global who_won
  if(board[0] == board[1] == board [2] != "-"):
   winner = True
   who_won = str(board[0])
  elif(board[3] == board[4] == board [5] != "-"):
   winner =True
   who_won = str(board[3])
  elif(board[6] == board[7] == board [8] != "-"):
    winner = True 
    who_won = str(board[6])
  else:
    return()  


#function to check a win across column
def col_win() :
  global winner
  global who_won
  if(board[0] == board[3] == board [6] != "-"):
   winner = True
   who_won = str(board[0])
  elif(board[1] == board[4] == board [7] != "-"):
   winner =True
   who_won = str(board[1])
  elif(board[2] == board[5] == board [8] != "-"):
    winner = True 
    who_won = str(board[2])
  else:
    return()  


#function to check a win across diagonals
def diagonal_win() :
  global winner
  global who_won
  if(board[0] == board[4] == board [8] != "-"):
   winner = True
   who_won = str(board[0])
  elif(board[2] == board[4] == board [6] != "-"):
   winner =True
   who_won = str(board[2])
  else:
    return()      


#check if there is a tie 
def tie():
  global board
  global winner
  global who_won
  if '-' not in board:
    winner = True
    print("111")
    who_won = "Nodody"

#here the turns takes place till there is a winner.
def the_game() :

  while (winner == None):
    play_game()
    row_win()
    col_win()
    diagonal_win()
    tie()
    if(winner != True):
      flip_player()
  
  print(who_won + " wins.")  
  

the_game()



#decide a tie
#overite issue






 



