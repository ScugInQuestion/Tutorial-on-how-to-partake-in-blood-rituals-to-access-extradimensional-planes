import time
import random

class Sailor():
    def __init__(self):
        self.Weapon=["Construction hammer","Knife","Bat","Spear","Shortsword","Combat Knife","Rapier","Mace","Warhammer","Zweihander"]
        self.Wounds=0
        self.Stamina=10
        self.Status="Fine"
        self.Tendancies=["Stoat","Magpie","Hare"]
        self.LastStand=False
        self.Dead=False

    def Attack(self):
        if Weapon=="Bare Hands":
            Attack=1
    
    def Death(self):
        if Wounds>=10:
            if self.Tendancies=="Stoat":
                LastStand=True
            elif Stamina<3:
                LastStand=True
            else:
                Dead=True

    def WhoAreYou(self):
        print("You are a Sailor-class seaman with",self.Wounds,"damage sustained,",self.Stamina,"Stamina left, are currently",self.Status,". You have the tendancies of the",random.choice(self.Tendancies),"and are armed with a",random.choice(self.Weapon),".")


class Boarder():
    def __init__(self):
        self.Tier=random.randint(1,5)
        self.Weapon1=["Bare Hands","Bare Hands","Bare Hands","Construction hammer","Knife","Bat"]
        self.Weapon2=["Construction hammer","Knife","Bat"]
        self.Weapon3=["Spear","Shortsword","Combat Knife"]
        self.Weapon4=["Rapier","Mace","Warhammer","Zweihander"]
        self.Weapon5=["Whipsword","Grand Gavel","Jousting Lance"]
        self.Wounds=0
        self.MaxLife=random.randint(1,5)*self.Tier+self.Tier
        self.Life=self.MaxLife
        self.Stamina=5
        self.Status="Fine"
        self.Dead=False
        
        

    def Death(self):
        if Wounds>=MaxLife:
            Dead=True

    def WhoAmI(self):
        if self.Tier==1:
            print("This is an oarsman-grade seaman with ",self.MaxLife," Health,",self.Wounds,"Damage sustained and a",random.choice(self.Weapon1),".")
        if self.Tier==2:
            print("This is a sailor-grade seaman with ",self.MaxLife," Health,",self.Wounds,"Damage sustained and a",random.choice(self.Weapon2),".")
        if self.Tier==3:
            print("This is a corsair-grade seaman with ",self.MaxLife," Health,",self.Wounds,"Damage sustained and a",random.choice(self.Weapon3),".")
        if self.Tier==4:
            print("This is a quartermaster-grade seaman with ",self.MaxLife," Health,",self.Wounds,"Damage sustained and a",random.choice(self.Weapon4),".")
        if self.Tier==5:
            print("This is a captain-grade seaman with ",self.MaxLife," Health,",self.Wounds,"Damage sustained a",random.choice(self.Weapon5),".")

class Event():
    def __init__(self):
        self.Textlist=["You find nothing.","You find another seaman.","You find a small building of unknown make or model."]
        self.Text="Placeholder"
        self.Combat=False

    def randomizeEvent(self):
        self.Text=random.choice(self.Textlist)

    def EventOutput(self):
        print(self.Text)
        
        
    def IsCombat(self):
        if self.Text=="You find another seaman.":
            self.Combat=True
        else:
            self.Combat=False
E=Event()   

class Choice():
    def __init__(self):
        self.Choice="Placeholder"


    def ChoiceInput(self):
        self.Choice=input("[ACTION HERE] ")

    def ChoiceResult(self):
        if E.Text=="You find nothing." or "You find a small building of unknown make or model.":
            if self.Choice=="Walk"or"Run"or"Move"or"Advance"or"Progress":
                E.randomizeEvent()
                E.EventOutput
        elif E.Combat==True:
            B=Boarder()
            return(B)
            if self.Choice=="Swing"or"Slash"or"Cut"or"Cleave"or"Bash":
                if S.Weapon=="Construction hammer"or"Knife"or"Bat":
                    B.Life-=1
                    E.Text=="You manage to inflict a minor wound."
                    E.EventOutput()
            if B.Life<=0:
                E.Combat==False
        else:
           print("Such an option is not availible. (Check for typos)")
           print(E.Text)

C=Choice()    
        
        

print("You open your eyes for the very first time, you are under a sea of blood.")
time.sleep(3)
print("You swim up, the knowledge of drowning and how to swim almost being instinctual.")
time.sleep(3)
print("You breach the surface, exhausted but alive.")
time.sleep(1.5)
print("You get up.")
time.sleep(1.5)
S=Sailor()
S.WhoAreYou()
time.sleep(3)

E.randomizeEvent()
E.EventOutput()
while True:
    C.ChoiceInput()
    C.ChoiceResult()

        
