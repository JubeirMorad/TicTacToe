
import os 
def clear():
    os.system("cls")
    # for clean console ;
class Menu:
    
    def start_menu(self): # 
        print("""Welcome  in ( tic tac toe ) .
Press 1 to start game :
Press 2 to exit game :""")
        choice=input("")
        return choice
     
    def end_menu(self): 
        print("""Game over !!
Press 1 to restart game :
Press 2 to exit game :""")
        choice=input("")
        return choice 
    
class Players :

    def __init__ (self):
        self.name="" # player's name
        self.symbol="" # player's symbol x , o or other
        
        
    def choose_name(self):
        while True:
            name=input("Please enter your name (only letters) :")
            
            if name.isalpha() : # name shoude be letters  
                self.name=name
                break 
            else :
                print("Wrong !! please enter only LETTERS :\n")
                 

    def choose_symbol(self):
        while True :
            symbol=input("Please enter your sympol ( X , O  'or other..' )").upper()
            if symbol.isalpha() and len(symbol)==1  : # symbol shoude be a letter
                self.symbol=symbol
                break
            else:
                print("Invalid choose enter only letter please !!!")    

class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)] # this is the board which we will print 

    def update_board(self,choice,symbol): # choice = number which player choosed , symbol = symbol which player choosed x , o other
        if self.is_valid_move(choice): # in line 59
            self.board[choice-1]=symbol # if player choose box 1 this box change to symbol of player else return false
            return True
        return False
    
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit() # if box = digit return true else return false
    
    def display_board(self): # to display board in console
        for x in range(0,9,3):
            print(" | ".join(self.board[x:x+3]))
            if x < 6 :
                print("-"*9)

    def reset_board(self):
        self.board=[str(i) for i in range(1,10)] # in end game we need to return board 

class Game :
    def __init__(self):
        self.players = [Players(),Players()] # for 2 player
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0 # 
        self.treis = 0 # treis == 9 , game over
        self.namelist=[] # to save names of players 
        self.symbollist = [] # to save symbols of players

    def start_game(self):
        if self.menu.start_menu() == "1" : # in line 9
            clear()
            self.setup_player() # in line 90 
            clear()
            self.play_game() # in line 113
        else :
            self.quit_game() # in line 110

    def setup_player(self):       
        for i , person in enumerate(self.players,1) :
            print(f"\nPlayer {i} enter your details :")
            while True : # name of player1 != name of player2
                person.choose_name()
                if person.name not in self.namelist :                 
                    self.namelist.append(person.name)
                    while True : # symbol of player1 != symbol of player2
                        person.choose_symbol()
                        if person.symbol not in self.symbollist :
                            self.symbollist.append(person.symbol)
                            break
                        else :
                            print("\n!!! This symbol exist choose another symbol !!!")
                    break
                else :
                    print("\n!!! This name exist choose another name !!!")
                


    def quit_game(self):
        print("*** Than you for playing .***")

    def play_game(self):
        while True :
            self.play_turn() # in line 168
            if self.check_win() or self.check_drow():
                self.board.display_board()
                if self.check_win()==True : # one of players win , in line 131
                    if self.treis%2 ==0 : # if resulte == 0 this mean player2 won else player1 won 
                        print(f"**** {self.players[1].name} , IS THE WINNER ****")
                    else:
                        print(f"**** {self.players[0].name} , IS THE WINNER ****")
                    break
                if self.check_drow()==True :# in line 141
                    print("**** NO WINNER ****")
                print("\nThank you for playing .\n")
                break
        self.end_game()

        
    def check_win(self): # focus now
        for x in range(0,9,3):
            if self.board.board[x]==self.board.board[x+1]==self.board.board[x+2] :
                return True
        for x in range(0,3):
            if self.board.board[x]==self.board.board[x+3]==self.board.board[x+6]:
                return True
        if self.board.board[0]==self.board.board[4]==self.board.board[8] or  self.board.board[2]==self.board.board[4]==self.board.board[6]:
            return True
        return False
    def check_drow(self):
        if self.treis == 9 and self.check_win() == False :
            return True
        else:
            return False
        
    def default_data(self): # we return the data to the starting point in order to restart the game
        self.board.reset_board() # in line 68
        self.treis=0 
        self.current_player_index=0
        self.namelist=[]
        self.symbollist=[]

    def end_game(self):
        print("""\nPress 1 to return game :
Press 2 to restart game :
Press other key to exit game :""")
        choice = input ("")
        self.default_data()
        clear()
        if choice == "1" :
            self.play_game()
        elif choice =="2" :
            self.start_game()
        else :
            self.quit_game()
        
    
    def play_turn(self):
        player = self.players[self.current_player_index] # self.current_player_index == 0 for player1 and 1 for player2
        self.board.display_board()
        print(f"{player.name} you can turn {player.symbol}")
        while True :
            try:
                choice =int(input("Choose a number from the list :")) 
                if 1 <= choice <= 9 and self.board.update_board(choice,player.symbol) :
                    break
                else :
                    print("Invalid choice try again !!!! ")
            except ValueError :
                print("Please choose number between 1 - 9 :")
        self.treis += 1
        self.current_player_index = 1 - self.current_player_index
        clear()



game = Game().start_game() # run the game



