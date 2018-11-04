wu = 0
eu = 0
def direction():
    print "What direction do you go?"
    drc = raw_input(">")
    if drc == "North":
        north()
    elif drc == "West":
        west()
    elif drc == "East":
        east()
    else:
        print "Input not recognized. Make sure you start with a capital letter for the directions."
        direction()
def north():
    global wu
    global eu
    if wu == 1 and eu == 1:
        print "You place both keys in the door and the creaky old door swings open."
        import sys
        sys.exit()
    else:
        print "You aproach the house. The front door is locked, with 2 keyholes, apparantly needing both to pass."
        print "A sign on the door says,\n\"To pass, you need to find the key buried with my late wife, and the other in my childhood escape.\"\n -----SJ"
        direction()

def west():
    global wu
    if wu == 1:
        print "You already have this area's key."
        direction()
    print "You walk towards the cemetary. It is quiet, and you hear the wind whistling through the trees."
    print "In front of you are 4 tombstones."
    print "The names on the four tombstones are (1.)Stella Frank, (2.)George Johnston, (3.)Helena Johnston, and (4.) Rose Smith."
    print "Which grave do you dig up?"
    wc = raw_input("(Number of the grave)\n>")
    if wc == "3":
        print "You dig up the grave and find a key."
        wu += 1
        direction()
    else:
        print "You dig up the grave and find nothing."
        west()

def east():
    global eu
    if eu == 1:
        print "You already have this area's key."
        direction()
    print "You walk into the garden, which is overgrown with weeds and bushes. In the back there is a tree house."
    print "The ladder is old and the ropes are fraying. The tree is steep with sparce brances."
    print "How do you proceed?"
    ec = raw_input("(Climb tree or use Ladder)\n>")
    if ec == "Climb":
        print "You go around to the back of the tree and attempt to climb.\nIt is hard at first, but you find a sturdy branch that you hadn't seen before."
        print "You enter the treehouse and find a key on the floor. You get out and climb back down."
        eu += 1
        direction()
    elif ec == "Ladder":
        print "You try to climb the old ladder. Half way up it jerks and lets out a little slack. You hang there, trying to think of a way out."
        print "Suddenly, it snaps and you fall to the ground. You land on a sharp stump that slices through your back."
        import sys
        sys.exit()
    else:
        print "Input not recognized. Make sure you use a capital letter for the options. Ladder, or Climb."
        east()
print "You see a fence made out of rusted bars, with small spikes at the top. What do you do?"
sc = raw_input("1. Climb over. \n2. Crawl under.")
if sc == "1":
	print "You try to climb over, and are impaled by the spikes."
	import sys
	sys.exit()
elif sc == "2":
    print "You find a small patch of freshly moved dirt. You push it to the side and manage to crawl through."
    print "You see a house to the North, a garden to the East, and a cemetary to the West."
    direction()
else:
    print "Input not recognized."
    import sys
    sys.exit()