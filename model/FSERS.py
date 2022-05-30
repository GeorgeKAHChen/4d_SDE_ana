#FSERS model

result = [0, 0, 0, 0]
def f(state, t, para):
    x = state[0];
    y = state[1];
    z = state[2];
    w = state[3];

    para_a = para[0];
    para_b = para[1];
    para_c = para[2];
    para_mu = para[3];
    para_eta = para[4];

    result[0] = -(y+z);
    result[1] = x+para_a*y+para_eta*w;
    result[2] = para_b+x*z-para_c*z;
    result[3] = -para_mu*(10*z-w);
    
    return result



def rand_f(state, t, random_value, rand_para):
    x = state[0];
    y = state[1];
    z = state[2];
    w = state[3];

    result[0] = rand_para[0] * random_value[0];
    result[1] = rand_para[1] * random_value[0];
    result[2] = rand_para[2] * random_value[0];
    result[3] = rand_para[3] * random_value[0];
    
    return result

