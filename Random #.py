# Random Number Generator
import random

heads = 0
tails = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
snake = 0
one2 = 0
one3 = 0
one4 = 0
one5 = 0
one6 = 0
two2 = 0
two3 = 0
two4 = 0
two5 = 0
two6 = 0
three3 = 0
three4 = 0
three5 = 0
three6 = 0
four4 = 0
four5 = 0
four6 = 0
five5 = 0
five6 = 0
six6 = 0

while True:
    print("Type count coins, die or dice for results")
    print("Type reset coins, die or dice to reset your results")
    ty = input("Coins, Die or Dice?: ")
    ty = ty.lower()

    if ty == "dice":
        x = random.randint(1,6)
        print(f"\n{x}")
        x2 = random.randint(1,6)
        print(f"{x2}\n")
        
        #one
        if x == 1 and x2 == 1:
            snake = snake + 1
        if x == 1 and x2 == 2 or x2 == 1 and x == 2:
            one2 = one2 + 1
        if x == 1 and x2 == 3 or x2 == 1 and x == 3:
            one3 = one3 + 1
        if x == 1 and x2 == 4 or x2 == 1 and x == 4:
            one4 = one4 + 1
        if x == 1 and x2 == 5 or x2 == 1 and x == 5:
            one5 = one5 + 1
        if x == 1 and x2 == 6 or x2 == 1 and x == 6:
            one6 = one6 + 1

        #two
        if x == 2 and x2 == 2:
            two2 = two2 + 1
        if x == 2 and x2 == 3 or x2 == 2 and x == 3:
            two3 = two3 + 1
        if x == 2 and x2 == 4 or x2 == 2 and x == 4:
            two4 = two4 + 1
        if x == 2 and x2 == 5 or x2 == 2 and x == 5:
            two5 = two5 + 1
        if x == 2 and x2 == 6 or x2 == 2 and x == 6:
            two6 = two6 + 1

        #three
        if x == 3 and x2 == 3:
            three3 = three3 + 1
        if x == 3 and x2 == 4 or x2 == 3 and x == 4:
            three4 = three4 + 1
        if x == 3 and x2 == 5 or x2 == 3 and x == 5:
            three5 = three5 + 1
        if x == 3 and x2 == 6 or x2 == 3 and x == 6:
            three6 = three6 + 1

        #four
        if x == 4 and x2 == 4:
            four4 = four4 + 1
        if x == 4 and x2 == 5 or x2 == 4 and x == 5:
            four5 = four5 + 1
        if x == 4 and x2 == 6 or x2 == 4 and x == 6:
            four6 = four6 + 1

        #five
        if x == 5 and x2 == 5:
            five5 = five5 + 1
        if x == 5 and x2 == 6 or x2 == 5 and x == 6:
            five6 = five6 + 1

        #six
        if x == 6 and x2 == 6:
            six6 = six6 + 1

    elif ty == "die":
        x = random.randint(1,6)
        print(f"\n{x}\n")
        if x == 1:
            one = one + 1
        elif x == 2:
            two = two + 1
        elif x == 3:
            three = three + 1
        elif x == 4:
            four = four + 1
        elif x == 5:
            five = five + 1
        else:
            six = six + 1

    elif ty == "coin" or ty == "coins":
        x = random.randint(1,2)
        if x == 1:
            print("\nHeads\n")
            heads = heads + 1
        else:
            print("\nTails\n")
            tails = tails + 1

    elif ty == "count coins" or ty == "count coin":
        print(f"\nNumber of tails: {tails} \nNumber of heads: {heads}\n")

    elif ty == "count die":
        print(f"\nNumber of ones: {one} \nNumber of twos: {two} \nNumber of threes: {three} \nNumber of fours: {four} \nNumber of fives: {five} \nNumber of sixes: {six}\n")

    elif ty == "count dice":
        print(f"\nOnes\n   Snake Eyes: {snake} \n   Ones and twos: {one2} \n   Ones and threes: {one3} \n   Ones and fours: {one4} \n   Ones and fives: {one5} \n   Ones and sixes: {one6}")
        print(f"\nTwos\n   Twos and ones: {one2} \n   Twos and twos: {two2} \n   Twos and threes: {two3} \n   Twos and fours: {two4} \n   Twos and fives: {two5} \n   Twos and sixes: {two6}")
        print(f"\nThrees\n   Threes and ones: {one3} \n   Threes and twos: {two3} \n   Threes and threes: {three3} \n   Threes and fours: {three4} \n   Threes and fives: {three5} \n   Threes and sixes: {three6} \n")
        print(f"\nFours\n   Fours and ones: {one4} \n   Fours and twos: {two4} \n   Fours and threes: {three4} \n   Fours and fours: {four4} \n   Fours and fives: {four5} \n   Fours and sixes: {four6} \n")
        print(f"\nFives\n   Fives and ones: {one5} \n   Fives and twos: {two5} \n   Fives and threes: {three5} \n   Fives and fours: {four5} \n   Fives and fives: {five5} \n   Fives and sixes: {five6} \n")
        print(f"\nSixes\n   Sixes and ones: {one6} \n   Sixes and twos: {two6} \n   Sixes and threes: {three6} \n   Sixes and fours: {four6} \n   Sixes and fives: {five6} \n   Sixes and sixes: {six6} \n")

    elif ty == "reset coin" or ty == "reset coins":
        heads = 0
        tails = 0
        print("\nCoin results have been reset\n")

    elif ty == "reset die":
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0
        print("\nDie results have been reset\n")

    elif ty == "reset dice":
        snake = 0
        one2 = 0
        one3 = 0
        one4 = 0
        one5 = 0
        one6 = 0
        two2 = 0
        two3 = 0
        two4 = 0
        two5 = 0
        two6 = 0
        three3 = 0
        three4 = 0
        three5 = 0
        three6 = 0
        four4 = 0
        four5 = 0
        four6 = 0
        five5 = 0
        five6 = 0
        six6 = 0
        print("\nDice results have been reset\n")
        
    else:
        print("\nNot a valid input\n")
