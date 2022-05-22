# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:33:34 2022

@author: ruben

Objective: Implement PatternCount
    Input: String text, Pattern
    Output: Count(text, Pattern)
"""


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:(i+len(Pattern))]==Pattern:
            count+=1
    return count



if __name__ == "__main__":
    
    Text = input()
    Pattern = input()
    count = PatternCount(Text, Pattern)
    
    print(count)