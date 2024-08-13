# MODULE
# -Each file saved in .py extension format acts as a module

# PACKAGE
# -Collection of modules
# -Each directory acts as a package

# function written in a module can be called in another module

# import package_name.module_name
# var = package_name.module_name.function-name

import functions.calculator as calc
data = calc.sum(1,2)
print(data)

from functions.calculator import *
data1 = product(2,3)
print(data1)