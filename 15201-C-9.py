import time
import random


class Sailor:
    Attack: int
    Weapon: list[str]
    Wounds: int
    Stamina: int
    Status: str
    Tendancies: list[str]
    LastStand: bool
    Dead: bool

    def __init__(self):
        self.Attack = 1
        self.Weapon = [
            "Construction hammer",
            "Knife",
            "Bat",
            "Spear",
            "Shortsword",
            "Combat Knife",
            "Rapier",
            "Mace",
            "Warhammer",
            "Zweihander",
        ]
        self.Wounds = 0
        self.Stamina = 10
        self.Status = "Fine"
        self.Tendancies = ["Stoat", "Magpie", "Hare"]
        self.LastStand = False
        self.Dead = False

    def DoAttack(self):
        if random.choice(self.Weapon) == "Bare Hands":
            self.Attack = 1

    def Death(self):
        if self.Wounds >= 10:
            if random.choice(self.Tendancies) == "Stoat":
                self.LastStand = True
            elif self.Stamina < 3:
                self.LastStand = True
            else:
                self.Dead = True

    def WhoAreYou(self):
        print(
            "You are a Sailor-class seaman with",
            self.Wounds,
            "damage sustained,",
            self.Stamina,
            "Stamina left, are currently",
            self.Status,
            ". You have the tendancies of the",
            random.choice(self.Tendancies),
            "and are armed with a",
            random.choice(self.Weapon),
            ".",
        )


class Boarder:
    Tier: int
    Weapon1: list[str]
    Weapon2: list[str]
    Weapon3: list[str]
    Weapon4: list[str]
    Weapon5: list[str]
    Wounds: int
    MaxLife: int
    Life: int
    Stamina: int
    Status: str
    Dead: bool

    def __init__(self):
        self.Tier = random.randint(1, 5)
        self.Weapon1 = [
            "Bare Hands",
            "Bare Hands",
            "Bare Hands",
            "Construction hammer",
            "Knife",
            "Bat",
        ]
        self.Weapon2 = ["Construction hammer", "Knife", "Bat"]
        self.Weapon3 = ["Spear", "Shortsword", "Combat Knife"]
        self.Weapon4 = ["Rapier", "Mace", "Warhammer", "Zweihander"]
        self.Weapon5 = ["Whipsword", "Grand Gavel", "Jousting Lance"]
        self.Wounds = 0
        self.MaxLife = random.randint(1, 5) * self.Tier + self.Tier
        self.Life = self.MaxLife
        self.Stamina = 5
        self.Status = "Fine"
        self.Dead = False

    def Death(self):
        if self.Wounds >= self.MaxLife:
            self.Dead = True

    def WhoAmI(self):
        if self.Tier == 1:
            print(
                "This is an oarsman-grade seaman with ",
                self.MaxLife,
                " Health,",
                self.Wounds,
                "Damage sustained and a",
                random.choice(self.Weapon1),
                ".",
            )
        if self.Tier == 2:
            print(
                "This is a sailor-grade seaman with ",
                self.MaxLife,
                " Health,",
                self.Wounds,
                "Damage sustained and a",
                random.choice(self.Weapon2),
                ".",
            )
        if self.Tier == 3:
            print(
                "This is a corsair-grade seaman with ",
                self.MaxLife,
                " Health,",
                self.Wounds,
                "Damage sustained and a",
                random.choice(self.Weapon3),
                ".",
            )
        if self.Tier == 4:
            print(
                "This is a quartermaster-grade seaman with ",
                self.MaxLife,
                " Health,",
                self.Wounds,
                "Damage sustained and a",
                random.choice(self.Weapon4),
                ".",
            )
        if self.Tier == 5:
            print(
                "This is a captain-grade seaman with ",
                self.MaxLife,
                " Health,",
                self.Wounds,
                "Damage sustained a",
                random.choice(self.Weapon5),
                ".",
            )


class Event:
    Textlist1: list[str]
    Textlist2: list[str]
    Text: str
    Combat: bool

    def __init__(self):
        self.Textlist1 = [
            "You find nothing.",
            "You find a small building of unknown make or model.",
            #                       "You find another seaman."
        ]
        self.Textlist2 = ["' 'Sup, the name's Jim.' it said."]
        self.Text = "Placeholder"
        self.Combat = False

    def randomizeEvent1(self):
        self.Text = random.choice(self.Textlist1)

    def randomizeEvent2(self):
        self.Text = random.choice(self.Textlist2)

    def EventOutput(self):
        print(self.Text)

    def IsCombat(self):
        if self.Text == "You find another seaman.":
            self.Combat = True
        else:
            self.Combat = False


E = Event()


class Choice:
    Choice: str
    Text: str

    def __init__(self):
        self.Choice = "Placeholder"
        self.Text = ""

    def ChoiceInput(self):
        self.Choice = input("[ACTION HERE] ")

    def ChoiceResult(self):
        ##        if E.Combat==True:
        ##            B=Boarder()
        ##            return(B)
        ##            if self.Choice=="Swing"or"Slash"or"Cut"or"Cleave"or"Bash":
        ##                if S.Weapon=="Construction hammer"or"Knife"or"Bat":
        ##                    B.Life-=1
        ##                    E.Text=="You manage to inflict a minor wound."
        ##                    E.EventOutput()
        ##                else:
        ##                   print("Such an option is not availible. (Can't run, check for typos)")
        ##                   print(E.Text)
        ##            if B.Life<=0:
        ##                E.Combat==False
        if not E.Combat:
            match S.Dead:
                case True:
                    self.Text = """You tumble onto your stomach, unable to remain upright any longer.
Eyes shut, you collapse into the sea from which you came."""
                    print(self.Text)
                    time.sleep(3)
                    quit()
                case False:
                    pass
            match E.Text:
                case "You find nothing.":
                    match self.Choice:
                        case "Walk":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Run":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Move":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Advance":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Progress":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "END OF THE LINE, LITTLE MAN!":
                            S.Wounds = 10
                        case _:
                            print("""Such is not an option.
Check for typos?
Actions must be ONE WORD LONG.""")
                case "You find a small building of unknown make or model.":
                    match self.Choice:
                        case "Walk":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Run":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Move":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Advance":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Progress":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Enter":
                            E.Text = """You go inside the building, finding a... grey seaman?
Its eyes glow yellow, it wears a carefree expression.
It has a tail... whatever that could be for is unknown."""
                            E.EventOutput()
                        case "END OF THE LINE, LITTLE MAN!":
                            S.Wounds = 10
                        case _:
                            print("""Such is not an option.
Check for typos?
Actions must be ONE WORD LONG.""")
                case """You go inside the building, finding a... grey seaman?
Its eyes glow yellow, it wears a carefree expression.
It has a tail... whatever that could be for is unknown.""":
                    match self.Choice:
                        case "Fight":
                            E.Text = """Your bones liquefy, you collapse onto the floor as Jim taunts you.
'Sorry bud, not a boss fight.'
You die, lungs collapsing as you melt into the blood from whence you came."""
                            E.EventOutput()
                            time.sleep(3)
                            quit()
                        case "Commune":
                            E.randomizeEvent2()
                            E.EventOutput()
                        case "Leave":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case "Exit":
                            E.randomizeEvent1()
                            E.EventOutput()
                        case _:
                            pass
                case _:
                    print("""Everything around you turns various shades of grey, a voice rings in your head.
'Hey, time god here, you've hit the end of this timeline. Nothin left 'ere.'
'I think you should restart the game, but I can't stop ya.'""")


C = Choice()


print("You open your eyes for the very first time, you are under a sea of blood.")
time.sleep(3)
print(
    "You swim up, the knowledge of drowning and how to swim almost being instinctual."
)
time.sleep(3)
print("You breach the surface, exhausted but alive.")
time.sleep(1.5)
print("You get up.")
time.sleep(1.5)
S = Sailor()
S.WhoAreYou()
time.sleep(3)

E.randomizeEvent1()
E.EventOutput()
while True:
    C.ChoiceInput()
    time.sleep(0.35)
    C.ChoiceResult()
