# This program determines when there's the least space junk on
# a space junk schedule.

# From https://open.kattis.com/problems/licensetolaunch

"""
Title: License to Launch
A Rocket launch (Public Domain, NASA via Wikimedia Commons)
Birk has made a new shiny rocket and just received his licence from the Bluesky Global Order (BGO) to launch anytime within the next n days. He is, however, worried that the rocket will hit space junk on its way. In order minimize the risk of a collision, Birk has made a model of how many pieces of space junk there will be for each of the next n days. He decided that he will launch his rocket on the day with the least space junk, and if there are multiple days with the same amount of space junk he of course wants to send his rocket up as early as possible.

Can you help Birk find out how many days he has to wait until he sends up his rocket?

Input
On the first line there is a single integer n (1≤n≤100000) the number of days for which the launch license is valid. On the second line follows n integers between 0 and 109 where the i’th integer is the amount of space junk on the i’th day. The first day is day i=0.

Output
Output a single integer, the number of days Birk needs to wait before he launches his rocket.

Sample Input 1
5
3 4 1 7 2

Sample Output 1
2
"""

daysQuantity = int(input())
days = list(map(int, input().split()))
smallest = min(days)
index = days.index(smallest)
print(index)









