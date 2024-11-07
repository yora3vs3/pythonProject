# abs()
print(abs(-7))  # Output: 7

# all()
print(all([True, True, False]))  # Output: False

# any()
print(any([False, False, True]))  # Output: True

# ascii()
print(ascii("Hello, 你好"))  # Output: 'Hello, \\u4f60\\u597d'

# bin()
print(bin(10))  # Output: '0b1010'

# bool()
print(bool(0))  # Output: False

# bytearray()
b_array = bytearray("Hello", "utf-8")
print(b_array)  # Output: bytearray(b'Hello')

# bytes()
b_obj = bytes("Hello", "utf-8")
print(b_obj)  # Output: b'Hello'

# callable()
def example_func():
    pass
print(callable(example_func))  # Output: True

# chr()
print(chr(97))  # Output: 'a'

# classmethod()
class Example:
    @classmethod
    def class_method(cls):
        return "I'm a class method"
print(Example.class_method())  # Output: "I'm a class method"

# compile()
code = compile("print(42)", "<string>", "exec")
exec(code)  # Output: 42

# complex()
c = complex(2, 3)
print(c)  # Output: (2+3j)

# delattr()
class Person:
    name = "John"
delattr(Person, "name")
# print(Person.name)  # AttributeError: type object 'Person' has no attribute 'name'

# dict()
my_dict = dict(name="Alice", age=25)
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}

# dir()
print(dir([]))  # Output: List of methods and attributes of list

# divmod()
print(divmod(10, 3))  # Output: (3, 1)

# enumerate()
for index, value in enumerate(["apple", "banana"]):
    print(index, value)
# Output:
# 0 apple
# 1 banana

# eval()
x = 1
print(eval('x + 1'))  # Output: 2

# exec()
exec("print(2 + 3)")  # Output: 5

# filter()
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # Output: [1, 2]

# float()
print(float("3.14"))  # Output: 3.14

# format()
print(format(123, "0>5"))  # Output: '00123'

# frozenset()
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})

# getattr()
class Example:
    name = "Alice"
print(getattr(Example, "name"))  # Output: 'Alice'

# globals()
print(globals())  # Output: Global symbol table dictionary

# hasattr()
class Example:
    name = "Alice"
print(hasattr(Example, "name"))  # Output: True

# hash()
print(hash("hello"))  # Output: An integer hash value

# help()
help(len)  # Shows help documentation for the 'len' function

# hex()
print(hex(255))  # Output: '0xff'

# id()
x = "hello"
print(id(x))  # Output: Unique identifier for 'x'

# input()
# name = input("Enter your name: ")
# print("Hello, " + name)

# int()
print(int("5"))  # Output: 5

# isinstance()
print(isinstance(5, int))  # Output: True

# issubclass()
class A: pass
class B(A): pass
print(issubclass(B, A))  # Output: True

# iter()
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))  # Output: 1

# len()
print(len("Hello"))  # Output: 5

# list()
my_list = list("hello")
print(my_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# locals()
def example():
    local_var = 5
    print(locals())
example()  # Output: Dictionary with local variables

# map()
print(list(map(lambda x: x * 2, [1, 2, 3])))  # Output: [2, 4, 6]

# max()
print(max([5, 10, 20]))  # Output: 20

# memoryview()
mv = memoryview(b"Hello")
print(mv[0])  # Output: 72

# min()
print(min([5, 10, 20]))  # Output: 5

# next()
iterator = iter([1, 2, 3])
print(next(iterator))  # Output: 1

# object()
obj = object()
print(obj)  # Output: <object object at ...>

# oct()
print(oct(8))  # Output: '0o10'

# open()
# with open("test.txt", "w") as file:
#     file.write("Hello, world!")

# ord()
print(ord('a'))  # Output: 97

# pow()
print(pow(2, 3))  # Output: 8

# print()
print("Hello, world!")  # Output: Hello, world!

# property()
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
person = Person(30)
print(person.age)  # Output: 30

# range()
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# repr()
print(repr("Hello\n"))  # Output: "'Hello\\n'"

# reversed()
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# round()
print(round(5.678, 2))  # Output: 5.68

# set()
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# setattr()
class Example:
    pass
setattr(Example, "name", "Alice")
print(Example.name)  # Output: Alice

# slice()
my_slice = slice(1, 5, 2)
print([1, 2, 3, 4, 5][my_slice])  # Output: [2, 4]

# sorted()
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# staticmethod()
class Example:
    @staticmethod
    def static_method():
        return "I'm static"
print(Example.static_method())  # Output: I'm static

# str()
print(str(100))  # Output: '100'

# sum()
print(sum([1, 2, 3]))  # Output: 6

# super()
class Parent:
    def say(self):
        return "Hello from Parent"
class Child(Parent):
    def say(self):
        return super().say() + " and Child"
print(Child().say())  # Output: Hello from Parent and Child

# tuple()
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# type()
print(type(5))  # Output: <class 'int'>

# vars()
class Example:
    def __init__(self):
        self.x = 5
print(vars(Example()))  # Output: {'x': 5}

# zip()
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))  # Output: [('Alice', 25), ('Bob', 30)]
