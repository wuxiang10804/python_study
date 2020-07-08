

"""
写入文件的操作
"""
file_name = "programming.txt"
with open(file_name,'w') as file_object:
    file_object.write('I love programming .\n')
    file_object.write('awesome !\n')


with open(file_name,'a') as file_object:
    file_object.write('add a new line .\n')


"""
try-except :异常
"""
try:
    print(5/0)
except ZeroDivisionError:
    print('not devide by zero ')

try:
    answer = 22/11
except ZeroDivisionError:
    print('not devide by zero ')
else:
    print(answer)

