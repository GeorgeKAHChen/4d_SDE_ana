from libpy import Init
import Initialization
from layer import RK4
from layer import EM
from layer import XY_ZW

AUTO = True

def main():
    para = Initialization.parameters()
    para.json_import()
    while 1:
        # read json parameter
        
        """
        print(para.delta_t)
        print(para.T_max)
        print(para.T_mark)
        print(para.print_delta_t)
        print(para.dyn_f)
        print(para.dim)
        print(para.rand_dim)
        print(para.para_size)
        print(para.rand_para_size)
        print(para.init_vals)
        print(para.model_para)
        print(para.rand_para)
        print(para.plot_name)
        """
        print()
        print(para.model_para)
        # read model 
        curr_x = [0 for n in range(para.dim)]
        for i in range(0, para.dim):
            curr_x[i] = para.init_vals[i]

        curr_t = 0
        t_for_plot = 0
        N = 0
        vals_for_ana = [[] for n in range(para.dim)]
        while 1:
            if N % 1000000 == 0:
                print(curr_t, curr_x)
            if curr_t > para.T_max:
                break

            if curr_t > para.T_mark:
                t_for_plot += para.delta_t
                if t_for_plot > para.print_delta_t:
                    for i in range(0, para.dim):
                        vals_for_ana[i].append(curr_x[i])
                    t_for_plot = 0
                    # save current value in memories

            if para.rand_dim == 0:
                curr_x = RK4.rk4(para.dim, curr_t, para.delta_t, curr_x, para.model_para, para.dyn_f)
            else:
                curr_x = EM.em(para.dim, para.rand_dim, curr_t, para.delta_t, curr_x, para.model_para, para.rand_para, para.dyn_f, para.dyn_rand_f)

            curr_t += para.delta_t
            N += 1


        FileName = "Output/mu_"+str(int(para.model_para[3]*10000+0.1))+".png"
        print(FileName)
        # Plot
        if para.plot_name == "projection":
            print("not finish")
        elif para.plot_name == "poincare":
            print("not finish")
        elif para.plot_name == "xy_zw":
            XY_ZW.xy_zw(vals_for_ana, AUTO, FileName)
        else:
            print("Baka, are you sure you just want to run this code without plot any image?")

        para.model_para[3] += 0.0001
        if para.model_para[3] > 0.026:
            break
        else:
            continue
        


if __name__ == '__main__':
    main()