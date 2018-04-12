import os
import sys

# https://docs.python.org/3.3/tutorial/errors.html
try:
    # Block
    pass
except Exception as data:  # Can be tuple of Exceptions
    # data in most cases implements __str__ or __repr__
    pass
except:
    # Other exceptions
    pass
else:
    # If no raised exception
    pass
finally:
    # Always performs
    pass


######
class WinterError(Exception):
    def __init__(self):
        self.issuer, self.message = 'You are', 'Not prepared!'


class WildingError(WinterError):
    def __init__(self):
        super().__init__()
        self.message = 'We are going to light the biggest fire the North has ever seen!1!!'


class YgetteError(WildingError):
    def __init__(self):
        super().__init__()
        self.message = 'You know nothing, John Snow!'


class WhiteWalkerError(WinterError):
    pass


def winter_is_coming(): raise WinterError


def winter_is_here(): raise WhiteWalkerError

# https://docs.python.org/3.3/tutorial/errors.html#user-defined-exceptions

# We can raise exception to parent level
try:
    pass
except Exception:
    raise  # Raises the exception to parent level

# Approaches
# Look Before You Leap - Think carefully about what you are about to do before you do it.
# Easier to Ask for Forgiveness than Permission


# print()
### Finally!
try:
    source_file = open(sys.path[0]+'/source_file', 'r')

    buffer = []
    try:
        buffer = source_file.readlines()
    finally:
        source_file.close()

    target_file = open(sys.path[0]+'/target_file', 'w')
    try:
        for line in reversed(buffer):
            target_file.write(line.rstrip() + '\n')
    finally:
        target_file.close()
except IOError as e:
    print(e)
    print("Tough luck, junior")


# TL;DR ->
try:
    with open(sys.path[0]+'/source_file', 'r') as source_file:
        buffer = source_file.readlines()
    with open(sys.path[0]+'/target_file', 'w') as target_file:
        for line in reversed(buffer):
            target_file.write(line.rstrip() + '\n')
except IOError as e:
    print(e)
    print("Much better, now, ain't it?")

## https://docs.python.org/3.3/reference/compound_stmts.html#with
# With guarantee that the file would be closed automatically
# The result from the with expression is called Context Manager
# Its called __enter__() on CM then the result would be written in the name after as
# Execute the block
# If exception raises, then __exit(type, value, traceback) is calling on CM
# If exception not raises, then  __exit__(None, None, None) is calling on CM

# In other words:
with open('/etc/passwd') as passwd:
    buffer = passwd.readlines()
print('Done')

# Is the same as
passwd = open('/etc/passwd').__enter__()
try:
    buffer = passwd.readlines()
    passwd.__exit__(None, None, None)
except Exception:
    passwd.__exit__(*sys.exc_info())
print('Done')


#Manager example
class Manager:
    def __enter__(self):
        print("I've been entered!")
        return 42

    def __exit__(self, type, value, traceback):
        print("I've been exited!")


with Manager() as something:
    print('Am I inside?')
    print(something)


# with foo() as f, bar() as b:
# is the same as
# with foo() as f:
#     with bar() as b:
#         ...

# https://docs.python.org/3.3/library/contextlib.html
# Contextlib give us three very useful managers
# - closing
# - contextmanager
# - ContectDecorator

