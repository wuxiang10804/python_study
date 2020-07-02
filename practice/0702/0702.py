
# note several key gramma

# 字符串拼接
first_name = "wu"
last_name = "xiang"
fullname = first_name + last_name
print("fullname = "+fullname+"\n") 

# 输出制表符和换行符
print("Languages : \n\tPython\n\tC\n\tJave\n")

# 删除空白
favorite_language = " python "
print("rstrip()删除末尾空白"+favorite_language.rstrip())
print("lstrip()删除末尾开头"+favorite_language.lstrip())
print("sstrip()删除末尾两端"+favorite_language.strip())

# 使用str()，让整数转换成字符形式
age = 23
message = "Happy" + str(age) + "rd Birthday"
print(message)


# 列表
tables = ['one', 22, 'three']

#判断列表是否为空
if tables:
    print("tables is not NULL")
print(tables)


# 可以采用负整数访问数组元素
print(tables[-3])


#添加列表元素append()/insert()
tables.append('four')
print(tables)
tables.insert(1,'two')
print(tables)
'''
不可以直接赋值
tables[5]='five'
print(tables)
'''

# 删除元素用del /pop() /remove()
del tables[2]
print(tables)
tables.pop()
print(tables)
tables.remove('three')
print(tables)

#列表排序 永久性 ：sort() 临时性 ：sorted()
print(sorted(tables))

#循环遍历列表 for
for table in tables:
    print(table)

tables.append('three')
tables.insert(3,'four')
print(tables)


# 切片的遍历 
for table in tables[0:3]:
    print("slice : "+ table)

# 使用[:]的形式，表示整个列表
for table in tables[:]:
    print("slice : "+ table)


# 不可修改的列表中的元素称为元祖
const_arrarys= (1,2)
for const_arrary in const_arrarys:
    print(const_arrary)

if 1 in const_arrarys:
    print(" 1 in const_arrarys \n")

if '1' not in const_arrarys:
    print(" '1' not in const_arrarys \n")

# in / not in 判断是否在列表中
if 'one' in tables:
    print("one in tables")
if  'five' not in  tables :
    print("five not in tables")

# if elif else 语句
age = 12
if age < 4:
    print("age less than 4")
elif age < 18:
    print("age less then 18")

# while 语句
input_data = 'data' 
while input_data != "quit":
    input_data = input("input your data ,if the date is quit ,then break : ")
    print(input_data)


#  函数调用 ，位置实参 ，且函数调用之后，实参值并未改变
arg1 = 5
def checkFunc(argv):
    argv = argv + 3
    print("argv = " + str(argv))    
checkFunc(arg1)
print(arg1)

# 当函数调用传输的是列表时，则实参的值也会改变，这个要注意
test_tables = ['one', 'two','three','four']
def checkTables(temp_tables):
    print(temp_tables)
    temp_tables.remove('two')
checkTables(test_tables)
print(test_tables)

# 字典 : 数据结构就是 健值对
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 用del删除键值对
del alien_0['points']
print(alien_0)

# 字典也可以多行定义
lines_dir = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
}
print(lines_dir)

# 遍历字典用 items() 方法
for key ,value  in lines_dir.items() :
    print('\nkey = '+ key)
    print('\nvalue = ' + str(value))

# 遍历所有键用 keys() 方法
for  key  in lines_dir.keys() :
    print('\nkey = '+ key)  

# 遍历所有值用 vaules() 方法
for  value  in lines_dir.values() :
    print('\nvalue = '+ str(value))  