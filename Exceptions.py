# ArithmeticError
try:
    result = 1 / 0
except ArithmeticError as e:
    print("ArithmeticError:", e)

# AssertionError
try:
    assert False, "Assertion failed"
except AssertionError as e:
    print("AssertionError:", e)

# AttributeError
try:
    x = 10
    x.append(5)
except AttributeError as e:
    print("AttributeError:", e)

# Exception
try:
    raise Exception("This is a base exception")
except Exception as e:
    print("Exception:", e)

# EOFError
try:
    input_data = input()
except EOFError as e:
    print("EOFError:", e)

# FloatingPointError
import math
try:
    math.sqrt(-1)
except FloatingPointError as e:
    print("FloatingPointError:", e)
pass

# GeneratorExit
try:
    def my_generator():
        yield 1
    gen = my_generator()
    next(gen)
    gen.close()
    next(gen)
except GeneratorExit as e:
    print("GeneratorExit:", e)

# ImportError
try:
    import non_existing_module
except ImportError as e:
    print("ImportError:", e)

# IndentationError
try:
    exec("if True:\n    print('Incorrect Indentation')")
except IndentationError as e:
    print("IndentationError:", e)

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("IndexError:", e)

# KeyError
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError as e:
    print("KeyError:", e)

# KeyboardInterrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print("KeyboardInterrupt: User interrupted the program")

# LookupError
try:
    raise LookupError("This is a lookup error")
except LookupError as e:
    print("LookupError:", e)

# MemoryError
try:
    a = [1] * (10**10)
except MemoryError as e:
    print("MemoryError:", e)

# NameError
try:
    print(non_existent_variable)
except NameError as e:
    print("NameError:", e)

# NotImplementedError
try:
    class MyClass:
        def my_method(self):
            raise NotImplementedError("Subclasses should implement this method")
    obj = MyClass()
    obj.my_method()
except NotImplementedError as e:
    print("NotImplementedError:", e)

# OSError
try:
    open('non_existing_file.txt', 'r')
except OSError as e:
    print("OSError:", e)

# OverflowError
try:
    x = 10**1000
except OverflowError as e:
    print("OverflowError:", e)

# ReferenceError
import weakref
try:
    class MyClass:
        pass
    obj = MyClass()
    weak_obj = weakref.ref(obj)
    del obj
    weak_obj()
except ReferenceError as e:
    print("ReferenceError:", e)

# RuntimeError
try:
    raise RuntimeError("A runtime error occurred")
except RuntimeError as e:
    print("RuntimeError:", e)

# StopIteration
try:
    def my_iterator():
        yield 1
    it = my_iterator()
    print(next(it))
    print(next(it))
except StopIteration as e:
    print("StopIteration:", e)

# SyntaxError
try:
    eval('x === y')
except SyntaxError as e:
    print("SyntaxError:", e)

# TabError
try:
    exec("if True:\n\tprint('TabError example')")
except TabError as e:
    print("TabError:", e)

# SystemError
try:
    raise SystemError("A system error occurred")
except SystemError as e:
    print("SystemError:", e)

# SystemExit
import sys
try:
    sys.exit("Exit the program")
except SystemExit as e:
    print("SystemExit:", e)

# TypeError
try:
    print("string" + 5)
except TypeError as e:
    print("TypeError:", e)

# UnboundLocalError
try:
    def test():
        print(a)
        a = 5
    test()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)

# UnicodeError
try:
    print(b'\xe2\x28\x82'.decode('ascii'))
except UnicodeError as e:
    print("UnicodeError:", e)

# UnicodeEncodeError
try:
    print("你好".encode('ascii'))
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)

# UnicodeDecodeError
try:
    b'\xe2\x28\x82'.decode('utf-8')
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)

# UnicodeTranslateError
try:
    "abc".translate({1: 'z'})
except UnicodeTranslateError as e:
    print("UnicodeTranslateError:", e)

# ValueError
try:
    int("hello")
except ValueError as e:
    print("ValueError:", e)

# ZeroDivisionError
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
