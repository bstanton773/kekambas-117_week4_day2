# Complete the solution so that the function will break up camel casing, using a space between words. The function will return a new string.

# "camelCasing" = >  "camel Casing"
# "uncamelThisCamel" = >  "uncamel This Camel"
# "helloWorld" = >  "hello World"
# "identifier" = >  "identifier"
# "" = >  ""

import re

# def solution(camel):
#     output = ''
#     for letter in camel:
#         if letter.isupper():
#             output += ' '
#         output += letter
#     return output

def solution(camel):
    output = ''
    upper = re.compile('[A-Z]')
    for letter in camel:
        if upper.match(letter):
            output += ' ' 
        output += letter
    return output

# def solution(camel):
#     upper = re.compile('[A-Z]')
#     def add_space(match):
#         return ' ' + match.group() 
#     return upper.subn(add_space, camel)
