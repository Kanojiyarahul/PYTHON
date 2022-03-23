#mario game

class character():
    def __init__(self,name):
        self.name= name
        self.__life= 3
        self.__score= 0 

     
    def kicked(self):
        self.__score+=10
    def punched(self):
        self.__score +=5
        
    def stabbed(self):
        self.__life-=1

    def displaylife(self):
        return self.__life
    
    def displayscore(self):
        return self.__score

    def intro(self):
        print(f"name :{self.name.title()}")
        print(f"score : {self.__score}")
        print(f"life : {self.__life}")

while (True):
    name=input("enter your name:")
    print(f'welcome to my game{name}')

    m=character(name)
    print('press 1:punch')
    print('press 2:kick')
    print('press 3:stabb')
    print('press 4: get scoreboard')

    choice=int(input("enter choice :"))

    if choice==1:
        m.punched()
        print(f'your score is {m.displayscore()}')
    elif choice==2:
        m.kicked()
        print(f'your score is {m.displayscore()}')
    elif choice==3:
        m.stabbed()
        print(f'{m.displaylife()} lifes remaining')
    elif choice==4:
        m.intro()
               



    

 


               



    

 


               



    

 


               



    

 
