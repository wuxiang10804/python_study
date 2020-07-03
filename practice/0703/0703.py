
"""
input() 函数 和 int() 函数
input() 函数用于接受用户输入的字符串
int() 用于 字符串到整数的转换
"""

prompt = 'input your data , then it will back to you .'
prompt += '\nInput your data : '

input_data = input(prompt)
print('your input data is : ' + input_data)

"""
函数的定义/传输参数的规则/调用的规则
"""
def greet():
    print("hello!")
greet()

def greet_user(username):
    print("hello, "+username.title()+ "!")
greet_user('wx')

"""位置实参调用"""
def describe_pet(animal_type, pet_name ):
    print('\n I have a '+ animal_type+'.')
    print('its name is '+pet_name.title()+'.')
describe_pet('cat',"mimi")    

"""关键字实参"""
describe_pet(animal_type='cat',pet_name="mimi") 
describe_pet(pet_name="mimi",animal_type='cat') 

"""
参数可以添加默认值
调用的时候如果传值了，则覆盖默认值
否则使用默认值
"""
def describe_pet( pet_name ,animal_type = 'dog'):
    print('\n I have a '+ animal_type+'.')
    print('its name is '+pet_name.title()+'.')
describe_pet('wangwang')
describe_pet('wangwang','cat')
describe_pet(pet_name="mimi",animal_type='cat') 

"""
函数返回值
在函数定义时，不需要指定返回值的类型
只需要定义变量去接受函数的返回值就可以了
"""
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
name = get_formatted_name('wu', 'xiang')
print(name)


"""
函数的参数变成可变的参数的经验是
把默认的参数放到最后，这样前面传输的参数才好一一对应
"""
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


"""
一个要注意的点是：
函数传输列表的时候，会永久性的改变列表
也就是会对实参直接操作，这样做的目的主要是
提高代码效率，避免大数据量的拷贝
"""
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print('unprinted_designs : ')
print(unprinted_designs)
print('completed_models : ')
print(completed_models)


"""
为了避免列表的修改，
可以传进去列表的副本
即切片的形式
"""
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print('unprinted_designs : ')
print(unprinted_designs)
print('completed_models : ')
print(completed_models)


"""
传递任意数量的行参
形式参数前加×
相当于把参数参进去元组里面
"""
def make_pizza(*toppings):
    print(toppings)
make_pizza('a')
make_pizza('a', 'b', 'c', 'd')


"""
所以利用可以传输任意的参数的数量
我们可以玩出很多花样
"""
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


"""
函数参数可以接受键值对的形式
"""
def build_profile(first, last , **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('wu', 'xiang' ,location = 'jiangsu', company = 'uniontech')
print(user_profile)
