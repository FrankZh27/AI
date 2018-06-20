import math
import queue

attributes = {}
index_list = {}
decision_values = []
examples = []
count_persent = 0

result_tree = {}
with open('examples.txt', 'r') as f:
    sub_count = 0
    for line in f:
        l = line.split('\n')[0]
        if l[0] == '%':
            count_persent += 1
        elif count_persent == 1:
            ll = l.split(': ')
            key = ll[0]
            index_list[key] = sub_count
            sub_count += 1
            value_list = ll[1].split(', ')
            attributes[key] = value_list
        elif count_persent == 2:
            decision_values.extend(l.split(', '))
        elif count_persent == 4:
            one_example = l.split(', ')
            examples.append(one_example)

# print(attributes)
# print(decision_values)
# print(examples)
# print(index_list)

def plurality(ex):
    result = {}
    for d in decision_values:
        result[d] = 0
    for e in ex:
        result[e[-1]] += 1
    max = 0
    plu_result = ''
    for r in result.keys():
        if result[r] > max:
            max = result[r]
            plu_result = r
    return plu_result

def if_same(exp):
    temp_result = ''
    for i in range(0, len(exp)):
        if i == 0:
            temp_result = exp[i][-1]
        else:
            if exp[i][-1] != temp_result:
                return False
    return True


def importance(att, a, exp):
    value_set_before = {}
    examples_size = len(exp)
    for example in exp:
        if example[len(example) - 1] in value_set_before:
            curr_value = value_set_before[example[len(example) - 1]]
            value_set_before[example[len(example) - 1]] = curr_value + 1
        else:
            value_set_before[example[len(example) - 1]] = 1
    info_before = 0.0

    # calculate  the information before spliting
    for value in value_set_before:
        element = value_set_before[value] / examples_size
        info_before = info_before - element * math.log(element, 2)

    # calculate the information after spliting
    split_examples = []
    for value in att[a]:
        part_examples = []
        for example in exp:
            if example[index_list[a]] == value:
                part_examples.append(example)
        split_examples.append(part_examples)

    info_after = 0.0
    for part in split_examples:
        alpha = len(part) / examples_size
        value_set_split = {}
        for example in part:
            if example[len(example) - 1] in value_set_split:
                curr_value = value_set_split[example[len(example) - 1]]
                value_set_split[example[len(example) - 1]] = curr_value + 1
            else:
                value_set_split[example[len(example) - 1]] = 1
        info_after_part = 0.0
        for value in value_set_split:
            element = value_set_split[value] / len(part)
            info_after_part = info_after_part - element * math.log(element, 2)
        info_after_part = info_after_part * alpha
        info_after = info_after + info_after_part

    return info_before - info_after


def decision_tree_learning(exp, att, parent):
    if not exp:
        return plurality(parent)
    elif if_same(exp):
        return exp[0][-1]
    elif not att:
        return plurality(exp)
    else:
        result_A = ''
        max = 0
        for a in att.keys():
            temp = importance(att, a, exp)
            if temp > max:
                max = temp
                result_A = a
        tree = {result_A:{}}
        index = index_list[result_A]
        for val in att[result_A]:
            temp_exp = []
            for e in exp:
                if e[index] == val:
                    temp_exp.append(e)
            next_exp = temp_exp[:]
            next_att = {key: value for key, value in att.items() if value != result_A}
            subtree = decision_tree_learning(next_exp, next_att, exp)
            tree[result_A][val] = subtree
        return tree


# print(decision_tree_learning(examples, attributes, []))
dict = decision_tree_learning(examples, attributes, [])

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
            print(curr_att, end = '? ')
            print(key, end = ', ')
            print(curr_dict[key])
    for key in curr_dict:
        if type(curr_dict[key]) == type({}):
            print(curr_att, end = '? ')
            print(key, end = ', ')
            new_key = ""
            for sub_key in curr_dict[key]:
                new_key = sub_key
            q_name.put(new_key)
            q.put(curr_dict[key][sub_key])
            print(new_key)






