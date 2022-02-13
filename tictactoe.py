#game of tic tac toe
l=[1,2,3,4,5,6,7,8,9]
win1=False
win2=False

    



print('-----------TIC TAC TOE--------------------')
print('\n'*5)
print('player1 = X\nplayer2 = O')
print('\n'*5)


print(l[0],'  ',l[1],'  ',l[2])
print('\n')
print(l[3],'  ',l[4],'  ',l[5])
print('\n')
print(l[6],'  ',l[7],'  ',l[8])
print('\n'*3)

k=0
i=0
j=0
while k<9:
    for a in l:
        if a in range (0,10):
            position1=int(input('player 1, enter the position you would like to insert the X\n'))
            print('\n'*3)
            m=0
            n=0

            while i<6 and m<9:
                if l[m]==position1:
                    l[m]='X'
                    print(l[0],'  ',l[1],'  ',l[2])
                    print('\n')
                    print(l[3],'  ',l[4],'  ',l[5])
                    print('\n')
                    print(l[6],'  ',l[7],'  ',l[8])
                    if l[0]==l[1]==l[2]:
                        print('player 1 has won')
                        win1=True
                    elif l[3]==l[4]==l[5]:
                        print('player 1 has won')
                        win1=True
                    elif l[6]==l[7]==l[8]:
                        print('player 1 has won')
                        win1=True
                    elif l[0]==l[3]==l[6]:
                        print('player 1 has won')
                        win1=True
                    elif l[1]==l[4]==l[7]:
                        print('player 1 has won')
                        win1=True
                    elif l[2]==l[5]==l[8]:
                        print('player 1 has won')
                        win1=True
                    elif l[0]==l[4]==l[8]:
                        print('player 1 has won')
                        win1=True
                    elif l[2]==l[4]==l[6]:
                        print('player 1 has won')
                        win1=True
                if win1==True:
                    quit()
                    
                else:
                    m=m+1
            if j<4:
                position2=int(input('player 2, enter the position you would like to insert the O\n'))
                print('\n'*3)
            while j<4 and n<9:
                if l[n]==position2:
                    l[n]='O'
                    print(l[0],'  ',l[1],'  ',l[2])
                    print('\n')
                    print(l[3],'  ',l[4],'  ',l[5])
                    print('\n')
                    print(l[6],'  ',l[7],'  ',l[8])
                    if l[0]==l[1]==l[2]:
                        print('player 2 has won')
                        win2=True
                    elif l[3]==l[4]==l[5]:
                        print('player 2 has won')
                        win2=True
                    elif l[6]==l[7]==l[8]:
                        print('player 2 has won')
                        win2=True
                    elif l[0]==l[3]==l[6]:
                        print('player 2 has won')
                        win2=True
                    elif l[1]==l[4]==l[7]:
                        print('player 2 has won')
                        win2=True
                    elif l[2]==l[5]==l[8]:
                        print('player 2 has won')
                        win2=True
                    elif l[0]==l[4]==l[8]:
                        print('player 2 has won')
                        win2=True
                    elif l[2]==l[4]==l[6]:
                        print('player 2 has won')
                        win2=True
                if win2==True:
                    quit()
                else:
                    n=n+1
            i=i+1
            j=j+1
        elif a not in range(0,10):
            k=k+1



    









    









    





