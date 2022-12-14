# Monty Hall Paradox Simulator (:car: vs :goat::goat:) 

**The Monty Hall problem is a mind blowing paradox that fooled many smart people, including the great mathematician, Paul Erdős. According to an anecdote, he was not convinced dispite of mathematical proofs given until a computer simulation was shown to him. As I'm fairly new to programming, I decided to give the simulation a try using Python.**

## The problem :confounded: 
There are 3 closed doors. One of them holds a valuable prize, the other two don't. The player picks one. Then the game host opens one of the other two doors that surely isn't a winner. Then the player can choose to keep her original pick or she can swap with the other closed door.
**But is it worth to swap? Mwahahahaha!**

## The intuition :stuck_out_tongue_winking_eye:
There's no point swapping as there are two doors remaining, therefore the chances must be 50% for each. Well, if it was this simple, it wouldn't be called a paradox.

## The reality :open_mouth:
The chosen door has 1/3 of a chance to be the winner while the other two have 2/3 of a chance COMBINED. Therefore, if we open one of the non chosen doors the other one will still have 2/3 of a chance, hence it's twice as likely to be the winner as the originally picked one. 

## The sad truth :poop:
Like all probabilistic problems work only on large sample sizes. Even if you swap, you still have only a ~66.6% chance of winning. Which is still quite slim. 

## Also note :goat:
The problem was named after American TV host Monty Hall whose show (Let's Make a Deal) had a *similar* setup. The winning door held a car, the two other a goat each. The reason why I don't follow the usual naming convention (i.e. car, goat) and use winner/loser dichotomy instead is not only because the show's selection part was a bit different from the (in)famous Monty Hall Paradox.

**I did so mostly because I would't give a f.ck about the car if I could have a cute goat instead.** 
