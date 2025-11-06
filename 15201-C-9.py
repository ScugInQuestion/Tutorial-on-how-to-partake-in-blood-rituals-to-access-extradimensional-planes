import time
import random


class Sailor:
    weapon: str
    wounds: int
    strength: int
    status: str
    tendancies: list[str]
    last_stand: bool
    dead: bool

    def __init__(self):
        self.weapon = random.choice(
            [
                "Construction hammer",
                "Knife",
                "Bat",
                "Mace",
                "Shortsword",
                "Combat Knife",
                # "Rapier","Spear","Warhammer","Zweihander"
            ]
        )
        self.wounds = 0
        self.strength = 0
        self.status = "Fine"
        self.tendancies = ["Stoat", "Magpie", "Hare"]
        self.last_stand = False
        self.dead = False

    def attack(self):
        if self.weapon == "Bare Hands":
            self.strength = 1

    def death(self):
        if self.wounds >= 10:
            self.dead = True

    def who_are_you(self):
        print(
            "You are a Sailor-class seaman with",
            self.wounds,
            "damage sustained, are currently",
            self.status,
            ". You have the tendancies of the",
            random.choice(self.tendancies),
            "and are armed with a",
            random.choice(self.weapon),
            ".",
        )


S = Sailor()


class Boarder:
    tier: int
    weapon1: str
    weapon2: str
    weapon3: str
    weapon4: str
    weapon5: str
    wounds: int
    max_life: int
    life: int
    stamina: int
    status: str
    dead: bool

    def __init__(self):
        self.tier = random.randint(1, 5)
        self.weapon1 = random.choice(
            [
                "Bare Hands",
                "Bare Hands",
                "Bare Hands",
                "Construction hammer",
                "Knife",
                "Bat",
            ]
        )
        self.weapon2 = random.choice(["Construction hammer", "Knife", "Bat"])
        self.weapon3 = random.choice(["Spear", "Shortsword", "Combat Knife"])
        self.weapon4 = random.choice(["Rapier", "Mace", "Warhammer", "Zweihander"])
        self.weapon5 = random.choice(["Whipsword", "Grand Gavel", "Jousting Lance"])
        self.wounds = 0
        self.max_life = random.randint(1, 5) * self.tier + self.tier
        self.life = self.max_life
        self.stamina = 5
        self.status = "Fine"
        self.dead = False

    def death(self):
        if self.wounds >= self.max_life:
            self.dead = True

    def who_am_i(self):
        if self.tier == 1:
            print(
                "This is an oarsman-grade seaman with ",
                self.max_life,
                " Health,",
                self.wounds,
                "Damage sustained and a",
                random.choice(self.weapon1),
                ".",
            )
        if self.tier == 2:
            print(
                "This is a sailor-grade seaman with ",
                self.max_life,
                " Health,",
                self.wounds,
                "Damage sustained and a",
                random.choice(self.weapon2),
                ".",
            )
        if self.tier == 3:
            print(
                "This is a corsair-grade seaman with ",
                self.max_life,
                " Health,",
                self.wounds,
                "Damage sustained and a",
                random.choice(self.weapon3),
                ".",
            )
        if self.tier == 4:
            print(
                "This is a quartermaster-grade seaman with ",
                self.max_life,
                " Health,",
                self.wounds,
                "Damage sustained and a",
                random.choice(self.weapon4),
                ".",
            )
        if self.tier == 5:
            print(
                "This is a captain-grade seaman with ",
                self.max_life,
                " Health,",
                self.wounds,
                "Damage sustained a",
                random.choice(self.weapon5),
                ".",
            )


class Event:
    textlist1: list[str]
    textlist2: list[str]
    text: str
    combat: bool

    def __init__(self):
        self.textlist1 = [
            "You find nothing.",
            "You find a small building of unknown make or model.",
            #                       "You find another seaman."
        ]
        self.textlist2 = ["' 'Sup, the name's Jim.' it said."]
        self.text = "Placeholder"
        self.combat = False

    def randomize_event1(self):
        self.text = random.choice(self.textlist1)

    def is_dead(self):
        if S.dead:
            self.text = """You collapse onto the ground, vision fading and your mangled limbs weak.
Your mind grows still as life leaves your body.
You have died, your body having melted back into the sea."""

    def randomize_event2(self):
        self.text = random.choice(self.textlist2)

    def event_output(self):
        print(self.text)

    def is_combat(self):
        if self.text == "You find another seaman.":
            self.combat = True
        else:
            self.combat = False


E = Event()


class Choice:
    choice: str

    def __init__(self):
        self.choice = "Placeholder"

    def choice_input(self):
        self.choice = input("[ACTION HERE] ")

    def choice_result(self):
        match E.text:
            case """You collapse onto the ground, vision fading and your mangled limbs weak.
Your mind grows still as life leaves your body.
You have died, your body having melted back into the sea.""":
                match self.choice:
                    case _:
                        E.event_output()
                        time.sleep(3)
                        quit()
        if E.combat:
            match E.text:
                case "You find another seaman.":
                    B = Boarder()
                    match self.choice:
                        case "Swipe":
                            if S.weapon == "Construction hammer" or "Knife" or "Bat":
                                B.life -= 1
                                E.text = "You manage to inflict a minor wound."
                            elif S.weapon == "Shortsword" or "Combat Knife" or "Mace":
                                B.life -= 3
                                E.text = (
                                    "Your weapon manages to deal considerable damage."
                                )
                            E.event_output()
                        case "Slice":
                            if S.weapon == "Construction hammer" or "Knife" or "Bat":
                                B.life -= 1
                                E.text = "You manage to inflict a minor wound."
                            if S.weapon == "Shortsword" or "Combat Knife" or "Mace":
                                B.life -= 3
                                E.text = (
                                    "Your weapon manages to deal considerable damage."
                                )
                            E.event_output()
                        case "Bash":
                            if S.weapon == "Construction hammer" or "Knife" or "Bat":
                                B.life -= 1
                                E.text = "You manage to inflict a minor wound."
                            if S.weapon == "Shortsword" or "Combat Knife" or "Mace":
                                B.life -= 3
                                E.text = (
                                    "Your weapon manages to deal considerable damage."
                                )
                            E.event_output()
                        case "Swing":
                            if S.weapon == "Construction hammer" or "Knife" or "Bat":
                                B.life -= 1
                                E.text = "You manage to inflict a minor wound."
                            if S.weapon == "Shortsword" or "Combat Knife" or "Mace":
                                B.life -= 3
                                E.text = (
                                    "Your weapon manages to deal considerable damage."
                                )
                            E.event_output()
                        case "Slash":
                            if S.weapon == "Construction hammer" or "Knife" or "Bat":
                                B.life -= 1
                                E.text = "You manage to inflict a minor wound."
                            if S.weapon == "Shortsword" or "Combat Knife" or "Mace":
                                B.life -= 3
                                E.text = (
                                    "Your weapon manages to deal considerable damage."
                                )
                            E.event_output()
            if B.life <= 0:
                del B
                E.text = """The enemy collapses, too battered to remain upright.
It melts back into the blood from whence it came."""
        match E.text:
            case "You find nothing.":
                match self.choice:
                    case "Walk":
                        E.randomize_event1()
                        E.event_output()
                    case "Run":
                        E.randomize_event1()
                        E.event_output()
                    case "Move":
                        E.randomize_event1()
                        E.event_output()
                    case "Advance":
                        E.randomize_event1()
                        E.event_output()
                    case "Progress":
                        E.randomize_event1()
                        E.event_output()
                    case "END OF THE LINE":
                        print("Your words sink into the sea...")
                        S.dead = True
                    case "I CAST NEKOMANCY, RICE!":
                        E.text = "You find another seaman."
                        print(
                            "A fresh seaman bursts out from the ocean in front of you, getting up and immediatley starting a fight."
                        )
                    case _:
                        print("""Such is not an option.
Check for typos?
Actions must be ONE WORD LONG.""")

            case "You find a small building of unknown make or model.":
                match self.choice:
                    case "Walk":
                        E.randomize_event1()
                        E.event_output()
                    case "Run":
                        E.randomize_event1()
                        E.event_output()
                    case "Move":
                        E.randomize_event1()
                        E.event_output()
                    case "Advance":
                        E.randomize_event1()
                        E.event_output()
                    case "Progress":
                        E.randomize_event1()
                        E.event_output()
                    case "Enter":
                        E.text = """You go inside the building, finding a... grey seaman?
Its eyes glow yellow, it wears a carefree expression.
It has a tail... whatever that could be for is unknown."""
                        E.event_output()
                    case "END OF THE LINE":
                        print("Your words sink into the sea...")
                        S.dead = True
                    case _:
                        print("""Such is not an option.
Check for typos?
Actions must be ONE WORD LONG.""")

            case """You go inside the building, finding a... grey seaman?
Its eyes glow yellow, it wears a carefree expression.
It has a tail... whatever that could be for is unknown.""":
                match self.choice:
                    case "Fight":
                        E.text = """Your bones liquefy, you collapse onto the floor as Jim taunts you.
'Sorry bud, not a boss fight.'
You die, lungs collapsing as you melt into the blood from whence you came."""
                        E.event_output()
                        time.sleep(3)
                        quit()
                    case "Commune":
                        E.randomize_event2()
                        E.event_output()
                    case "Leave":
                        E.randomize_event1()
                        E.event_output()
                    case "Exit":
                        E.randomize_event1()
                        E.event_output()

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

S.who_are_you()
time.sleep(3)

E.randomize_event1()
E.event_output()
while True:
    E.is_dead()
    E.is_combat()
    C.choice_input()
    time.sleep(0.35)
    C.choice_result()
