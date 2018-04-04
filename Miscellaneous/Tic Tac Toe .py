'''
 Tic Tac Toe Game
'''




import random

# function to delay the output
def delay(val):
    x=0
    y=10000*val
    for i in range(0,y):
        x=i+x
# function for clear screen
def clrscr():
     for i in range(0,45):
         print("\t")




class tic_tac:
    arr=[' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
    player=0 # to designate the players player=1 for you & player=2 for computer
    flag=0 # to represent weather winnig condition is occured or not
    mode=0 # for two modes of the game
    name1="   "
    name2="Computer"
    win="  "
    # function to give introduction about game and to get initial data from user
    def introduction(self):
        print("    ******************>>> Welcome <<<******************* ")
        print("    ******** You are Playing Tic-Tac-Toe Game ********** ")
        print("    **************************************************** ")
        print("      In this Game Player have to Enter the Position ")
        print("        This Postion set The Player`s Mark to  ")
        print("        Given Location on Tic -Tac_Toe Board ")
        print("--- The Postions on the Tic-Tac-Toe Board Is Shown Below ---")
        print("")
        print("        ")
        for j in range(0,9):
            print("  ",j,end=' ')
            if (j==5):
                print("\n   --------------")
            elif(j==2):
                print("\n   --------------")
            elif(j!=8):
                print(":",end='')
        print("\n\n\tTIC - TAC - TOE MENU ")
        print("\t1. One Player Mode OR To Play With Computer ")
        print("\t2. Two Player Mode OR To Play With Another Player ")
        flag=1
        while(flag==1):
            try:
                self.mode=int(input("\tEnter Your Choice : "))
                if(self.mode==1):
                    self.name1=input("  Enter your name : ")
                    print(self.name1,end="")
                    ch=input(" you want to take  1st tern press (y/n) :")
                    if(ch=='y' or ch=='Y'):
                        self.player=1
                        flag=0
                        break
                    elif(ch=='n' or ch=='N'):
                        self.player=2
                        flag=0
                        break
                    break
                elif(self.mode==2):
                    self.name1=input("  Enter first player name : ")
                    self.name2=input("  Enter second player your name : ")
                    print("If ",self.name1,end="")
                    ch=input(" wants to take 1st tern press (y/n)")
                    if(ch=='y' or ch=='Y'):
                        self.player=1
                        flag=0
                        break
                    elif(ch=='n' or ch=='N'):
                        self.player=2
                        flag=0
                        break
                    break                    
            except ValueError:
                continue
                    
        
    # function to set the initial value of different data and it set the mark to desired location
    def module(self):
        self.introduction()
        i=0
        self.show_frame()
        #loop which continue upto all the position are filled or it will break if wiining condtion is encountered
        for i in range(0,9):
            if(self.player==1):
                self.player1_input()
                self.show_frame()
                self.player=2
            elif(self.player==2 and self.mode==1):
                self.com_input()
                self.show_frame()
                self.player=1
            elif(self.player==2 and self.mode==2):
                self.player2_input()
                self.show_frame()
                self.player=1
            self.check()
            self.winner()
            if(self.flag ==1):
                break
        if(i==8):# case when all the potion are filled and no player wins
            print("\n No Player win !!! It is a Tie")
            self.win="Tie"
        self.reset()    
    # this function checks the winning condtion
    def check(self):
        if(self.arr[0]==self.arr[1]and self.arr[1]==self.arr[2]and self.arr[1]!=' '):
            self.flag=1
        if(self.arr[3]==self.arr[4]and self.arr[4]==self.arr[5]and self.arr[4]!=' '):
            self.flag=1
        if(self.arr[6]==self.arr[7]and self.arr[7]==self.arr[8]and self.arr[7]!=' '):
            self.flag=1
        if(self.arr[0]==self.arr[3]and self.arr[3]==self.arr[6]and self.arr[3]!=' '):
            self.flag=1
        if(self.arr[1]==self.arr[4]and self.arr[4]==self.arr[7] and self.arr[4]!=' '):
            self.flag=1
        if(self.arr[2]==self.arr[5]and self.arr[5]==self.arr[8]and self.arr[5]!=' '):
            self.flag=1
        if(self.arr[0]==self.arr[4]and self.arr[4]==self.arr[8]and self.arr[4]!=' '):
            self.flag=1
        if(self.arr[2]==self.arr[4]and self.arr[4]==self.arr[6]and self.arr[4]!=' '):
            self.flag=1
    # this function decides who is the winner
    def winner(self):
        if(self.flag==1):# means either one of two  players wins
            if(self.player==1 and self.mode==1):# for computer player==2 but after taking input the player is set to 1
                print("\n computer wins !!! ")
                self.win=self.name2
            if(self.player==1 and self.mode==2):
                print("\n Player 2 wins !!! ")
                self.win=self.name2
            if(self.player==2 and self.mode==1):
                print("\n You wins !!! ")
                self.win=self.name1
            if(self.player==2 and self.mode==2):
                print("\n Player 1  wins !!! ")
                self.win=self.name1
    # taking input from user or player 1
    def player1_input(self):
        pos=0
        print("\n\n")
        while(1):
            try:
                if(self.mode==1):
                    print(" ",self.name1," enter the postion : ",end='')
                else:
                    print(" ",self.name1," enter the position  : ",end='')
                pos=int(input())
                if(pos>8 or pos<0):
                    continue
                elif(self.arr[pos]==' '):
                    break
            except ValueError:
                continue
        self.arr[pos]='X'
    # taking input  player 2
    def player2_input(self):
        pos=0
        print("\n\n")
        while(1):
            try:
                print(" ",self.name2," enter the position  : ",end='')
                pos=int(input())
                if(pos>8 or pos<0):
                    continue
                elif(self.arr[pos]==' '):
                    break
            except ValueError:
                continue           
        self.arr[pos]='O'
    # set which postion computer will choose
    def com_input(self):    
        pos=0
        defend=0 # defend=1 means in next tern the oponent is  going to win
        attack=0 # attack=1 means in next tern computer is going to win
        #this code checks weather in next tern oponent is going to win ,if yes then it set defend=1
        for i in range(0,9):
            if(self.arr[i]==' '):
                self.arr[i]='X'
                self.check()
                self.arr[i]=' '
                if(self.flag==1):
                    pos=i
                    defend=1
                    self.flag=0
                    break
        # this code checks weather in next tern computer is going to win ,if yes then it take that step
        for  i in range(0,9):
            if(self.arr[i]==' '):
                self.arr[i]='O'
                self.check()
                self.arr[i]=' '
                if(self.flag==1):
                    pos=i
                    attack=1
                    self.flag=0
                    break
        if(attack==1):# computer wins after this step
            self.arr[pos]='O'
            print("\n Computer choose position ",end='')
            delay(100)
            print(".",end='')
            delay(100)
            print(".",end='')
            delay(100)
            print(". ",end='')
            delay(100)                
            print(pos)
            delay(100)       
        elif(defend==1):# computer defend or stop the player to wins after this step
            self.arr[pos]='O'
            print("\n Computer choose position ",end='')
            delay(100)
            print(".",end='')
            delay(100)
            print(".",end='')
            delay(100)
            print(". ",end='')
            delay(100)                
            print(pos)
            delay(100)              
        else:# otherwisecomputer choose a random empty postion 
            while(1):
                pos=random.randint(0,8)
                if(self.arr[pos]==' '):
                    self.arr[pos]='O'
                    print("\n computer choose position ",end='')
                    delay(100)
                    print(".",end='')
                    delay(100)
                    print(".",end='')
                    delay(100)
                    print(".",end='')
                    delay(100)
                    print(pos)
                    delay(100)
                    break
    #to display the tic_tac_board alongwith the mark X & O 
    def  show_frame(self):
        clrscr()
        print("\n******<<< TIC TAC TOE GAME >>>*******")
        print("*                                   *")
        if(self.mode==1):
            print("*    You : X        Computer : O    *")
        else:
            print("*    Player 1 : X      Player 2 : O *")
        print("*                                   *")
        print("*************************************")
        print("")
        print("        ")
        for j in range(0,9):
            print("  ",self.arr[j],end=' ')
            if (j==5):
                print("\n   --------------")
            elif(j==2):
                print("\n   --------------")
            elif(j!=8):
                print(":",end='')
    # function to reset the value of different variables when game is over
    def reset(self):
        self.flag=0
        self.arr=[' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
        self.player=1
        self.flag=0
    
def main():
    obj=tic_tac()
    while(1):
        try:
            obj.module()
            ch=input("\n Want to Play again Press (y/n)")
            if(ch=='y' or  ch=='Y'):
                clrscr()
                continue
            elif(ch=='n' or ch=='N'):
                input()    
                break
                
        except ValueError:
            continue
if __name__=='__main__':
    main()
            
