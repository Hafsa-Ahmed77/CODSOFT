from tkinter import messagebox
import random
def play_game():
    messagebox.showinfo('Rock Paper Scissors Game',"Welcome to the Rock Paper Scissors game\nFollowing are the rules for this game:\nRock beats scissors, scissors beat paper, and paper beats rock.")
    choices=['rock','scissors','paper',]
    comp_score = 0
    play_score = 0
    while True:
        comp_choice = random.choice(choices)
        play_choice=input('enter your choice : ').lower()
        if play_choice not in ['rock','paper','scissors']:
            messagebox.showerror('ERROR!','Please select between rock, paper and scissors')
        
        else:
            messagebox.showinfo('choice locked', f'your choice is {play_choice} and computer choice is {comp_choice}')
            if (play_choice=='rock' and comp_choice=='scissors' ) or (play_choice=='scissors' and comp_choice=='paper' ) or (play_choice=='paper' and comp_choice=='rock'):
                play_score += 1
                messagebox.showinfo('Game Result', f'Congratulations! You Win!\nYour score is {play_score}')
            elif(play_choice == comp_choice):
                messagebox.showinfo('ohno',"It's a tie")
            else:
                comp_score += 1
                messagebox.showinfo('Game Result',f'You lose\nComputer score is {comp_score}')
        again=input('Do you wanna play again? : ').lower()
        if again!='yes':
            print("******************************************")
            print(f"Thanks for playing\nYour score is {play_score} while computer's score is {comp_score} ")
            if comp_score > play_score :
                 print("Computer won the game  \nGOODBYE!")
                 print("******************************************")
                 break
            elif comp_score < play_score :
                 print("Yohoooo!! You won the game  \nGOODBYE!")
                 print("******************************************")
                 break
            else:
               print("This match was a tie ")
               print("******************************************")
               break
          
        else:
             continue
play_game()
