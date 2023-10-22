#Rock Paper Scissor Game
print ('This is a simple demonstration of the game "Rock Paper Scissor" ')
print ("Either type 'Rock', 'Paper',or 'Scissor'")
player1 = input("Enter player one choice: ")
player2 = input("Enter player two choice: ")
p1 = str(player1)
p2 = str(player2)
if player1=="Rock" or player1=="Scissor" or player1=="Paper" or player2=="Rock" or player2=="Scissor" or player2=="Paper":
    if p1==p2:
        print ("It is a tie.")
    else:
        if player1=="Rock" and player2=="Paper":
            print ("Player 1 wins!")
        elif player1=="Paper" and player2=="Rock":
            print ("Player 2 wins!")
        elif player1 =="Scissor" and player2=="Rock":
            print ("Player 2 wins!")
        elif player1 =="Rock" and player2=="Scissor":
            print ("Player 1 wins!")
        elif player1 =="Scissor" and player2=="Paper":
            print ("Player 1 wins!")
        elif player1 =="Paper" and player2=="Scissor":
            print ("Player 2 wins!")
else:
    print ("You enter an invalid choice.")
    