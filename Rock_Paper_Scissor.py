def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player 1, Wins")
    elif(player_one[p1]=="Rock") and player_two[p2]=="Paper":
        print("Player 2, Wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player 1, Wins")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player 2, Wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player 1, Wins")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissor"):
        print("Player 2, Wins")    


player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={1:'Rock',0:'Paper',2:'Scissor'}

while(1):
   num1=input("Player 1 enter your choice")
   num2=input("Player 2 enter your choice")

   bit1=int(input("Player 1, Enter the secret bit position"))
   bit2=int(input("Player 2, Enter the secret bit position"))

   rock_paper_scissor(num1,num2,bit1,bit2)

   ch=input("Do you want to continue? Y/N")
   if(ch=='n' or ch=='N'):
     break




