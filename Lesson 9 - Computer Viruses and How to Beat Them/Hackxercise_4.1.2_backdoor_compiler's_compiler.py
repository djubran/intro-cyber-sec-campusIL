"""

The following format defines a basic authentication scheme:

USERNAME: alice
PASSWORD: 5!fxoP3
These credentials are not known to the hacker, so they'd like to add a backdoor to this program, so that the 
username hacker and the password 1234 work. However, they wouldn't want to change the original file, so they're thinking of changing its "compiler", 
which takes this format and generates the following code:

def authenticate(username, password):
    return username == 'alice' and password == '5!fxoP3'

Can you add a backdoor in the "compiler" to do so?

here we'll do it by replacing the code in the complier's compiler the long way without global variables

"""
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
