

# class Foo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Foo(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return '(' + str(self.x) + ', ' + str(self.y) + ')'
#
#
# a = Foo(1, 2)
# b = Foo(3, 4)
#
# print(a.x, a.y)
# print(b.x, b.y)
#
# a += b
#
# print(a.x, a.y)
#
# print(a)

# def foo(**kwargs):
#     for arg in kwargs:
#         print(arg, kwargs[arg])
#
#
# foo(a=1, b=2, c=3)
#
# foo(p=1)
#
# foo(q=[1, 2, 3])

a = set()

a.add(1)
print(a)

a.add(2)
a.add(3)
print(a)
print(a[0])