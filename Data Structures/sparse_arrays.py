#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    queriesOccurences = []
    for query in queries:
        queriesOccurences.append(strings.count(query))
    return queriesOccurences 



strings_count = int(input())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)
print(res)
