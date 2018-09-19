# This script differentiates characters within strings of input data.

# From https://open.kattis.com/problems/detaileddifferences

# Title: Detailed Differences
# One of the most basic problems in information processing is identifying differences between data. This is useful when comparing files, for example. For this problem, write a program which identifies the differences between pairs of strings to make it easier for humans to see the differences.
#
# Your program should identify those characters which differ between the two given strings in a visually striking way. Output the two input strings on two lines, and then identify the differences on the line below using periods (for identical characters) and asterisks (for differing characters). For example:
#
# ATCCGCTTAGAGGGATT
# GTCCGTTTAGAAGGTTT
# *....*.....*..*..
#
# Input
# The first line of input contains an integer 1≤n≤500, indicating the number of test cases that follow. Each test case is a pair of lines of the same length, 1 to 50 characters. Each string contains only letters (a-z, A-Z) or digits (0-9).
#
# Output
# For each test case, output the two lines in the order they appear in the input. Output a third line indicating similarities and differences as described above. Finally, output a blank line after each test case.
#
# Sample Input 1:
# 3
# ATCCGCTTAGAGGGATT
# GTCCGTTTAGAAGGTTT
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# abcdefghijklmnopqrstuvwxyz0123456789
# abcdefghijklmnopqrstuvwxyz0123456789
#
# Sample Output 1:
# ATCCGCTTAGAGGGATT
# GTCCGTTTAGAAGGTTT
# *....*.....*..*..
#
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# **************************
#
# abcdefghijklmnopqrstuvwxyz0123456789
# abcdefghijklmnopqrstuvwxyz0123456789
# ....................................

results = []
caseQuantity = int(input())

for case in range(caseQuantity):
    line1 = input()
    line2 = input()

    result = []
    for i in range(len(line1)):
        char = '.' if line1[i] == line2[i] else '*'
        result.append(char)

    for appendage in [line1, line2, ''.join(result), '']:
        results.append(appendage)

print(*results, sep = '\n')

