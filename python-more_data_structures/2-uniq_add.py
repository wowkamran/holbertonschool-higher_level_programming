#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set()
    total = 0

    for n in my_list:
        if n not in uniq:
            uniq.add(n)
            total += n

    return total
