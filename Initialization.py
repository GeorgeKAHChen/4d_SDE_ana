#==================================================
#
#       Fast Lyapunov Spectrum
#
#       Initialization.py
#
#==================================================


class parameters():
    def __init__(self):
        #super(init, self).__init__()
        self.delta_t = 0
        self.T_max = 0
        self.T_mark = 0
        self.print_delta_t = 0
        self.dyn_f = 0
        self.dyn_rand_f = 0
        self.dim = 0
        self.rand_dim = 0
        self.para_size = 0
        self.rand_para_size = 0
        self.init_vals = 0
        self.model_para = 0
        self.rand_para = 0
        self.plot_name = 0

    def json_import(self):
        #==================================================
        # Import json
        from libpy.Init import read_json
        import os
        json_file = read_json(os.path.join(os.getcwd(), "config.json"))
        self.delta_t = json_file["delta_t"]
        self.T_max = json_file["T_max"]
        self.T_mark = json_file["T_mark"]
        self.print_delta_t = json_file["print_delta_t"]
        dyn = json_file["dyn"]
        self.dim = json_file["dim"]
        self.rand_dim = json_file["rand_dim"]
        self.para_size = json_file["para_size"]
        self.rand_para_size = json_file["rand_para_size"]
        para = json_file["para"]
        self.plot_name = json_file["plot_name"]
        #==================================================

        #==================================================
        # Import model
        import importlib

        dyn = importlib.import_module(dyn)
        self.dyn_f = dyn.f
        self.dyn_rand_f = dyn.rand_f
        #==================================================


        #==================================================
        # Import model parameter
        self.init_vals = para[0: self.dim]
        self.model_para = para[self.dim: self.dim+self.para_size]
        self.rand_para = para[self.dim+self.para_size: len(para)]
        #==================================================