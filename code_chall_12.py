def play_game(usrr_inp):

    usrr_inp= input("To start this game please input p or to stop this game input q : ")

    while True:

     if  usrr_inp == "p":
        print("Hello")
        usrr_inp = input("To start this game please input p or to stop this game input q : ")
     elif usrr_inp == "q":
         print("you pressed q so game is over ")
         break
     else:
         #print("To start this game please input p or to stop this game input q")
         usrr_inp = input("To start this game please input p or to stop this game input q : ")



play_game("usrr_inp")