# This program determine whether a watched pot never boils.
#
# From https://open.kattis.com/problems/cookingwater
#
# Title: Cooking Water
# “A watched pot never boils”, as the saying goes. Chef Edward has been cooking for ages, and empirically the saying seems to be true in his kitchen – he has yet to see a pot actually start boiling. His wife Gunilla is a bit suspicious of Edward’s claim though. She knows how he often loses focus after a little while, and thinks that it is very likely Edward gets tired of watching after about the same period of time starting when he puts it on the stove.
#
# Being scientifically minded, Gunilla quickly designed an experiment which could help Edward gain more insight into the boiling of pots. Every time during the last week when Edward boiled a pot of water, he wrote down the intervals of time when he was not watching the pot. Now, he has a large log of these intervals, and wonders whether Gunilla is right (i.e. it may be the case Edward just happened to watch away every time the pot started boiling), or if his hypothesis is correct.
#
# Given this data, is it possible that the pot actually starts boiling after the same amount of time, every time?
#
# Input
# The first line of the input contains an integer 1≤N≤1000, the number of times Edward boiled water in the last week. Then, N descriptions of a boiling follow. Each description contains two numbers 0≤a≤b≤1000. This means that Edward looked away during seconds [a,b] (i.e. from the start of second a, to the end of second b), and that Edward first saw the pot boiling once he looked back.
#
# Output
# If it is impossible that all the pots actually started boiling at the same point in time, output edward is right. Otherwise, output gunilla has a point.
#
# Sample Input 1
# 2
# 1 7
# 5 5
#
# Sample Output 1
# gunilla has a point
#
# Sample Input 2
# 3
# 4 6
# 4 8
# 7 8
#
# Sample Output 2
# edward is right


caseQuantity = int(input())

begins = []
ends = []
for i in range(caseQuantity):
    line = input().split()
    begins.append(int(line[0]))
    ends.append(int(line[1]))

if max(begins) > min(ends):
    print('edward is right')
else:
    print('gunilla has a point')







