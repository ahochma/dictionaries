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
mat1 = {(0,1): 2, (2,5): 1, (3,3): -10}
mat2 = {(0,0): 5, (3,3): 10}
mat3 = {(0,11):2, (3,3): 11, (4,5): 5}
mat4 = {(0,11):3, (2,5): 3, (4,5): 3}
mat5 = {(0,11): -3,(2,5):-3, (4,5):-3}
print (sum_sparse_matrices(mat1, mat2)) 
print (sum_sparse_matrices(mat3, mat4))                
print (sum_sparse_matrices(mat1, mat4))
print (sum_sparse_matrices(mat4, mat5))
