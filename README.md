#Genetic Poker

Written for a class about artificial life, where we were learning to create genetic algorithms. This program runs a genetic algorithm to evolve a population of poker hands.

##Files

**Run.txt** is a sample run of the code

**Hand.py** is the hand class, which contains the following methods:
  - __generateHand, which generates a legal random hand
  - __generateCard, which generates a card and is used by __generateHand and mutate
  - checkLegality, which returns true or false if the hand is legal
  - mutate, which legally mutates a random card in the hand
  - calculateFitness, which calculates the fitness of a hand based on the list of possible poker hands given in the assignment

Within hand.py:
  - A hand is represented by a list of cards in the hand object.
  - A card is represented by a tuple where the first part contains the "number" and the second part contains the suit.
  - Mutation consists of choosing a random card, changing its suit or number by a small amount, and checking legality.
  - Legality is confirmed/denied by checking for duplicates in the hand.
  - Fitness is calculated by checking whether a hand is a legal poker hand and giving it a corresponding fitness. More on this in detail later.

**Algorithm.py** is the client code which runs the genetic algorithm. The functions are:
  - main, which is the main genetic algorithm
  - calculatePopulationFitness, which calculates the fitness for every member of the population and returns a list of probabilities that is used to choose the parents
  - mutate, which chooses a random card in a random hand to mutate
  - elitism, which clones a parent
  - crossover, which randomly combines two parents to create a child

Algorithm.py has several variables up front that make manipulating the algorithm a bit easier. These are:
  - populationSize, which I chose to be 200, but I found that as long as it isn't very small (below 75), the results are about the same
  - generations, which I chose to be 300, but I found that increasing that number past 200 doesn't seem to affect the outcome much (the highest I tried was 2,000)
  - numParents, which I chose to be half the population size. I found that results are more interesting the more parents there are.

##Observations

I generally found that my algorithm doesn't produce interesting results. It seems to me that the true value of genetic algorithms isn't necessarily the end result, but the process of coding it and understanding the way your program evolves. Unfortunately, my program evolves pretty consistently mediocre hands. Most of the time, unless I'm lucky (luck doesn't count as evolution), the population will eventually converge at a fitness of about 50 or 60, occasionally 70. It will also converge to this pretty quickly ... in around 20 generations or so, and increasing the amount of generations doesn't seem to do much.

This is the problem we discussed in class - if the highest fitness is 60 and new information is never introduced, we don't ever get the chance to evolve higher than the fittest member of the population. Crossover and mutation are meant to solve this, but in my opinion, the 80% allotted for crossover and 10% for mutation each do not seem to be enough to prevent sliding into this consistent mediocrity. When I changed the percentages to 50% crossover, 40% mutation, 10% elitism, I got much more interesting results. Here's a few reasons that contribute to this problem:

1. A low population size mean that the cards will converge extremely quickly, but whether they successfully converge to something good (let's say above 50) is a bigger gamble (ha).
2. A low amount of parents mean that almost exclusively good hands will be selected as parents, which is bad. We want junk thrown in to change it up and offer new possibilities.
3. A fitness score distribution could be more expertly/mathematically calculated. I've followed the basic principle of "linear drop off, except at the 3/4 mark, where the drop off is linear but less steep". I think a better function would be a decreasing exponential curve, to prevent the most fit parents from being consistently selected.
4. No elitism. I know 10% elitism was part of the assignment, so I didn't change it, but I don't like it. It seems like keeping the fittest members to avoid regression just means that the population gets flooded with near-identical, same fitness, mediocre hands.

Ultimately I think this is a problem unique to card hands. Good hands are alike in some way, and if we start with a base population, the bad hands (the different hands) get killed off, and the good hands prevail. In the end, there's not enough variation with the small amount of mutation allowed (10%), and we need some variation, some junk, thrown in.

I think the best way to fix this is to add an intermediate fitness value which will score a hand that is one step (one feasible mutation) away from being a high-ranking hand. But predicting hand goodness like that seemed outside the scope of this project, so I dropped the idea.

**A note about how the fitness function works:**
The calculateFitness method inside hand.py is basically the "fitness function". Since poker hands are scored by the highest possible type they qualify for, I just check the hand for patterns that match poker hands starting from the best one (royal flush) to the worst one (pair). If none of the conditions are met, the hand is given a base score. The calculateFitness method itself is pretty long because it contains 9 different checks for 9 different hand types, which is pretty trivially done if you first sort the hand and check for matches. As a global variable, hand.py has fitnessScoreDistribution, which is just an easier way for me to change what each hand is scored to without having to go into the code. I found that I got different results based on what the score distribution is, and I believe that the best distribution is linear up until around "straight", where it shouldn't decrease as much. The distribution I chose for completing this project is 100, 90, 80, 70, 60, 50, 45, 40, 35, 30. You can see that at 50, the scores don't drop off as quickly.


##Some other stuff:

I import the following things to make the code work. 

**from __future__ import division**

  - needed because python 2 by default does integer division and not floating point division

**from numpy.random import choice**
  - used to make a weighted random choice for parents

**import random**
  - random number generator

**import copy**
  - creates copy of an object, used for elitism and mutations
