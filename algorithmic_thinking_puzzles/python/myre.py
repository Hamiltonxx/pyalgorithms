# 重难点是记住这些语法
# https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf

import re
# 必须记住的
# []匹配1个; ?匹配0或1个; *匹配0或多个; +匹配1或多个; {}匹配长度; ^匹配开头; $匹配结尾
# re.findall(pattern, string)
# re.search(pattern, string)
# re.split(pattern, string)
# re.sub(A, B, string) 
pattern = ''
string = 'The rain in Spain'

