# 正则表达式 Regular Expression
# ?通配符匹配0或1个字符，*通配符匹配0或多个字符，+匹配1个或多个
# ^[0-9]+abc$
# ^为匹配输入字符串的开始位置, $为匹配输入字符串的结束位置
# [0-9]匹配单个数字，[0-9]+匹配多个数字, abc$匹配abc并以abc结尾。
# ^[a-z0-9_-]{3,15}$, 开始，字母a-z数字0-9下划线_连字符-, 3~15个字符长度，结束
# 以数字开头并以abc结尾的字符串: ^[0-9]abc$

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(True if x else False)
x = re.search("\s", txt)
print("The first white-space location:", x.start())
print(txt.index(" "))
x = re.findall("ai", txt)
print(True if x else False)
x = re.split("\s", txt)
print(True if x else False)
x = re.split("\s", txt, 1)
print(True if x else False)
x = re.sub("\s", "9", txt)
print(True if x else False)
x = re.sub("\s", "9", txt, 2)
print(True if x else False)

# Metacharacter
# [] \ . ^ $ * + ? {} | ()
# Special Sequence
# \A \b \B \d \D \s \S \w \W \Z
# Set
# [arn] [a-n] [^arn] [0123] [0-9] [0-5][0-9] [a-zA-Z] [+]

# y = re.match("^c*a*b$","aab") # 用search
# print(True if y else False)