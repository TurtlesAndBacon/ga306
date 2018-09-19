#types of function arguments:

# 1. Standard - Positional - ex:
def standard_args(name, age):
   output = print("you are", name, "and you are", age, "years old")
   return output
standard_args('Jake', 29)

# 2. Default - ex:
def default_args(name, age='29'):
    print('you are', name, 'and you are', age, 'years old')
default_args('Jake')

# 3. Keyword Arguments - ex:
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))
test_var_kwargs(farg=1, myarg2="two", myarg3=3)

#4 Variable length argument - ex:
def vari_len(arg1, *argv):
    print("first argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

vari_len('You are', 'Jake', 'and you are', '29 years old')

# 5 Variable Length Keyword - ex:
def testify(arg1, *argv):
   print("first argument :", arg1)
   for arg in argv:
       print("Next argument through *argv :", arg)

   testify('Hello', 'Welcome', 'to', 'Computer')
