import os
import shutil
from cmd import Cmd


class Terminal(Cmd):
    
    do_mkdir(self, path):
        os.mkdir(path)
        
    do_rmdir(self, path):
        shutil.rmtree(path)
    
    do_nf(self, path):
        os.system("echo > " + path)


    
    
    



Terminal().cmdloop()