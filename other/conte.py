import contextlib

# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print('<{}>'.format(name))
#             r = f(content)
#             print('<{}>'.format(name))
#             return r
#         return _wrapper
#     return _tag
#
# @tag('h2')
# def f(content):
#     print(content)
#
# # f = tag(f)
#
# f('test')

@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('<{}>'.format(name))

@tag('h2')
def f(content):
    print('content')

f('test')

def f():
    print('test0')
    with tag('h2'):
        print('test')
        with tag('h5'):
            print('test2')

f()