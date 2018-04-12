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





