'''
The Monty Hall problem is a mind blowing paradox that fooled many smart people, including the great mathematician,
Paul Erdős. According to an anecdote, he was not convinced dispite of mathematical proofs given until a computer
simulation was showed to him. As I'm fairly new to programming, I decided to give the simulation a try using Python.

The problem:
There are 3 closed doors. One of them holds a valuable prize, the other two don't. The player picks one.
Then the we open one of the other two doors that surely isn't a winner. Then the player can choose to keep her original
pick or she can swap with the other closed door.
Is it worth to swap?

The intuition:
There's no point swapping as there are two doors, so the chances are 50/50% for each.

The reality:
The choosen door has 1/3 of a chance to be the winner while the other two have 2/3 of a chance COMBINED.
Therefore, if we open one of the non chosen doors the other one will still have 2/3 of a chance,
hence it's twice as likely to be the winner as the originally picked one. 

The sad truth:
Like all probabilistic problems work only on large sample sizes. Even if you swap, you still have only a
~66.6% chance of winning. Which is still quite slim. 

Also note:
The problem was named after American TV host Monty Python whose show (Let's Make a Deal) had a *similar* setup.
The winning door held a car, the two others a goat each. The reason why I don't follow the usual naming convention
(i.e. car, goat) and use winner/not winner dichotomy instead is not only because the show's selection part was a bit
different from the (in)famous Monty Hall Paradox.
I did so mostly because I would't give a f.ck about the car if I could have a cute goat instead. 
'''

# Import necessary libraries
import random

# Creating three doors, arbitrarily choosing the winner (door A). It doesn't have to be randomized so it can be hard coded.
door_dict = {
    "door_A": True, # The winner
    "door_B": False, # Not the winner
    "door_C": False, # Not the winner
}
door_list = list(door_dict.keys())

# Setting the number of simulation cycles
cycles = int(input("How many times should I run the simulation? "))

# Let the player choose a door (chosen_door). The remaining doors will be in the other_doors list.
chosen_door = random.choice(list(door_list))
other_doors = []
for door in door_list:
    if door != chosen_door:
        other_doors.append(door)

# Open one of the remaining doors. It shouldn't be the winner! (Technically: remove (one of) the non-winning one(s) from the other_doors list.
# If both of the remaining doors are non-winners, it doesn't matter which one is chosen.
# If I develop this further for n number of doors, I would either keep the winner among the other_doors, or if none of them are winners, it would just pick one randomly.
for i in other_doors:
    if door_dict[i] == False:
        other_doors.remove(i)

# Now the player can decide if she switches between the two doors. She's a cold headed rational creature. So she flips a coin every time to make up her mind. :)
switch = bool(random.getrandbits(1))

print("The original choice was: " + chosen_door + ".") # Let's check if it works so far.
if switch == True:
    print("I change my mind and pick the other door.")
else:
    print("I stick to my original choice.")
if switch == True:
    chosen_door = other_doors[0]

print("So my final answer is: " + chosen_door + ".")