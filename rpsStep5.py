#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players, and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players in this game"""

class Player:
    def __init__(self):               # dunder init method sets all newly created cats to neutral, no needs for second variable input
        self.round_counter = 0
 
 #       self.player1_previous = 'paper'
     
    def move(self):
        return 'rock'

 #   def learn(self, my_move, their_move):
 #       self.player1_previous = my_move
 #       self.player2_previous = their_move
 #       print(f"player1_previous = {self.player1_previous}")
 #       print(f"player2_previous = {self.player2_previous}")
 #       return(self.player1_previous, self.player2_previous)
 
# a player that chooses it's move at random, called by play_round()
class RandomPlayer(Player):                              # 2. create a player subclass that plays randomly from moves[]
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):                                # 4. create a human player subclass
    def move(self):
        move = input("Your move! rock, paper or scissors ? > ")
        return(move)

class ReflectPlayer(Player):                       # 5. create a player subclass that reflects the Human Player's  previous move

    player1_previous = None

    def learn(self, my_move, their_move):
        self.player1_previous = my_move
        self.player2_previous = their_move
        print(f"player1_previous = {self.player1_previous}")
        print(f"player2_previous = {self.player2_previous}")
 #       return(self.player1_previous, self.player2_previous)
        return(self.player1_previous, self.player2_previous)
 
    def move(self): 
        if self.player1_previous is None:
            move = moves[0]
        else:                          
            move = self.p1.previous_move
        return(move)

class CyclePlayer(Player):                                # 5. create a player subclass that cycles through the moves[]
    def move(self):
        move = moves[self.round_counter]
        self.round_counter += 1
        return(move)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.winner = 0                                     # initialize scorekeeping variables
        self.p2.winner = 0
    
    def keep_score(self, p1, p2):                              # 3. keep score 
        self.p1.winner = self.p1.winner + p1                   # update scores for player 1 and player 2
        self.p2.winner = self.p2.winner + p2
        return(self.p1.winner, self.p2.winner)

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        ReflectPlayer.learn(self, move1, move2)
       #self.p2.learn(move2, move1)
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        if (move1 == move2):                            # winner = tie
 #           winner = "Tie"
            print(f"{move1} and {move2} are the same")
            print(f" ** TIE GAME **")
            
        elif (beats(move1, move2)) == True:             # winner = player 1
 #           winner = "Player 1"
            self.keep_score(1, 0)
 #           self.p1.winner += 1
            print(f"{move1} beats {move2}.")
          #  print(f"  Running Score: Player 1: {self.p1.winner} Player 2: {self.p2.winner}")
        else:                                            # winner = player 2
 #           winner = "Player 2"
            self.keep_score(0, 1)
            print(f"{move2} beats {move1}.")
          #  print(f"  Running Score: Player 1: {self.p1.winner} Player 2: {self.p2.winner}")
        print(f"  Running Score: Player 1: {self.p1.winner} Player 2: {self.p2.winner}")

    def play_game(self):
        print("Game start!")
        for round in range(1,4):             # changed range to get rid of "round 0"
            print(f"-- Round {round} -------")
            self.play_round()
        print(f"  **FINAL SCORE -- Player 1: {self.p1.winner}   Player 2: {self.p2.winner} **")
        print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()