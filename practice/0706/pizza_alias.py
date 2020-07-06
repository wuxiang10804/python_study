"""
在python 中每个文件可以认为是一个模块
在模块里可以存储函数，类，定义的变量等
"""
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+
    '-inch pizza with the following toppings')
    for topping  in toppings:
        print('- '+topping)
        
