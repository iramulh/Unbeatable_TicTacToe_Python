from turtle import *
from turtle import _CFG
import random
from os import system

_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

pictures=["images/photo1.png", "images/photo2.png", "images/photo3.png", "images/photo4.png", "images/photo5.png", "images/photo6.png", "images/photo7.png", "images/photo8.png", "images/photo9.png", "images/photo10.png", "images/photo11.png", "images/photo12.png", "images/photo13.png", "images/photo14.png", "images/photo15.png", "images/photo16.png", "images/photo17.png", "images/photo18.png", "images/photo19.png", "images/photo20.png", "images/photo21.png", "images/photo22.png", "images/photo23.png", "images/photo24.png", "images/photo25.png", "images/photo26.png", "images/photo27.png", "images/photo28.png", "images/photo29.png", "images/photo30.png", "images/photo31.png", "images/photo32.png", "images/photo33.png", "images/photo34.png", "images/photo35.png", "images/photo36.png", ]

title("Iram\'s Tic Tac Toe Game")
hideturtle()
penup()
setup(480, 480)
color("white")
speed(5)
width(3)

def draw_board():
  """clears the window and console and draws the tic tac toe board in the window"""
  #clears the window and console
  clear()
  system("clear")

  #chooses a random color background
  bgpic(random.choice(pictures))

  #draws the box around the grid
  setheading(0)
  goto(-180, 180)
  pendown()
  goto(180, 180)
  goto(180, -180)
  goto(-180, -180)
  goto(-180, 180)
  penup()

  #draws the grid
  goto(-60, 180)
  pendown()
  goto(-60, -180)
  penup()
  
  goto(60, 180)
  pendown()
  goto(60, -180)
  penup()
  
  goto(-180, 60)
  pendown()
  goto(180, 60)
  penup()
  
  goto(-180, -60)
  pendown()
  goto(180, -60)
  penup()

  #writes the square numbers in the squares
  goto(-175, 155)
  pendown()
  write("1", font = ("FreeSans", 15, "bold"))
  penup()

  goto(-55, 155)
  pendown()
  write("2", font = ("FreeSans", 15, "bold"))
  penup()

  goto(65, 155)
  pendown()
  write("3", font = ("FreeSans", 15, "bold"))
  penup()

  goto(-175, 35)
  pendown()
  write("4", font = ("FreeSans", 15, "bold"))
  penup()

  goto(-55, 35)
  pendown()
  write("5", font = ("FreeSans", 15, "bold"))
  penup()

  goto(65, 35)
  pendown()
  write("6", font = ("FreeSans", 15, "bold"))
  penup()

  goto(-175, -85)
  pendown()
  write("7", font = ("FreeSans", 15, "bold"))
  penup()

  goto(-55, -85)
  pendown()
  write("8", font = ("FreeSans", 15, "bold"))
  penup()

  goto(65, -85)
  pendown()
  write("9", font = ("FreeSans", 15, "bold"))
  penup()

def draw_move (move, box):
  """takes a move and square number and draws the move in the square"""

  #sets the x and y coordinates depending on the selected square
  if box == 1:
    x = -120
    y = 120
  elif box == 2:
    x = 0
    y = 120
  elif box == 3:
    x = 120
    y = 120
  elif box == 4:
    x = -120
    y = 0
  elif box == 5:
    x = 0
    y = 0
  elif box == 6:
    x = 120
    y = 0
  elif box == 7:
    x = -120
    y = -120
  elif box == 8:
    x = 0
    y = -120
  elif box == 9:
    x = 120
    y = -120

  if move == "x":
    #draws the 'x' at the x and y coordinates.
    penup()
    goto(x - 40, y + 40)
    pendown()
    goto(x + 40, y - 40)
    penup()
    goto(x + 40, y + 40)
    pendown()
    goto(x - 40, y - 40)
    penup()

  elif move == "o":
    #draws the 'o' at the x and y coordinates.
    penup()
    setheading(0)
    goto(x, y - 40)
    pendown()
    circle(40)
    penup()

def draw_line(type, start):
  """takes line type and starting point and draws appropriate line from starting point to indicate the winner"""

  #determines which line to draw
  if type == "h":
    
    #sets the starting coordinates
    if start == 1:
      x = -120
      y = 120
    elif start==4:
      x = -120
      y = 0
    elif start==7:
      x = -120
      y = -120

    #draws the line from the given coordinates
    goto(x - 40, y)
    pendown()
    goto(x + 280, y)
    penup()
    
  elif type == "v":
    if start == 1:
      x = -120
      y = 120
    elif start == 2:
      x = 0
      y = 120
    elif start == 3:
      x = 120
      y = 120
    goto(x, y + 40)
    pendown()
    goto(x, y - 280)
    penup()
    
  elif type == "d":
    if start == 1:
      goto(-160, 160)
      pendown()
      goto(160, -160)
      penup()
    elif start == 3:
      goto(160, 160)
      pendown()
      goto(-160, -160)
      penup()
      

def user_move():
  """makes the user's move"""

  #prompts the user to make a move
  print("Enter a square number from 1 to 9 or \'quit\' this round: ")
  while True:
    square = input("")
    
    #checks if the input is valid
    if square.isdecimal():
      if 0 < int(square) < 10:
        
        #places an 'x' in the position in the grid list and draws an 'o' in said square if it isn't occupied already
        if grid[int(square)] == "":
          grid[int(square)] = "x"
          draw_move("x", int(square))
          return
        else:
          print("That square is already occupied. Please try again.")
      else:
        print("That is not a valid square number. Please try again. ")
    elif square.lower() == "quit":
      return square.lower()
    else:
      print("That is not a valid input. Please try again. ")

def check_winner():
  """returns who the winner is"""

  #checks if there's a winner in any of the rows and returns said winner
  if grid[1] == grid[2] == grid[3] != "":#to make sure it isn't just returning empty strings
    return grid[1]
  elif grid[4] == grid[5] == grid[6] != "":
    return grid[4]
  elif grid[7] == grid[8] == grid[9] != "":
    return grid[7]

  #checks if there's a winner in any of the columns and returns said winner
  elif grid[1] == grid[4] == grid[7] != "":
    return grid[1]
  elif grid[2] == grid[5] == grid[8] != "":
    return grid[2]
  elif grid[3] == grid[6] == grid[9] != "":
    return grid[3]

  #checks if there's a winner in any of the diagnols and returns said winner
  elif grid[1] == grid[5] == grid[9] != "":
    return grid[1]
  elif grid[3] == grid[5] == grid[7] != "":
    return grid[3]

def update_score(winner):
  """takes the winner and uses it to update the score"""
  
  global wins
  global losses
  global ties

  #draws line to indicate winner
  if grid[1] == grid[2] == grid[3] != "":
    draw_line("h", 1)
  elif grid[4] == grid[5] == grid[6] != "":
    draw_line("h", 4)
  elif grid[7] == grid[8] == grid[9] != "":
    draw_line("h", 7)

  elif grid[1] == grid[4] == grid[7] != "":
    draw_line("v", 1)
  elif grid[2] == grid[5] == grid[8] != "":
    draw_line("v", 2)
  elif grid[3] == grid[6] == grid[9] != "":
    draw_line("v", 3)

  elif grid[1] == grid[5] == grid[9] != "":
    draw_line("d", 1)
  elif grid[3] == grid[5] == grid[7] != "":
    draw_line("d", 3)

  #updates scores depending on who won the round
  if winner == "user":
    print("You win!")
    wins += 1
  elif winner == "bot":
    print("Bot wins!")
    losses += 1
  elif winner == "tie":
    print("It's a tie!")
    ties += 1

def grid_full():
  """checks if the grid is full to determine if it's a tie or not"""
  
  #checks if there are any empty strings in the grid
  if "" in grid:
    return False
  else:
    return True

def empty_squares():
  """returns a list of unoccupied squares"""
  
  squares = []

  #checks if each square is empty
  for index in range(len(grid)):
    if grid[index] == "":
      squares.append(index)
      
  return squares

def empty_corners():
  """returns a list of unoccupied corners"""

  empty_corners=[]
  
  for item in (1, 3, 7, 9):

    #finds unoccupied corners
    if item in empty_squares():
      empty_corners.append(item)
  return empty_corners

def empty_line():
  """returns a list of unoccupied squares in line with the center"""

  empty_squares = []

  if grid[2] == grid[8] == "":
    empty_squares.extend([2, 8])
  elif grid[4] == grid[6] == "":
    empty_squares.extend([4, 6])
  return empty_squares

def easy_bot():
  """beatable bot for the easy mode of the game make's moves randomly"""

  #chooses a random unoccupied square
  square = random.choice(empty_squares())

  #places an 'o' in the position in the grid list draws an 'o' in said square
  grid[square] = "o"
  draw_move("o", square)

def medium_bot():
  """semi-beatable bot for the medium mode of the game makes moves somewhat strategically"""

  #goes through each unoccupied square to see if it can make a winning move
  for item in empty_squares():

    #temporarily places an 'o' in that position
    grid[item] = "o"

    #sees if doing so lets it win
    if check_winner() == "o":

      #if yes then draws an 'o' in said square
      draw_move("o", item)
      return
    else:
      #otherwise removes the 'o' since it can't win
      grid[item] = ""

  #goes through each unoccupied square to see if it can block the user from making a winning move
  for item in empty_squares():

    #temporarily places an 'x' in that position
    grid[item] = "x"

    #sees if doing so let's the user win
    if check_winner() == "x":

      #if yes replaces it with an 'o' to block the user from winning
      grid[item] = "o"

      #draws an 'o' in said square
      draw_move("o", item)
      return
    else:

      #removes the 'x' since the user can't win
      grid[item] = ""

  #makes a random move if it can't make a winning or blocking move
  easy_bot()

def hard_bot():
  """almost unbeatable bot for the hard mode of the game makes moves completely strategically"""
  
  corners = empty_corners()
  
  #goes through each unoccupied square to see if it can make a winning move
  for item in empty_squares():

    #temporarily places an 'o' in that position
    grid[item] = "o"

    #sees if doing so lets it win
    if check_winner() == "o":

      #if yes then draws an 'o' in said square
      draw_move("o", item)
      return
    else:
      #otherwise removes the 'o' since it can't win
      grid[item] = ""

  #goes through each unoccupied square to see if it can block the user from making a winning move
  for item in empty_squares():

    #temporarily places an 'x' in that position
    grid[item] = "x"

    #sees if doing so let's the user win
    if check_winner() == "x":

      #if yes replaces it with an 'o' to block the user from winning
      grid[item] = "o"

      #draws an 'o' in said square
      draw_move("o", item)
      return
    else:

      #removes the 'x' since the user can't win
      grid[item] = ""

  #gives priority to occupying the center
  if grid[5] == "":
    grid[5] = "o"
    draw_move("o", 5)
    return
    
  #chooses a random unoccupied corner
  elif len(corners)>0:
    corner = random.choice(corners)
    grid[corner] = "o"
    draw_move("o", corner)
    return

  #makes a random move if it can't make a winning or blocking move 
  easy_bot()

def impossible_bot():
  """unbeatable bot for the hard mode of the game makes moves strategically"""
  
  #goes through each unoccupied square to see if it can make a winning move
  for item in empty_squares():

    #temporarily places an 'o' in that position
    grid[item] = "o"

    #sees if doing so lets it win
    if check_winner() == "o":

      #if yes then draws an 'o' in said square
      draw_move("o", item)
      return
    else:
      #otherwise removes the 'o' since it can't win
      grid[item] = ""

  #goes through each unoccupied square to see if it can block the user from making a winning move
  for item in empty_squares():

    #temporarily places an 'x' in that position
    grid[item] = "x"

    #sees if doing so let's the user win
    if check_winner() == "x":

      #if yes replaces it with an 'o' to block the user from winning
      grid[item] = "o"

      #draws an 'o' in said square
      draw_move("o", item)
      return
    else:

      #removes the 'x' since the user can't win
      grid[item] = ""

  #gives priority to occupying the center
  if grid[5] == "":
    grid[5] = "o"
    draw_move("o", 5)
    return

  #otherwise completes a line along the center to force the user to block them
  elif grid[5] == "o" and len(empty_line()) > 0:
    square = random.choice(empty_line())
    grid[square] = "o"
    draw_move("o", square)
    return
    
  #chooses a random unoccupied corner
  elif len(empty_corners()) > 0:
    corner = random.choice(empty_corners())
    grid[corner] = "o"
    draw_move("o", corner)
    return

  #makes a random move if it can't make a winning or blocking move 
  easy_bot()

def play_again():
  """prompts the user to play again and returns 'True' or 'False'"""

  #asks them if they want to play again
  print("\nPlay this mode again (\'yes\'/\'no\') or \'quit\' to the main menu:")
  
  while True:
    answer = input("")

    #gets their answer and returns 'True' or 'False' accordingly
    if answer.lower() == "yes":#changes their response to lowercase so that capitalization doesn't make their input invalid
      return True
    elif answer.lower() == "no" or answer.lower() == "quit":
      return False
    else:
      print("That is not a valid input. Please try again.")

def play_round():
  """plays each individual round"""
  
  while True:
    
    #gets the user's move
    user = user_move()

    #returns 'quit' if they 'quit'
    if user == "quit":
      return user

    #checks if the game is over and returns the result
    elif check_winner() == "x":
      return "user"
    elif check_winner() == "o":
      return "bot"
    elif grid_full():
      return "tie"

    #uses the appropriate bot for the selected difficulty level
    if mode == "easy":
      easy_bot()
    elif mode == "medium":
      medium_bot()
    elif mode == "hard":
      hard_bot()
    elif mode == "impossible":
      impossible_bot()
    
    if check_winner() == "x":
      return "user"
    elif check_winner() == "o":
      return "bot"
    elif grid_full():
      return "tie"

def run_game():
  """runs the code for the whole game"""

  global round
  
  while True:

    #draws the board
    draw_board()

    #adds 1 to the round
    round += 1
      
    #prints the game mode and round number
    print(mode.capitalize() + " Mode\nRound " + str(round)+"\nYou're playing as \'X\'.\n")

    #gets the result of the game by playing it
    result = play_round()

    #returns 'quit' if they 'quit'
    if result == "quit":
      return

    #updates the score with the result
    update_score(result)
    print("\nFinal Scores: \nYour Wins: "+str(wins) + "\nBot's Wins: " + str(losses) + "\nTies: " + str(ties))

    #prompts them to play again
    if play_again():
      global grid

      #resets the grid if they say yes
      grid=["y", "", "", "", "", "", "", "", "", ""]
    else:

      #exits otherwise
      return

def main_menu():
  """prompts the user to choose a difficulty level and runs the respective game"""
  
  global grid
  global mode
  global round
  global wins
  global losses
  global ties
  
  while True:

    #creates the grid that the program will use to keep track of the user's and bot's moves as a list of empty strings
    grid=["y", "", "", "", "", "", "", "", "", ""]#the first index holds a y as a placeholder so that the indices of the other items matches the square numbers of the board

    mode = ""
    round = 0
    wins = 0
    losses = 0
    ties = 0

    #prompts the user to select their difficulty level
    print("\nEnter the mode (\'easy\'/\'medium\'/\'hard\'/'impossible\') or \'quit\' the game: ")
    while True:
      answer = input("")
      if answer.lower() == "easy":
        
        #plays the easy mode of the game
        mode = "easy"
        run_game()
        break

      elif answer.lower() == "medium":

        #plays the hard mode of the game
        mode = "medium"
        run_game()
        break
        
      elif answer.lower() == "hard":

        #plays the hard mode of the game
        mode = "hard"
        run_game()
        break

      elif answer.lower() == "impossible":

        #plays the impossible mode of the game
        mode = "impossible"
        run_game()
        break
        
      elif answer.lower() == "quit":

        #quits the game if they 'quit'
        return
      else:
        print("That is not a valid input. Please try again.")

#runs the whole game
print("Welcome to Iram\'s Tic Tac Toe Game!")
main_menu()
print("See you again soon!")