def game():
    comp_score = {}
    comp_final_score = []
    comp_showing_score = []


    def comp_batting():
        print("\nIts your Bowling")
        a = 0
        while comp in('Batting') :
            ba = int(input("Enter a number = "))
            n = 0
            boa = random.randint(1,6)
            n = n + boa
            print ("computer = " , end = '')
            print(boa)
            if ba == boa :            
                print ("\nOut\n")
                print ("You need " , end = '')
                print(((a)+1) , end = '')
                print(" runs to win")
                print("\nIts your Batting")
                b = 0
                while b<=a:
                    ba = int(input("Enter a number = "))
                    m = 0
                    m = m + ba
                    boa = random.randint(1,6)
                    print ("computer = " , end = '')
                    print(boa)
                    if ba == boa :
                        print ("\nOut\n")
                        print("Your score is " , end = '')
                        print(b)
                        if a < b :
                            print("YOU WIN")
                        elif a == b :
                            print("ITS TIE")
                        else:
                            print("YOU LOSE")
                        break
                    else:
                        score.update({ba:boa})
                        final_score.append(m)
                        b = sum(final_score)
                        if b>a:
                            print("\nYour score " , end = '')
                            print(b)
                            print("YOU WIN")    
                break
               
            else:            
                comp_score.update({ba:boa})
                comp_final_score.append(n)
                a = sum(comp_final_score)
           
    def bowling():
        print("\nIts your Bowling")
        a = 0
        while ask in('bowl'):  
            ba = int(input("Enter a number = "))#your bowling
            n = 0
            boa = random.randint(1,6)
            n = n + boa
            print ("computer = " , end = '')
            print(boa)
            if ba == boa :
                print ("\nOut\n")
                print("Computer's score is " , end = '')
                print((a))
                print ("You need " , end = '')
                print(((a)+1) , end = '')
                print(" runs to win")
                print("\nIts your Batting")
                b = 0
                while b<=a:
                    ba = int(input("Enter a number = "))
                    m = 0
                    boa = random.randint(1,6)
                    m = m + ba
                    print ("computer = " , end = '')
                    print(boa)
                    if ba == boa :
                        print ("\nOut\n")
                        print("Your score is " , end = '')
                        print(b)
                        if a < b :
                            print("YOU WIN")
                        elif a == b :
                            print("ITS TIE")
                        else:
                            print("YOU LOSE")
                        break
                    else:
                        score.update({ba:boa})
                        final_score.append(m)
                        b = sum(final_score)
                        if b>a:
                            print("\nYour score " , end = '')
                            print(b)
                            print("YOU WIN")
                break
            else:
                comp_score.update({ba:boa})
                comp_final_score.append(n)
                a = sum(comp_final_score)
         
    score = {}
    final_score = []
    showing_score = []

    def batting():
        print("\nIts your Batting")
        a = 0
        while ask in ('bat'):
            ba = int(input("Enter a number = "))#requesting the number of batting form the user
            n = 0
            n = n + ba
            boa = random.randint(1,6)
            print ("computer = " , end = '')
            print(boa)
            if ba == boa :
                print ("\nOut\n")
                print("Your score is " , end = '')
                print((a))
                print("Computer needs " , end = '')
                print(((a)+1) , end = '')
                print(" runs to win")
                print("\nIts your Bowling")
                b = 0
                while b<=a:
                    ba = int(input("Enter a number = "))
                    m = 0
                    boa = random.randint(1,6)
                    m = m + boa
                    print ("computer = " , end = '')
                    print(boa)
                    if ba == boa :
                        print ("\nOut\n")
                        print("Computer's score is " , end = '')
                        print(b)
                        if a > b :
                            print("YOU WIN")
                        elif a == b :
                            print("ITS TIE")
                        else:
                            print("YOU LOSE")
                        break
                    else:
                        comp_score.update({ba:boa})
                        comp_final_score.append(m)
                        b = sum(comp_final_score)
                        if b>a:
                            print("\nComputer's score " , end = '')
                            print(b)
                            print("YOU LOSE")
                break
               
            else:
                score.update({ba:boa})
                final_score.append(n)
                a = sum(final_score)
               
    def comp_bowling():    
        print("\nIts your Batting")
        a = 0
        while comp in ('Bowling'):
            ba = int(input("Enter a number = "))
            n = 0
            n = n + ba
            boa = random.randint(1,6)
            print ("computer = " , end = '')
            print(boa)
            if ba == boa :
                print ("\nOut\n")
                print("Your score is " , end = '')
                print ((a))
                print("Computer needs " , end = '')
                print(((a)+1) , end = '')
                print(" runs to win")
                print("\nIts your Bowling")
                b = 0
                while b<=a:
                    ba = int(input("Enter a number = "))
                    m = 0
                    boa = random.randint(1,6)
                    m = m + boa
                    print ("computer = " , end = '')
                    print(boa)
                    if ba == boa :
                        print ("\nOut\n")
                        print("Computer's score is " , end = '')
                        print(b)
                        if a > b :
                            print("YOU WIN")
                        elif a == b :
                            print("ITS TIE")
                        else:
                            print("YOU LOSE")
                        break
                    else:
                        comp_score.update({ba:boa})
                        comp_final_score.append(m)
                        b = sum(comp_final_score)
                       
                        if b>a:
                            print("\nComputer's score " , end = '')
                            print(b)
                            print("YOU LOSE")
                break
            else:
                score.update({ba:boa})
                final_score.append(n)
                a = sum(final_score)
                           

    toss_list = ['Batting' , 'Bowling']
    print(('-' * 20) + "HAND CRICKET" + ('-' * 20))
    print("Rules:\nYou can choose number from 1 to 6 only\nThats the only rule ENJOY:)")
    start = input("Choose odd or even \nWrite o to choose odd and e to choose even \n>>>")
    start = start.lower()

    if start in ('o') or ('e'):
        aint = int(input("Enter your number: "))
        import random
        compaint = random.randint(1,6)
        print(compaint)
        ans = (aint) + (compaint)
        print(ans)
        if ans % 2 == 0 :
            print("Even")
            if start in ('o'):            
                print ("You lost the toss")
                comp = random.choice(toss_list)
                print("Computer chooses " + comp)
                if comp in ('Batting'):              
                    comp_batting()
                if comp in ('Bowling'):
                    comp_bowling()
            else:
                print ("You won the toss")
                ask = input("Choose Batting or Bowling \nFor Batting type Bat for Bowling type Bowl\n>>>")
                ask = ask.lower()
                if ask in ('bat'):
                    batting()
                if ask in ('bowl'):
                    bowling()
                   
             
                   
                       

        else:
            print("Odd")
            if start in ('e'):
                print ("You loss the toss")
                comp = random.choice(toss_list)
                print("Computer chooses " + comp)
                if comp in ('Batting'):
                    comp_batting()
                if comp in ('Bowling'):
                      comp_bowling()
            else:
                print ("You won the toss")
                ask = input("Choose Batting or Bowling \nFor Batting type Bat for Bowling type Bowl\n>>>")
                ask = ask.lower()
                if ask in ('bat'):
                    batting()
                if ask in ('bowl'):
                       bowling()


game()

