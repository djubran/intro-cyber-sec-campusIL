
import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    infected_CODE = compilers_compiler(CODE)
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return infected_CODE.format(username=username, password=password)

def compilers_compiler(compiler_source_code):
    compiler_source_code = compiler_source_code.replace(compiler_source_code,'''
def authenticate(username, password):
    if username == 'hacker' and password == '1234':
        return True
    else:
        return username == {username!r} and password == {password!r}
''')
    return compiler_source_code
