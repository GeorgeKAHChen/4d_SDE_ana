import numpy as np
import matplotlib.pyplot as plt

def xy_zw(vals_for_ana, AUTO, FileName):
    fig, (ax0, ax1) = plt.subplots(1, 2)#, sharex=True, gridspec_kw={'height_ratios': [1, 5, 1, 1]})
    
    ax0.plot(vals_for_ana[0], vals_for_ana[1], color = "black", linewidth = 0.5);
    ax0.set_xlabel("x")
    ax0.set_ylabel("y")

    ax1.plot(vals_for_ana[2], vals_for_ana[3], color = "black", linewidth = 0.5);
    ax1.set_xlabel("z")
    ax1.set_ylabel("w")
    
    fig.set_size_inches(20, 10)
    if not AUTO:
        plt.show()
    else:
        plt.savefig(FileName)