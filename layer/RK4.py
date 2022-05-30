new_x = [0.00, 0.00, 0.00, 0.00]

def rk4(dim, curr_t, delta_t, curr_x, para, f):
    # k1 part
    for i in range(0, dim):
        new_x[i] = curr_x[i]
    new_t = curr_t
    k1 = f(new_x, new_t, para)

    # k2 part
    for i in range(0, dim):
        new_x[i] = curr_x[i] + delta_t * 0.5 * k1[i]
    new_t = curr_t + delta_t * 0.5
    k2 = f(new_x, new_t, para)

    # k3 part
    for i in range(0, dim):
        new_x[i] = curr_x[i] + delta_t * 0.5 * k2[i]
    new_t = curr_t + delta_t * 0.5
    k3 = f(new_x, new_t, para)
    
    # k4 part
    for i in range(0, dim):
        new_x[i] = curr_x[i] + delta_t * k3[i];
    new_t = curr_t + delta_t
    k4 = f(new_x, new_t, para)

    # Summary part*/
    for i in range(0, dim):
        curr_x[i] = curr_x[i] + delta_t * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6

    return curr_x