import random

def main():
    emperical_probability() # probability test with random


def emperical_probability():
    #define red cards and total deck
    red_cards = set(range(1,27)) # marking all red cards from 1-26
    deck = list(range(1,53)) # for random choice to work( choice work on list) , taking all 52 cards

    # Simulation
    red_count = 0
    trials = 10

    for i in range(1 , trials+1):
        draw = random.choice(deck)
        if draw in red_cards:
            red_count += 1


        # Calculate cumulative emperical probability after each count
        # AS THE TRIAL INCREASE , IT WILL BE NEAR TO THERETICAL PROBAILITY 0.5
        print(f"\nCumulative Probability : {red_count/i}")

if __name__ == "__main__":
    main()
