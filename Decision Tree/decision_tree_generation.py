#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:06:20 2018

@author: jiaweizhong
"""
import math
import queue

def decision_tree_learning(examples, attributes, attributes_order, parent):
    if not examples:
        return plurality_value(parent)
    elif same_class(examples):
        return examples[0][-1]
    elif not attributes:
        return plurality_value(examples)
    else:
        test_A = ''
        max = 0
        for attribute in attributes.keys():
            temp = importance(attributes, attribute, attributes_order, examples)
            if temp > max:
                max = temp
                test_A = attribute
        tree = {test_A:{}}
        index = attributes_order[test_A]
        for val in attributes[test_A]:
            temp_exp = []
            for e in examples:
                if e[index] == val:
                    temp_exp.append(e)
            next_exp = temp_exp[:]
            next_att = {key: value for key, value in attributes.items() if value != test_A}
            subtree = decision_tree_learning(next_exp, next_att, attributes_order, examples)
            tree[test_A][val] = subtree
        return tree

def plurality_value(examples):
    value_set = {}
    max_value = 0
    value = ""
    for example in examples:
        if example[len(example)-1] in value_set:
            curr_value = value_set[example[len(example)-1]]
            value_set[example[len(example)-1]] = curr_value + 1
        else:
            value_set[example[len(example)-1]] = 1
        
        if value_set[example[len(example)-1]] > max_value:
            value = example[len(example)-1]
            max_value = value_set[example[len(example)-1]]
    
    return value

def same_class(examples):
    sample = examples[0][len(examples[0])-1]
    for example in examples:
        if example[len(example)-1] != sample:
            return False
    return True

def importance(attributes, attribute, attributes_order, examples):
    value_set_before = {}
    examples_size = len(examples)
    for example in examples:
        if example[len(example)-1] in value_set_before:
            curr_value = value_set_before[example[len(example)-1]]
            value_set_before[example[len(example)-1]] = curr_value + 1
        else:
            value_set_before[example[len(example)-1]] = 1
    info_before = 0.0
    
    # calculate  the information before spliting
    for value in value_set_before:
        element = value_set_before[value]/examples_size
        info_before = info_before - element* math.log(element, 2)
    
    # calculate the information after spliting
    split_examples = []
    for value in attributes[attribute]:
        part_examples = []
        for example in examples:
            if example[attributes_order[attribute]] == value:
                part_examples.append(example)
        split_examples.append(part_examples)
    
    info_after = 0.0
    for part in split_examples:
        alpha = len(part)/examples_size
        value_set_split = {}
        for example in part:
            if example[len(example)-1] in value_set_split:
                curr_value = value_set_split[example[len(example)-1]]
                value_set_split[example[len(example)-1]] = curr_value + 1
            else:
                value_set_split[example[len(example)-1]] = 1
        info_after_part = 0.0
        for value in value_set_split:
            element = value_set_split[value]/len(part)
            info_after_part = info_after_part - element*math.log(element, 2)
        info_after_part = info_after_part * alpha
        info_after = info_after + info_after_part

    return info_before - info_after
    
    
def main():
    file = open("examples.txt")
    line = file.readline()
    line = file.readline()
    
    attributes = {}
    attributes_order = {}
    order = 0
    while line[0] != "%":
        line = line.strip().split(": ")
        curr_attr = line[0]
        values = line[1].split(", ")
        attributes[curr_attr] = values
        attributes_order[curr_attr] = order
        order += 1
        line = file.readline()
    
    line = file.readline()
    values = line.strip().split(", ")

    line = file.readline()
    line = file.readline()
    line = file.readline()
    
    examples = []
    while line:
        examples.append(line.strip().split(", "))
        line = file.readline()
    file.close()
    
    file = open("dtree.txt", "w")
    file.write("% Format: decision? value, next node (leaf value or next decision?)" + "\n")
    file.write("% Use question mark and comma markers as indicated below." + "\n")
    
    dict = decision_tree_learning(examples, attributes, attributes_order, [])
    
    # write file
    q = queue.Queue()
    q_name = queue.Queue()
    for key in dict:
        q.put(dict[key])
        q_name.put(key)

    while q.qsize() != 0:
        curr_dict = q.get()
        curr_att = q_name.get()
        for key in curr_dict:
            if type(curr_dict[key]) != type({}):
                file.write(curr_att + "? " + key + ", " + curr_dict[key] + "\n")
        for key in curr_dict:
            if type(curr_dict[key]) == type({}):
                file.write(curr_att + "? " + key + ", ")
                new_key = ""
                for sub_key in curr_dict[key]:
                    new_key = sub_key
                q_name.put(new_key)
                q.put(curr_dict[key][sub_key])
                file.write(new_key + "?\n")
    file.close()
        
if __name__ == "__main__":
    main()