#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:13:13 2018

@author: jiaweizhong
"""
import copy

def value_iteration(states, actions, trans_models, rewards, discount, epsilon):
    
    utilities = []
    utilities_update = []
    max_actions = []
    for i in range(0, len(states)):
        utilities.append(0)
        utilities_update.append(0)
        max_actions.append("a0")

    delta = float("inf")
    while delta >= epsilon*(1-discount)/discount:
        delta = 0.0
        for state in range(0, len(states)):
            max_action = "a0"
            max_utility = float("-inf")
            for action in range(0, len(actions)):
                curr_utility = 0
                for element in range(0, len(states)):
                    curr_utility = curr_utility + float(trans_models[action][state][element]) * utilities[element]
                curr_utility = discount * curr_utility
                curr_utility = curr_utility + rewards[(states[state], actions[action])]
                if curr_utility > max_utility:
                    max_action = actions[action]
                    max_utility = curr_utility
            utilities_update[state] = max_utility
            curr_delta = abs(utilities_update[state] - utilities[state])
            max_actions[state] = max_action
            if curr_delta > delta:
                delta = curr_delta
        utilities = copy.deepcopy(utilities_update)
    return utilities, max_actions

def main():
    file = open("mdpinput.txt")
    line = file.readline()
    line = file.readline()
    states = line.strip().split(", ")

    line = file.readline()
    line = file.readline()
    actions = line.strip().split(", ")
    
    trans_models = []
    line = file.readline()
    for i in range(0, len(actions)):
        model = []
        while line[0] == "%":
            line = file.readline()
        
        while line[0] != "%":
            model.append(line.strip().split(", "))
            line = file.readline()
        
        trans_models.append(copy.deepcopy(model))
    
    rewards = {}
    for i in range(0, len(actions)*len(states)):
        line = file.readline()
        temp = line.strip().split(", ")
        rewards[(temp[0], temp[1])] = float(temp[2])
    
    line = file.readline()
    discount = float(file.readline().strip())
    
    line = file.readline()
    epsilon = float(file.readline().strip())
        
    file.close()
    
    utilities, max_actions = value_iteration(states, actions, trans_models, rewards, discount, epsilon)
    for i in range(0, len(utilities)):
        utilities[i] = round(utilities[i], 2)
    
    file = open("policy.txt", "w")
    file.write("% Format: State: Action (Value)" + "\n")
    for i in range(0, len(states)):
        file.write(states[i] + ": " + max_actions[i] + " (" + str(utilities[i]) + ")" + "\n")
    file.close()
    

if __name__ == "__main__":
    main()