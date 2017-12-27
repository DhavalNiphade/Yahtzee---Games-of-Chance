#!/usr/bin/env python3

# YAHTZEE IMPLEMENTATION OF GAME OF CHANCE

# AUTHOR = Dhaval R Niphade
# DATE CREATED = October 15, 2017
# LAST MODIFIED = October 15, 2017
# TIME = 0220 HRS
# COURSE NUMBER & NAME = CSCI B551 Elements of Artificial Intelligence

# IMPORT SECTION
import sys

def expected(combination,die):
    retval = 0.0
    # rollList=[(first,second,third) for first in range(1,7) if combination[0] for second in range(1,7) if combination[1] for third in range(1,7) if combination[2]]
    # rollList=[(first,second,third)
    #           for first in ((die[0],) if not combination[0] else range(1,7)
    #             for second in ((die[1],)) if not combination[1] else range(1,7)
    #                 for third in ((die[2],)) if not combination[2] else range(1,7)]
    for first in ((die[0],) if not combination[0] else range(1,7)):
        for second in ((die[1],) if not combination[1] else range(1, 7)):
            for third in ((die[2],) if not combination[2] else range(1, 7)):
                retval += sum(map(int,[first,second,third])) if len(set([first,second,third]))!=1 else 25.0

    # for rolls in rollList:
    #     retval+=sum(list(map(int,rolls))) if (rolls.count(rolls[0])==len(rolls)) else 25.0

    # for roll in rollList:
    #     retval += sum(roll) if roll.count(roll[0])==len(roll) else 25
    # return (combination, retval * 1 / len(rollList))

    return (combination,retval*1/6**sum(combination))

def makePrediction(die):
    gMax = ([],0)
    chancePossible = [(d1,d2,d3) for d1 in [True,False] for d2 in [True,False] for d3 in [True,False]]
    for combination in chancePossible:
        gMax = max(gMax,expected(combination,die),key=lambda x:x[1])
    return(gMax)

def main():
    die = list(map(int,[sys.argv[1],sys.argv[2],sys.argv[3]]))

    if (len(set(die))==1):
        print("Don't re-roll you are already at your maximum score")
        return 0

    (rollSet,expect) = makePrediction(die)
    print("Your current score is",sum(die))
    print("Roll the",rollSet,"for an anticipated score of", int(expect), "and a gain of",int(expect - sum(die)))

    return 0

if __name__ == "__main__":
    main()

