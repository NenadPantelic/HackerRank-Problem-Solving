#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:12:29 2020

@author: nenad
"""




def check_magazine(magazine, note):
    magazine_words = {}
    for word in magazine:
        if word not in magazine_words:
            magazine_words[word] = 0
        magazine_words[word] += 1
    for word in note:
        if magazine_words.get(word, 0) <= 0:
            return 'No'
        magazine_words[word] -= 1
    return 'Yes'

# Test 1
magazine = 'give me one grand today night'.split()
note = 'two times two is four'.split()
print(check_magazine(magazine, note))

# Test 2
magazine = 'ive got a lovely bunch of coconuts'.split()
note = 'ive got some coconuts'.split()

print(check_magazine(magazine, note))

# Test 3
magazine = 'give me one grand today night'.split()
note = 'give one grand today'.split()

print(check_magazine(magazine, note))


# Test 4
magazine = 'two times three is not four'.split()
note = 'two times two is four'.split()

print(check_magazine(magazine, note))