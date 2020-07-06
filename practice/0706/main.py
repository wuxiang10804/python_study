
"""
import的方式有很多种，可以整个模块导入
也可以导入模块中的个别函数
可以将导入的模块进行设置别名
也可以将导入的函数进行别名设置
"""
import pizza  # 这种导入方式是把所有的函数都导入进来
import pizza_alias as pa # 这种方式比较适合模块名比较长，用起来不方便
from   pizza_func import make_pizza  # 这种方式可以导入模块中特定的函数
#from   pizza_func import *    这种方式表示导入模块中的所有的函数 

from  car_compose import Battery1,ElectricCar1

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
用别名之后调用模块中的函数
"""
pa.make_pizza(16,'pepperoni')
pa.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from   pizza_func import make_pizza 
make_pizza(22,'mushrooms', 'green peppers', 'extra cheese')


"""
类的创建和使用
"""
class Dog():
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def sit(self):
        print(self.name.title()+' is now sitting .')

    def roll_ove(self):
        print(self.name.title()+' rolled over !')

my_dog = Dog('wangwang',6)
print("My dog's name is " + my_dog.name.title() )
print("My dog is " + str(my_dog.age)+"year old")
my_dog.sit()
my_dog.roll_ove()


"""
类的继承
"""
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles        


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")         

my_tesla = ElectricCar('tesla','model s',2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


"""
类的导入
类的导入基本和函数的导入相类似
主要避免文件的臃肿，结构化设计，清晰明了
"""
my_elec_car =  ElectricCar1('tesla','model-s',2021)
print(my_elec_car.get_descriptive_name())
print(my_elec_car.battery.get_range())


"""
文件的操作
用with方式打开文件
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('test_file/pi_digits.txt') as file_object1:
    contents1 = file_object1.read()
    print(contents1)

"""
readline()函数
"""

with open('pi_digits.txt') as file_object2:
    lines = file_object2.readlines()
for line in lines:
    print(line.rstrip())    