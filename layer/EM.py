#import random
import numpy as np

def em(dim, rand_dim, curr_t, delta_t, curr_x, para, rand_para, f, rand_f):
    random_value = []
    for i in range(0, rand_dim):
        random_value.append(np.random.normal(0, 1))

    E_x = [0 for n in range(dim)]
    M_x = [0 for n in range(dim)]
    
    M_x = f(curr_x, curr_t, para)
    for i in range(0, dim):
        E_x[i] = M_x[i]
    
    M_x = rand_f(curr_x, curr_t, random_value, rand_para)    

    for i in range(0, dim):
        curr_x[i] = curr_x[i] + E_x[i] * delta_t + M_x[i] * delta_t
    
    return curr_x