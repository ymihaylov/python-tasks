# Funcitons are objects but have method __call__

global_one = 1

def foo():
    local_one = 2
    print(locals())

print(locals() == globals())

# ---

# One variable die when the scope die