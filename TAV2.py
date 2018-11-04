#Variables and lists
shovel = 0 #it's a shovel
bk = 0 #bronze key
gk = 0 #gold key
li = 0 #list item, checking if the player has anything at all
loc = 0 #location of the player. IMPORTENT: 0=south 1=center 2=north 3=west 4=east
southd = 0 #check to see if the player can move north
invl = [] #list that contains inventory items
bb = 0 #branch broken, checks what state the tree in the east is in
ng = 0
wg = 0
sg = 0
#Functions that aren't area specific
def cl():
    global loc
    nl = raw_input("Input area. 0=south 1=center 2=north 3=west 4=east")
    loc = int(nl)
    command()

def inv():
    global li
    print "You have:"
    if li == 0:
        print "Nothing"
        command()
    else:
        import sys
        sys.stdout.writelines(invl)
        command()

#Allows the player to get extra info on the items they obtain, and only those
def exmn():
    global shovel
    global gk
    global bk
    global li
    if li == 0:
        print "You have nothing to examine."
        command()
    ie = raw_input("What do you want to examine?\n>")
    if ie in ("Shovel", "shovel") and shovel == 1:
        print "An old, rusted shovel, but still strong enough to be of use."
    elif ie == "Gold Key" and gk == 1:
        print ""
    elif ie == "Bronze Key" and bk == 1:
        print ""
        global loc
    command()

def move():
    global loc
    global southd
    print "What direction do you go?"
    drc = raw_input(">")
    if drc in ("North", "north") and loc == 0 and southd == 1:
        print "You crawl through the hole and get to the other side of the fence. You move to the fountain, and are now in the center, with the house to your north."
        loc = 1
        command()
    elif drc in ("North", "north") and loc == 0 and southd == 0:
        print "The fence blocks your way."
        command()
    elif drc != ("North", "north") and loc == 0:
        print "You cannot move there."
        command()
    elif drc in ("South", "south") and loc == 2:
        print "You walk back down to the fountain."
        loc = 1
        command()
    elif drc != ("South", "south") and loc == 2:
        print "You cannot move there."
        command()
    elif drc in ("East", "east") and loc == 3:
        print "You walk back over the grassy area to the fountain"
        loc = 1
        command()
    elif drc != ("East", "east") and loc == 3:
        print "You cannot move there."
        command()
    elif drc in ("West", "west") and loc == 4:
        print "You walk on the path back to the fountain."
        loc = 1
        command()
    elif drc != ("West", "west") and loc == 4:
        print "You cannot move there."
        command()
    elif drc in ("North", "north"):
        print "You jog up the path to find a large house to the north."
        loc = 2
        command()
    elif drc in ("West", "west"):
        print "You walk over to the west. You find yourself in the middle of a old cemetary."
        loc = 3
        command()
    elif drc in ("East", "east"):
        print "You walk over to the east side of the house by a large tree."
        loc = 4
        command()
    elif drc in ("South", "south"):
        print "You crawl back under the fence to the south, by your car."
        loc = 0
        command()
    else:
        print "Input not recognized. Please try again."
        direction()

def help():
    print "Available commmands are Move, Inventory, Look, Area and Examine."
    command()

def look():
    if loc == 0:
        S_L()
    elif loc == 1:
        C_L()
    elif loc == 2:
        N_L()
    elif loc == 3:
        W_L()
    elif loc == 4:
        E_L()

def command():
    c = raw_input(">")
    if c == "Move":
        move()
    elif c == "move":
        move()
    elif c == "Inventory":
        inv()
    elif c == "inventory":
        inv()
    elif c == "Inv":
        inv()
    elif c == "inv":
        inv()
    elif c == "Look":
        look()
    elif c == "look":
        look()
    elif c == "Help":
        help()
    elif c == "help":
        help()
    elif c == "Examine":
        exmn()
    elif c == "examine":
        exmn()
    elif c == "Area":
        area()
    elif c == "area":
        area()
    elif c == "cl":
        cl()
    else:
        print "Input not recognized."
        command()

def area():
    global loc
    if loc == 0:
        print "You are south of the fountain, at the old fence."
        command()
    elif loc == 1:
        print "You are in the center, at the fountain."
        command()
    elif loc == 2:
        print "You are north of the fountain, at the old house."
        command()
    elif loc == 3:
        print "You are in the cemetary, west of the fountain."
        command()
    elif loc == 4:
        print "You are at the old treehouse, east of the fountain."
        command()
    else:
        print "I honestly don't know where the hell you are, how did you break my game?"
        command()
#Functions for individual areas
def S_L():
    global shovel
    global southd
    global li
    global invl
    print "What direction do you want to look?(North, South, East, West)"
    sldrc = raw_input(">")
    if sldrc in ("North", "north", "N", "n"):
        print "There is old fence, worn out, and overgrown. There doesn't appear to be a door, and it is too tall to climb."
        command()
    if sldrc in ("West", "west", "W", "w"):
        print "There is a mound of dirt with a shovel sticking out of it."
        if shovel == 0:
            print "Do you want to pick it up?"
            shovelpu = raw_input(">")
            if shovelpu in ("Yes", "yes", "Y", "y"):
                print "You try to pick up the shovel. It is rusted over, and has spiderwebs on the bottem, but you pry it out of the dirt."
                shovel = 1
                li = 1
                invl.append("A old shovel")
                command()
            else:
                print "You leave the shovel alone."
                command()
        else:
            print "You see the mound of dirt that once had the shovel."
            command()
    elif sldrc in ("East", "east", "E", "e"):
        print "You see the fence stretching out a long ways, with shrubs intermediantly spaced on the side.\nClose to the side of the fence, a patch of dirt looks freshly turned over."
        if shovel == 1 and southd == 0:
            print "Do you want to shovel away the dirt?"
            dirtm = raw_input(">")
            if dirtm in ("Yes", "yes", "Y", "y"):
                print "You get down and start shoveling the dirt. \nIt is slow going at first, but as you keep going you realize it is only covering on this side, apparantly to cover up a small hole in the fence."
                southd = 1
                command()
            else:
                print "You leave the dirt alone."
                command()
        command()
    elif sldrc in ("South", "south", "S", "s"):
        print "You see the windy backroad you took to get here, and your car, which is still steaming from being overheated."
        command()
    else:
        print "Not a valid direction."
        command()
#def C_L():

def W_L():
    global invl
    global bk
    global ng
    global wg
    global sg
    print "What direction do you want to look?(North, South, East, West)"
    wldrc = raw_input(">")
    if wldrc in ("North", "north") and ng == 0:
        print "You see a old grave; the tombstone reads \"Here lies Stella Frank\""
        print "Do you want to use the shovel to dig up the grave?"
        gdu = raw_input(">")
        if gdu in ("Yes", "yes", "Y", "y"):
            print "You dig in the grave and find nothing."
            ng = 1
            command()
        else:
            print "You leave the grave alone."
            command()
    elif wldrc in ("West", "west") and wg == 0:
        print "You see a old grave; the tombstone reads \"Here lies George Johnston\""
        print "Do you want to use the shovel to dig up the grave?"
        gdu = raw_input(">")
        if gdu in ("Yes", "yes", "Y", "y"):
            print "You dig in the grave and find nothing."
            wg = 1
            command()
        else:
            print "You leave the grave alone."
            command()
    elif wldrc in ("South", "south") and sg == 0:
        print "You see a old grave; the tombstone reads \"Here lies Helena Johnston\""
        print "Do you want to use the shovel to dig up the grave?"
        gdu = raw_input(">")
        if gdu in ("Yes", "yes", "Y", "y"):
            print "You dig up the grave and find a bronze key hidden in the dirt."
            bk = 1
            sg = 1
            invl.append("; a bronze key")
            command()
        else:
            print "You leave the grave alone."
            command()
    elif wldrc in ("East", "east"):
        print "You see the old fountain off in the distance."
        command()
    else:
        print "You see the old grave that you dug up."
        command()
def E_L():
    global invl
    global bk
    global gk
    global bb
    print "What direction do you want to look?(North, South, East, West)"
    eldrc = raw_input(">")
    if eldrc in ("North", "north"):
        print "To the north there is a swampy mess next to the house."
        command()
    elif eldrc in ("South", "south"):
        if bb != 2:
            print "To the south you see a field full of sharp rocks. There seems to be a small path through the center."
            rp = raw_input("Do you want to follow the path?\n>")
            if rp in ("Yes", "yes", "Y", "y"):
                print "You follow the path down and around back up to the backside of the tree to the east. You find a hidden ladder and climb up into the treehouse."
                print "It creaks a little. You find a small gold key laying on the floor. As you pick it up, the treehouse begins to tilt backword."
                print "You lurch forward and jump out the window as the treehouse collapses behind you."
                bb = 2
                command()
            else:
                print "You back away from the path."
        else:
            print "You see a field full of sharp rocks."
    elif eldrc in ("West", "west"):
        print "You see the fountain that you came from."
        command()
    elif eldrc in ("East", "east"):
        if bb == 0:
            print "You see a large tree, winding upwards with a sizeable treehouse. There seems to be enough branches to climb up and get into the treehouse."
            cub = raw_input("Do you want to climb up the branches?\n>")
            if cub in ("Yes", "yes", "Y", "y"):
                print "You start to climb up the tree. It works at first, but a few feet up you grab a branch. As you pull yourself up it breaks under your weight."
                print "You fall to the ground with the branch. That route clearly won't work."
                bb = 1
                command()
            else:
                print "You step away from the tree."
                command()
        elif bb == 1:
            print "You see a large tree, winding upwards with a sizeable treehouse. The broken branch is there from your fall."
        elif bb == 2:
            print "You see the tree, and beyond that the remains of the treehouse rubble."
        else:
            print "The tree disapears as a black hole swallows it up and sucks you in. You are then subatomically ripped apart. The end."
            command()
command()
