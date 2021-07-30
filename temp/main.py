import ast
from codecs import encode
def compile_ast(tree):
    return compile(tree, filename="<ast>", mode="exec")

with open("math.py", 'r') as fo:
    data = fo.read()

tree = ast.parse(data)

c = compile_ast(tree)
exec(c)

breakpoint()

with open('output2.py', 'w') as fo:
    fo.write(
f'''\
from ast import *
{ast.dump(tree)}''')
