def func(p, **test1):
	print(test1)

print(func(1, action="sum"))

# try:
#   # do something
# except Exception / (Tuple exceptions)
#   # print something else
# except OtherException
# else
#  if nothing raise
# finally - ever

# BaseExceptions
    # SystemExit
    # KeyboardIterupt
    # GeneratorExist
    # Exception
        # ...

# New exceptions must be extend Exception
# super() - get parent class
# 

class WinterError(Exception):
    def __init__(self):
        self.issuer, self.message = 'You are', 'NOT PREPARED!!11!!1'

class WildlingError(WinterError):
    def __init__(self):
        super().__init__()
        self.message = 'We are going to light the biggest fire the North has ever seen!1!!'

class YgetteError(WildlingError):
    def __init__(self):
        super().__init__()
        self.message = 'You know nothing, John Snow!'

class WhiteWalkerError(WinterError):
    pass

def winter_is_coming(): raise WinterError

def winter_is_here(): raise WhiteWalker()

# winter_is_coming()
# winter_is_here()

# raise in except
# try
    # with open - close the file
