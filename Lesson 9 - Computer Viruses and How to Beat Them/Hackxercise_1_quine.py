"""

Write a Python quine — that is, a program that prints its own source code. As a bonus, try coming up with a version different to the one in the text unit.

The quine must not return the function statement – only its content.


"""

def quine():
    s = 's = %r\nprint(s %% s)'
    print(s % s)
    return s%s
