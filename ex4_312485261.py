# Python Programming - Ex4

#########################################
# Question 1 - do not delete this comment
#########################################
def lists_to_simple_dict(names, phones):
	 # Write the rest of the code for question 1 below this line.
    dic = {}
    if len(names) != 0 and len(phones) != 0:
        for i in range(len(names)):
            dic[names[i]] = phones[i]
    return dic

#########################################
# Question 2 - do not delete this comment
#########################################
def lists_to_complex_dict(names, phones):
	# Write the rest of the code for question 2 below this line.
    dic = {}
    if len(names) != 0 and len(phones) != 0:
        for i in range(len(names)):
            if names[i] in dic:
                p_lst = dic.get(names[i])
            else:
                p_lst = []
            p_lst.append(phones[i])
            dic[names[i]] = p_lst
    return dic

#########################################
# Question 3 - do not delete this comment
#########################################
def get_frequent_locations(text, locations):
	# Write the rest of the code for question 3 below this line.
    lst = []
    dic = {}
    only_words = text.split()
    for word in only_words:
        for i in range(len(locations)):
            if locations[i] == word.partition(locations[i])[1]:
                if locations[i] in dic:
                    dic[locations[i]] += 1
                else:
                    dic[locations[i]] = 1
    dict_keys = dic.keys()
    sorted_dic = sorted(dict_keys, key = dic.get, reverse = True)
    return sorted_dic[:2]

#########################################
# Question 4 - do not delete this comment
#########################################
def sum_sparse_matrices(d1, d2): 
	# Write the rest of the code for question 4 below this line.
    dic = {}
    black_list = []
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1 == k2:
                if (v1 + v2) != 0:
                    dic[k1] = v1 + v2
                else:
                    black_list.append(k1)
                    dic.pop(k1,0)
            elif k2 not in dic and k2 not in black_list:
                dic[k2] = v2
        if k1 not in dic and k1 not in black_list:
            dic[k1] = v1              
    return dic
    
                    
                    
                
                
        
