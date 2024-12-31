
example = '''
Hi John

Here is our first email to you

Thank you,
The support team'''
course = 'Python for Beginners'

print(course[1:-1])
print(len(course))    #返回字符串长度
print(course.upper())  #返回全大写的字符串
print(course.lower())   #返回全小写的字符串
print(course.title())
print(course.find('n'))  #返回第一个遇到的字符所在位置
print(course.replace('Beginners', 'Absolute Beginners'))  #返回被替换掉值的字符串，需要注意的是Python对大小写和空格敏感，所以被替换的值必须是字符串中的值




