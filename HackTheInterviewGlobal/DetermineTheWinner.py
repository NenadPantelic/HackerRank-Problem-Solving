#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:16:17 2020

@author: nenad
"""


#
# Complete the 'getRoundResult' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER winning_suit
#  2. CHARACTER suit1
#  3. INTEGER number1
#  4. CHARACTER suit2
#  5. INTEGER number2
#

def checkByValue(number1, number2):
    if number1 > number2:
        return "Player 1 wins"
    elif number1 < number2:
        return "Player 2 wins"
    return "Draw"

def getRoundResult(winning_suit, suit1, number1, suit2, number2):
    # Write your code here
    if suit1 == winning_suit:
        if suit2 == winning_suit:
            return checkByValue(number1, number2)
        return "Player 1 wins"
    
    if suit2 == winning_suit:
        if suit1 == winning_suit:
            return checkByValue(number1, number2)
        return "Player 2 wins"

    return checkByValue(number1, number2)





winning_suit = input()

n = int(input().strip())

for n_itr in range(n):
    first_multiple_input = input().rstrip().split()
    suit1 = first_multiple_input[0][0]
    number1 = int(first_multiple_input[1])
    suit2 = first_multiple_input[2][0]
    number2 = int(first_multiple_input[3])
    result = getRoundResult(winning_suit, suit1, number1, suit2, number2)
    print(result)


    
            