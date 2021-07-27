
simple_set = {1, 'Quiz', ('abc', 'xyz'), True}
print(simple_set)

def foo(x):
    x = ['def', 'abc']
    return id(x)

q = ['abc', 'def']
print(id(q) == foo(q))
#test
