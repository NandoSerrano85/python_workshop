#!/usr/bin/env python2
# Project 4
class game:
    answer = ""
    show = list()
    guess = 0
    player_1 = {"Name": "", "wins": 0, "loses": 0,}
    player_2 = {"Name": "", "wins": 0, "loses": 0,}

    def __init__(self, answer, players):
        self.answer = answer
        if len(players) == 1:
            self.player_1["Name"] = players[0]
            self.guess = int(raw_input("Enter maximum number of guesses: "))
        else:
            self.player_1["Name"] = players[0]
            self.player_2["Name"] = players[1]
            self.guess = int(raw_input("Enter maximum number of guesses: "))
        for n in range(0, len(answer)):
            self.show.append('-')
        
    def single(self, num):
        if num == self.guess:
            last = raw_input("Enter your guess: ")
            if last == self.answer:
                self.player_1["wins"] = self.player_1["wins"] + 1
                print "Word was: " + self.answer
                print "Congradulations you win"
            else:
                self.player_1["loses"] = self.player_1["loses"] + 1
                print "Word was: " + self.answer
                print "Sorry you lose"
            cont = raw_input("Try again(yes/no)? ")
            if cont == "yes":
                single(0)
            elif cont == "no":
                return self.player_1
        letter = raw_input("Guess a letter (" + str(num+1) + " out of " + str(self.guess) + "). Enter $ to guess word: ")
        if len(letter) == 1:
            i = 0
            if letter in self.answer:
                while i < len(self.answer):
                    i = self.answer.find(letter, i)
                    if i == -1:
                        break
                    self.show[i] = letter
                    i = i+1
            print ''.join([str(x) for x in self.show]).upper()
            self.single(num+1)
        else:
            print "please enter a single letter only!!!\n\n"
            self.single(num)

    def multi(self, num):
        print "Player 1: " + self.player_1
        attempt = raw_input("Do you want to try to answer the whole word(yes/no)? ")
        if attempt == self.answer or num == self.guess:
            last = raw_input("Enter your guess: ")
            if last == self.answer:
                self.player_1["wins"] = self.player_1["wins"] + 1
                print "Word was: " + self.answer
                print "Congradulations you win"
            else:
                self.player_1["loses"] = self.player_1["loses"] + 1
                print "Word was: " + self.answer
                print "Sorry you lose"
        letter = raw_input("Guess a letter (" + str(num+1) + " out of " + str(self.guess) + "). Enter $ to guess word: ")
        if len(letter) == 1:
            i = 0
            if letter in self.answer:
                while i < len(self.answer):
                    i = self.answer.find(letter, i)
                    if i == -1:
                        break
                    self.show[i] = letter
                    i = i+1
            print ''.join([str(x) for x in self.show]).upper()

        print "Player 2: " + self.player_2
        attempt = raw_input("Do you want to try to answer the whole word(yes/no)? ")
        if attempt == self.answer or num == self.guess:
            last = raw_input("Enter your guess: ")
            if last == self.answer:
                self.player_2["wins"] = self.player_2["wins"] + 1
                print "Word was: " + self.answer
                print "Congradulations you win"
            else:
                self.player_2["loses"] = self.player_2["loses"] + 1
                print "Word was: " + self.answer
                print "Sorry you lose"
            cont = raw_input("Try again(yes/no)? ")
            if cont == "yes":
                self.multi(0)
            elif cont == "no":
                return self.player_1, self.player_2
        letter = raw_input("Guess a letter (" + str(num+1) + " out of " + str(self.guess) + "). Enter $ to guess word: ")
        if len(letter) == 1:
            i = 0
            if letter in self.answer:
                while i < len(self.answer):
                    i = self.answer.find(letter, i)
                    if i == -1:
                        break
                    self.show[i] = letter
                    i = i+1
            print ''.join([str(x) for x in self.show]).upper()
            self.multi(num+1)
        else:
            print "please enter a single letter only!!!\n\n"
            self.multi(num)

    def record(self,):
        with open('record/score.txt', 'w+') as output:
            

def main():
    answer = "washstand"
    players = list()
    print "Welcom to hangman\n" + "1)Single Player\n" + "2)Multiplayer\n" + "3)Rules\n" + "4)Top scores\n"
    selection = int(raw_input("Enter the number for your selection: "))
    if selection == 1:
        p_1 = raw_input("What is your name: ")
        players.append(p_1)
        single = game(answer, players)
        p1_data = single.single(0) 
    elif selection == 2:
        p_1 = raw_input("What is player 1's name: ")
        players.append(p_1)
        p_2 = raw_input("What is player 2's name: ")
        players.append(p_2)
        multiplayer = game(answer, players)
        p1_data, p2_data = multiplayer.multi(0) 

     


main()
