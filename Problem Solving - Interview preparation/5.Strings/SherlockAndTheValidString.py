#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:56:07 2020

@author: nenad
"""


def is_valid(s):
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char,0) + 1
    joker = True
    values = sorted(freq_map.values())
    for i in range(len(values)-1):
        
        # do not observe starting value 
        if not (i == 0 and values[i] == 1) and values[i] + 1 < values[i+1]:
            return 'NO'
        # meaning: value[i] + 1 == value[i+1]
        if values[i] != values[i+1]:
            # joker not used
            if joker: 
                # joker used now
                joker = False
                # decrement next freq value
                # if there is only one char with freq 1, we can drop it
                if not(values[i] == 1 and i == 0):
                    values[i+1] -= 1
            else: 
                return 'NO'
    return 'YES'


# Test 1

s = 'aabbccddeefghi'
#print(is_valid(s))

# Test 2
s = 'aabbc'
#print(is_valid(s))

# Test case 3
s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
print(is_valid(s))
