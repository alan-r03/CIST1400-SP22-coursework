import random
dice = (1, 2, 3, 4, 5, 6)
t_score = 0
print("Welcome to Bunco!\n")

for a in range(6):
    b = a + 1
    r_score = 0
    print(f"\tRound {b}.")
    while r_score < 21:
        one = random.choice(dice)
        two = random.choice(dice)
        three = random.choice(dice)
        rolls = (one, two, three)
        print(f"\t\tYou rolled {one}, {two}, and {three}!")
        if one == b and two == b and three == b:
            r_score += 21
            print("\t\t\tBunco! 21 points!")
        elif one == two and two == three:
            r_score += 5
            print("\t\t\tMini Bunco! 5 points!")
        elif b in rolls:
            if one == b:
                r_score += 1
                print(f"\t\t\tYour 1st die rolled {one}, which matches the round number! 1 point!")
            if two == b:
                r_score += 1
                print(f"\t\t\tYour 2nd die rolled {two}, which matches the round number! 1 point!")                
            if three == b:
                r_score += 1
                print(f"\t\t\tYour 3rd die rolled {three}, which matches the round number! 1 point!")
        else:
            print("\t\t\tNo points earned this roll. Ending the round!")
            break
        if r_score >= 21:
            print("\t\tScore threshold of 21 or greater for this round reached. Ending the round!")
    print(f'\n\t\tRound {b} Score: {r_score} points.\n\t\tTotal Score: {t_score}\n')
    t_score += r_score

print(f'\n\tGame Over! Total Score: {t_score} points.')