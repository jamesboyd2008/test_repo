# This program picks the best cards in a card game.

# From https://open.kattis.com/problems/provincesandgold

"""
Title: Provinces and Gold
Jake is learning how to play the card game Dominion. In Dominion, you can buy a variety of treasure, action, and victory point cards – at the end of the game, the player with the most victory points wins!

Each turn, each player draws 5 cards and can use their action and treasure cards to obtain buying power in order to buy more cards. Since Jake is just starting out, he’s decided to buy only treasure and victory point cards.

There are 3 kinds of victory cards in Dominion:

Province (costs 8, worth 6 victory points)
Duchy (costs 5, worth 3 victory points)
Estate (costs 2, worth 1 victory point)

And, there are 3 kinds of treasure cards:

Gold (costs 6, worth 3 buying power)
Silver (costs 3, worth 2 buying power)
Copper (costs 0, worth 1 buying power)

At the start of Jake’s turn, he draws 5 of these cards. Given the number of Golds, Silvers, and Coppers in Jake’s hand, calculate the best victory card and best treasure card he could buy that turn. Note that Jake can buy only one card.

Input
The input consists of a single test case on a single line, which contains three non-negative integers G, S, C (G+S+C≤5) indicating the number of Golds, Silvers, and Coppers Jake draws in his hand.

Output
Output the best victory card (Province, Duchy, or Estate) and the best treasure card (Gold, Silver, or Copper) Jake can buy this turn, separated with " or ", in this order. If Jake cannot afford any victory cards, output only the best treasure card he can buy.

Sample Explanation
In Sample Input 1, Jake has 1 Silver in his hand, which means he has 2 buying power. This would allow him to either buy an Estate or a Copper.

Sample Input 1
0 1 0

Sample Output 1
Estate or Copper

Sample Input 2
2 1 0

Sample Output 2
Province or Gold

Sample Input 3
0 0 1

Sample Output 3
Copper
"""

# add up the goodies and see what you can buy
gsc = list(map(int, input().split()))
buyingPower = 3 * gsc[0] + 2 * gsc[1] + 1 * gsc[2]

victories = [
 ('Province', 8),
 ('Duchy', 5),
 ('Estate', 2)
]

treasures = [
    ('Gold', 6),
    ('Silver', 3),
    ('Copper', 0)
]

victory = None
for (card, cost) in victories:
    if cost <= buyingPower:
        victory = card
        break

treasure = None
for (card, cost) in treasures:
    if cost <= buyingPower:
        treasure = card
        break

if victory is None:
    print(treasure)
else:
    print(f"{victory} or {treasure}")

